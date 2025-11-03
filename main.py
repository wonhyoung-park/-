# -*- coding: utf-8 -*-
# 2025-11-03 - Smart Vocab Builder - 메인 진입점
# 파일 위치: main.py

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from utils.logger import setup_logger
from database.db_connection import DBConnection

# Windows 환경 UTF-8 설정
if sys.platform == 'win32':
    import locale
    locale.setlocale(locale.LC_ALL, '')
    sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
    sys.stderr.reconfigure(encoding='utf-8') if hasattr(sys.stderr, 'reconfigure') else None

def initialize_database():
    """DB 초기화"""
    db = DBConnection.get_instance()

    # 스키마 실행
    schema_path = os.path.join('database', 'schema.sql')
    if os.path.exists(schema_path):
        db.execute_script(schema_path)
        print("[OK] DB 스키마 생성 완료!")

    # 초기 데이터 실행
    init_data_path = os.path.join('database', 'init_data.sql')
    if os.path.exists(init_data_path):
        db.execute_script(init_data_path)
        print("[OK] 초기 데이터 설정 완료!")

def main():
    setup_logger()
    initialize_database()

    app = QApplication(sys.argv)

    # 한글 폰트 설정
    app.setFont(QFont("맑은 고딕", 10))

    from views.main_window import MainWindow
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    
    # 테스트: 단어 추가
    from controllers.word_controller import WordController
    controller = WordController()
    
    try:
        word_id = controller.add_word('hello', '안녕', '인사말')
        print(f"✅ 단어 추가 성공! ID: {word_id}")
        
        words = controller.get_all_words()
        print(f"✅ 전체 단어 수: {len(words)}")
        for word in words:
            print(f"  - {word['english']}: {word['korean']}")
    except Exception as e:
        print(f"❌ 오류: {e}")

if __name__ == '__main__':
    main()