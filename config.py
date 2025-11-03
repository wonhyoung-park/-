# 2025-10-27 - Smart Vocab Builder - 전역 설정
# 파일 위치: config.py

import os

# 프로젝트 루트 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 데이터베이스 설정
DB_DIR = os.path.join(BASE_DIR, 'resources')
DB_NAME = 'vocabulary.db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

# 애플리케이션 정보
APP_NAME = 'Smart Vocab Builder'
APP_VERSION = '1.0.0'
APP_AUTHOR = 'AI Software Student Team'

# 윈도우 설정
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 700

# 폰트 설정
DEFAULT_FONT_FAMILY = '맑은 고딕'
DEFAULT_FONT_SIZE = 14
CARD_FONT_SIZE = 32

# 로그 설정
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'app.log')
LOG_MAX_BYTES = 10 * 1024 * 1024  # 10MB
LOG_BACKUP_COUNT = 5

# 학습 기본 설정
DEFAULT_DAILY_WORD_GOAL = 50
DEFAULT_FLASHCARD_COUNT = 20