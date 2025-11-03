# 2025-11-03 - Smart Vocab Builder - 로깅 설정 (UTF-8 인코딩)
# 파일 위치: utils/logger.py

import logging
import os
import sys
from config import LOG_DIR, LOG_FILE

def setup_logger():
    """로거 설정 (한글 깨짐 방지)"""
    os.makedirs(LOG_DIR, exist_ok=True)

    # Windows 콘솔 UTF-8 설정
    if sys.platform == 'win32':
        try:
            # stdout, stderr을 UTF-8로 재설정
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            pass

    # StreamHandler에 UTF-8 인코딩 명시
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # FileHandler에 UTF-8 인코딩 명시
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, stream_handler]
    )