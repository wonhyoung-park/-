# 2025-10-27 - Smart Vocab Builder - 단어 Controller
# 파일 위치: controllers/word_controller.py

import logging
from models.word_model import WordModel

logger = logging.getLogger(__name__)


class WordController:
    """단어 관리 비즈니스 로직"""
    
    def __init__(self):
        self.model = WordModel()
    
    def get_all_words(self):
        """전체 단어 목록"""
        return self.model.get_all_active_words()
    
    def search_words(self, keyword, search_type='all'):
        """단어 검색"""
        return self.model.search_words(keyword, search_type)
    
    def add_word(self, english, korean, memo=None):
        """단어 추가"""
        if not english or not korean:
            raise ValueError("영어와 한국어는 필수입니다")
        return self.model.add_word(english, korean, memo)
    
    def update_word(self, word_id, **kwargs):
        """단어 수정"""
        return self.model.update_word(word_id, **kwargs)
    
    def delete_word(self, word_id):
        """단어 삭제"""
        return self.model.delete(word_id, soft=True)
    
    def toggle_favorite(self, word_id):
        """즐겨찾기 토글"""
        return self.model.toggle_favorite(word_id)