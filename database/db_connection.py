# 2025-10-27 - Smart Vocab Builder - DB 연결 관리 (Singleton)
# 파일 위치: database/db_connection.py

import sqlite3
import os
import logging
from config import DB_PATH, DB_DIR

logger = logging.getLogger(__name__)


class DBConnection:
    """
    SQLite 데이터베이스 연결을 관리하는 Singleton 클래스
    """
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """싱글톤 인스턴스 반환"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def connect(self):
        """데이터베이스 연결"""
        if self._connection is None:
            try:
                # DB 디렉토리가 없으면 생성
                os.makedirs(DB_DIR, exist_ok=True)
                
                self._connection = sqlite3.connect(DB_PATH)
                self._connection.row_factory = sqlite3.Row  # 딕셔너리처럼 접근 가능
                logger.info(f"데이터베이스 연결 성공: {DB_PATH}")
            except Exception as e:
                logger.error(f"데이터베이스 연결 실패: {e}")
                raise
        return self._connection

    def close(self):
        """데이터베이스 연결 종료"""
        if self._connection:
            self._connection.close()
            self._connection = None
            logger.info("데이터베이스 연결 종료")

    def execute_query(self, query, params=None):
        """
        SELECT 쿼리 실행
        
        Args:
            query (str): SQL 쿼리
            params (tuple, optional): 쿼리 파라미터
            
        Returns:
            list: 조회 결과 리스트
        """
        try:
            conn = self.connect()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            results = cursor.fetchall()
            return results
        except Exception as e:
            logger.error(f"쿼리 실행 실패: {query}, 오류: {e}")
            raise

    def execute_update(self, query, params=None):
        """
        INSERT/UPDATE/DELETE 쿼리 실행
        
        Args:
            query (str): SQL 쿼리
            params (tuple, optional): 쿼리 파라미터
            
        Returns:
            int: 영향받은 행 수 또는 생성된 ID
        """
        try:
            conn = self.connect()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            conn.commit()
            
            # INSERT인 경우 생성된 ID 반환
            if query.strip().upper().startswith('INSERT'):
                return cursor.lastrowid
            else:
                return cursor.rowcount
        except Exception as e:
            conn.rollback()
            logger.error(f"업데이트 실행 실패: {query}, 오류: {e}")
            raise

    def execute_script(self, script_path):
        """
        SQL 스크립트 파일 실행
        
        Args:
            script_path (str): SQL 파일 경로
        """
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                script = f.read()
            
            conn = self.connect()
            cursor = conn.cursor()
            cursor.executescript(script)
            conn.commit()
            logger.info(f"스크립트 실행 완료: {script_path}")
        except Exception as e:
            logger.error(f"스크립트 실행 실패: {script_path}, 오류: {e}")
            raise