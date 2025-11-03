# -*- coding: utf-8 -*-
# 2025-11-03 - Smart Vocab Builder - 메인 윈도우 (탭 기반)
# 파일 위치: views/main_window.py

import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget,
                             QLabel, QMessageBox, QMenuBar, QMenu, QAction, QStatusBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, APP_VERSION


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_theme = 'light'
        self.init_ui()
        self.load_theme()

    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(1000, 700)

        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # 탭 위젯 생성
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabPosition(QTabWidget.North)
        layout.addWidget(self.tabs)

        # 탭 추가
        self.add_tabs()

        # 메뉴바 생성
        self.create_menu_bar()

        # 상태바 생성
        self.create_status_bar()

    def add_tabs(self):
        """탭 추가"""
        # 단어 관리 탭 (임시 플레이스홀더)
        word_tab = QWidget()
        word_layout = QVBoxLayout(word_tab)
        word_layout.addWidget(QLabel("단어 관리 화면"))
        self.tabs.addTab(word_tab, "단어 관리")

        # 플래시카드 탭
        flashcard_tab = self.create_placeholder_tab("플래시카드 학습 화면")
        self.tabs.addTab(flashcard_tab, "플래시카드")

        # 시험 탭
        exam_tab = self.create_placeholder_tab("시험 화면")
        self.tabs.addTab(exam_tab, "시험")

        # 통계 탭
        stats_tab = self.create_placeholder_tab("학습 통계 화면")
        self.tabs.addTab(stats_tab, "통계")

        # 설정 탭
        settings_tab = self.create_placeholder_tab("설정 화면")
        self.tabs.addTab(settings_tab, "설정")

    def create_placeholder_tab(self, text):
        """플레이스홀더 탭 생성"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel(text)
        label.setFont(QFont("맑은 고딕", 16))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        info_label = QLabel("(준비 중)")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)

        return widget

    def create_menu_bar(self):
        """메뉴바 생성"""
        menubar = self.menuBar()

        # 파일 메뉴
        file_menu = menubar.addMenu("파일(&F)")

        exit_action = QAction("종료(&X)", self)
        exit_action.setShortcut("Alt+F4")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 보기 메뉴
        view_menu = menubar.addMenu("보기(&V)")

        # 테마 변경
        theme_menu = view_menu.addMenu("테마")

        light_action = QAction("라이트 모드", self)
        light_action.triggered.connect(lambda: self.change_theme('light'))
        theme_menu.addAction(light_action)

        dark_action = QAction("다크 모드", self)
        dark_action.triggered.connect(lambda: self.change_theme('dark'))
        theme_menu.addAction(dark_action)

        # 도움말 메뉴
        help_menu = menubar.addMenu("도움말(&H)")

        about_action = QAction("정보(&A)", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_status_bar(self):
        """상태바 생성"""
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage(f"{APP_NAME} v{APP_VERSION} - 준비 완료")

    def load_theme(self):
        """테마 로드"""
        theme_file = f"resources/styles/{self.current_theme}_theme.qss"

        if os.path.exists(theme_file):
            try:
                with open(theme_file, 'r', encoding='utf-8') as f:
                    self.setStyleSheet(f.read())
            except Exception as e:
                print(f"테마 로드 실패: {e}")

    def change_theme(self, theme):
        """테마 변경"""
        self.current_theme = theme
        self.load_theme()
        self.statusBar.showMessage(f"테마 변경: {theme} 모드")

    def show_about(self):
        """정보 다이얼로그"""
        QMessageBox.about(
            self,
            "정보",
            f"<h2>{APP_NAME}</h2>"
            f"<p>버전: {APP_VERSION}</p>"
            f"<p>영어 단어 학습 프로그램</p>"
            f"<p>© 2025 All Rights Reserved</p>"
        )

    def update_status(self, message):
        """상태바 메시지 업데이트"""
        self.statusBar.showMessage(message)