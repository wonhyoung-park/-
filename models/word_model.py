# 2025-10-27 - Smart Vocab Builder - 단어 Model
# 파일 위치: models/word_model.py

import logging
from models.base_model import BaseModel

logger = logging.getLogger(__name__)


class WordModel(BaseModel):
    """
    단어(words) 테이블 전용 Model
    """
    TABLE_NAME = 'words'
    PRIMARY_KEY = 'word_id'

    def get_all_active_words(self, order_by='english'):
        """
        삭제되지 않은 모든 단어 조회
        
        Args:
            order_by (str): 정렬 기준 컬럼
            
        Returns:
            list: 단어 목록
        """
        try:
            where_clause = "is_deleted = 0"
            return self.find_all(where_clause=where_clause, order_by=order_by)
        except Exception as e:
            logger.error(f"활성 단어 조회 실패: {e}")
            raise

    def get_favorites(self):
        """
        즐겨찾기 단어 조회
        
        Returns:
            list: 즐겨찾기 단어 목록
        """
        try:
            where_clause = "is_favorite = 1 AND is_deleted = 0"
            return self.find_all(where_clause=where_clause, order_by='english')
        except Exception as e:
            logger.error(f"즐겨찾기 조회 실패: {e}")
            raise

    def search_words(self, keyword, search_type='all'):
        """
        단어 검색
        
        Args:
            keyword (str): 검색 키워드
            search_type (str): 'english', 'korean', 'all'
            
        Returns:
            list: 검색 결과
        """
        try:
            if search_type == 'english':
                where_clause = "english LIKE ? AND is_deleted = 0"
            elif search_type == 'korean':
                where_clause = "korean LIKE ? AND is_deleted = 0"
            else:  # all
                where_clause = "(english LIKE ? OR korean LIKE ?) AND is_deleted = 0"
                params = (f'%{keyword}%', f'%{keyword}%')
                return self.find_all(where_clause=where_clause, params=params, order_by='english')
            
            params = (f'%{keyword}%',)
            return self.find_all(where_clause=where_clause, params=params, order_by='english')
        except Exception as e:
            logger.error(f"단어 검색 실패 (키워드={keyword}): {e}")
            raise

    def add_word(self, english, korean, memo=None):
        """
        단어 추가
        
        Args:
            english (str): 영어 단어
            korean (str): 한국어 뜻
            memo (str, optional): 메모
            
        Returns:
            int: 생성된 word_id
        """
        try:
            data = {
                'english': english.strip(),
                'korean': korean.strip(),
                'memo': memo.strip() if memo else None
            }
            return self.insert(data)
        except Exception as e:
            logger.error(f"단어 추가 실패 (영어={english}): {e}")
            raise

    def update_word(self, word_id, **kwargs):
        """
        단어 수정
        
        Args:
            word_id (int): 단어 ID
            **kwargs: 수정할 필드 (english, korean, memo 등)
            
        Returns:
            int: 영향받은 행 수
        """
        try:
            # 빈 값 제거
            data = {k: v for k, v in kwargs.items() if v is not None}
            
            if not data:
                logger.warning(f"수정할 데이터가 없음 (word_id={word_id})")
                return 0
            
            return self.update(word_id, data)
        except Exception as e:
            logger.error(f"단어 수정 실패 (word_id={word_id}): {e}")
            raise

    def toggle_favorite(self, word_id):
        """
        즐겨찾기 토글
        
        Args:
            word_id (int): 단어 ID
            
        Returns:
            int: 영향받은 행 수
        """
        try:
            word = self.find_by_pk(word_id)
            if not word:
                raise ValueError(f"단어를 찾을 수 없음: word_id={word_id}")
            
            new_favorite = 0 if word['is_favorite'] == 1 else 1
            return self.update(word_id, {'is_favorite': new_favorite})
        except Exception as e:
            logger.error(f"즐겨찾기 토글 실패 (word_id={word_id}): {e}")
            raise

    def update_statistics(self, word_id, is_correct):
        """
        단어 학습 통계 업데이트
        
        Args:
            word_id (int): 단어 ID
            is_correct (bool): 정답 여부
            
        Returns:
            int: 영향받은 행 수
        """
        try:
            word = self.find_by_pk(word_id)
            if not word:
                raise ValueError(f"단어를 찾을 수 없음: word_id={word_id}")
            
            from datetime import datetime
            
            if is_correct:
                data = {
                    'correct_count': word['correct_count'] + 1,
                    'last_learned_at': datetime.now().isoformat()
                }
            else:
                data = {
                    'wrong_count': word['wrong_count'] + 1,
                    'last_learned_at': datetime.now().isoformat()
                }
            
            return self.update(word_id, data)
        except Exception as e:
            logger.error(f"통계 업데이트 실패 (word_id={word_id}): {e}")
            raise