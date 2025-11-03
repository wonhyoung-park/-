# 2025-10-27 - Smart Vocab Builder - 기본 Model 클래스
# 파일 위치: models/base_model.py

import logging
from database.db_connection import DBConnection

logger = logging.getLogger(__name__)


class BaseModel:
    """
    모든 Model의 기본 클래스
    공통 CRUD 연산 제공
    """
    TABLE_NAME = None  # 자식 클래스에서 반드시 정의
    PRIMARY_KEY = None  # 자식 클래스에서 반드시 정의

    def __init__(self):
        self.db = DBConnection.get_instance()

    def find_all(self, where_clause=None, params=None, order_by=None):
        """
        전체 레코드 조회
        
        Args:
            where_clause (str, optional): WHERE 조건
            params (tuple, optional): 조건 파라미터
            order_by (str, optional): 정렬 조건
            
        Returns:
            list: 조회 결과
        """
        try:
            query = f"SELECT * FROM {self.TABLE_NAME}"
            
            if where_clause:
                query += f" WHERE {where_clause}"
            
            if order_by:
                query += f" ORDER BY {order_by}"
            
            results = self.db.execute_query(query, params)
            return [dict(row) for row in results]
        except Exception as e:
            logger.error(f"전체 조회 실패 ({self.TABLE_NAME}): {e}")
            raise

    def find_by_pk(self, pk_value):
        """
        Primary Key로 단일 레코드 조회
        
        Args:
            pk_value: Primary Key 값
            
        Returns:
            dict: 조회 결과 또는 None
        """
        try:
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE {self.PRIMARY_KEY} = ?"
            results = self.db.execute_query(query, (pk_value,))
            
            if results:
                return dict(results[0])
            return None
        except Exception as e:
            logger.error(f"PK 조회 실패 ({self.TABLE_NAME}, PK={pk_value}): {e}")
            raise

    def insert(self, data):
        """
        레코드 삽입
        
        Args:
            data (dict): 삽입할 데이터
            
        Returns:
            int: 생성된 ID
        """
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?' for _ in data])
            query = f"INSERT INTO {self.TABLE_NAME} ({columns}) VALUES ({placeholders})"
            
            result = self.db.execute_update(query, tuple(data.values()))
            logger.info(f"레코드 삽입 성공 ({self.TABLE_NAME}, ID={result})")
            return result
        except Exception as e:
            logger.error(f"레코드 삽입 실패 ({self.TABLE_NAME}): {e}")
            raise

    def update(self, pk_value, data):
        """
        레코드 수정
        
        Args:
            pk_value: Primary Key 값
            data (dict): 수정할 데이터
            
        Returns:
            int: 영향받은 행 수
        """
        try:
            set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
            query = f"UPDATE {self.TABLE_NAME} SET {set_clause} WHERE {self.PRIMARY_KEY} = ?"
            
            params = list(data.values()) + [pk_value]
            result = self.db.execute_update(query, tuple(params))
            logger.info(f"레코드 수정 성공 ({self.TABLE_NAME}, PK={pk_value})")
            return result
        except Exception as e:
            logger.error(f"레코드 수정 실패 ({self.TABLE_NAME}, PK={pk_value}): {e}")
            raise

    def delete(self, pk_value, soft=True):
        """
        레코드 삭제 (논리적 삭제 또는 물리적 삭제)
        
        Args:
            pk_value: Primary Key 값
            soft (bool): True면 is_deleted=1, False면 물리적 삭제
            
        Returns:
            int: 영향받은 행 수
        """
        try:
            if soft:
                # 논리적 삭제
                query = f"UPDATE {self.TABLE_NAME} SET is_deleted = 1 WHERE {self.PRIMARY_KEY} = ?"
            else:
                # 물리적 삭제
                query = f"DELETE FROM {self.TABLE_NAME} WHERE {self.PRIMARY_KEY} = ?"
            
            result = self.db.execute_update(query, (pk_value,))
            logger.info(f"레코드 삭제 성공 ({self.TABLE_NAME}, PK={pk_value}, soft={soft})")
            return result
        except Exception as e:
            logger.error(f"레코드 삭제 실패 ({self.TABLE_NAME}, PK={pk_value}): {e}")
            raise