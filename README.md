# Smart Vocabulary Builder (스마트 단어장)

영어 단어 학습을 위한 데스크톱 애플리케이션

## 📋 프로젝트 개요

고등학생 및 대학생을 위한 영어 단어 학습 프로그램입니다.
- **단어 관리**: CRUD, 검색, 즐겨찾기
- **플래시카드**: 반복 학습 지원
- **시험**: 단답형/객관식 시험
- **통계**: 학습 진척도 시각화
- **설정**: 테마, 학습 목표 설정

## 🛠️ 기술 스택

- **언어**: Python 3.8+
- **GUI**: PyQt5
- **데이터베이스**: SQLite
- **차트**: matplotlib
- **아키텍처**: MVC 패턴

## 📦 설치 및 실행 방법

### 1. 사전 준비

- Python 3.8 이상 설치 확인
  ```bash
  python --version
  ```

- Git 설치 확인
  ```bash
  git --version
  ```

### 2. 프로젝트 클론

```bash
git clone https://github.com/wonhyoung-park/-.git
cd smart_voca
```

### 3. 가상환경 생성 및 활성화

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 4. 패키지 설치

```bash
pip install -r requirements.txt
```

### 5. 프로그램 실행

```bash
python main.py
```

## 📁 프로젝트 구조

```
smart_voca/
├── config.py                 # 전역 설정
├── main.py                   # 진입점
├── requirements.txt          # 패키지 목록
│
├── controllers/              # 컨트롤러 계층
│   └── word_controller.py   # 단어 관리 컨트롤러
│
├── models/                   # 모델 계층
│   ├── base_model.py        # 기본 CRUD 모델
│   └── word_model.py        # 단어 모델
│
├── views/                    # 뷰 계층
│   ├── main_window.py       # 메인 윈도우
│   └── word_management/     # 단어 관리 뷰 (개발 중)
│
├── database/                 # 데이터베이스
│   ├── db_connection.py     # DB 연결 관리
│   ├── schema.sql           # 스키마 정의
│   └── init_data.sql        # 초기 데이터
│
├── utils/                    # 유틸리티
│   ├── logger.py            # 로깅
│   ├── csv_handler.py       # CSV 처리
│   ├── datetime_helper.py   # 날짜/시간 처리
│   └── validators.py        # 유효성 검증
│
├── resources/                # 리소스
│   └── styles/              # QSS 스타일시트
│       ├── light_theme.qss
│       └── dark_theme.qss
│
└── docs/                     # 문서
    ├── 기획/                 # 기획 문서
    ├── 설계/                 # 설계 문서
    └── 구현/                 # 구현 현황
```

## 🗄️ 데이터베이스 구조

- **words**: 단어 정보
- **learning_sessions**: 학습 세션
- **learning_history**: 학습 이력
- **exam_history**: 시험 이력
- **exam_questions**: 시험 문제
- **wrong_note**: 오답 노트
- **user_settings**: 사용자 설정

## 🚀 현재 개발 상황 (2025-11-03)

### ✅ 완료
- [x] 프로젝트 구조 설계
- [x] 데이터베이스 스키마 (7개 테이블)
- [x] 기본 MVC 구조
- [x] 단어 모델 및 컨트롤러
- [x] 메인 윈도우 (탭 기반)
- [x] 테마 시스템 (라이트/다크 모드)

### 🔧 개발 중
- [ ] 단어 관리 뷰
- [ ] 플래시카드 뷰
- [ ] 시험 뷰
- [ ] 통계 뷰
- [ ] 설정 뷰

## 📝 개발 가이드

### 새로운 환경에서 작업 시작하기

1. **저장소 클론**
   ```bash
   git clone https://github.com/wonhyoung-park/-.git
   cd smart_voca
   ```

2. **가상환경 설정**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **최신 코드 받기**
   ```bash
   git pull origin main
   ```

### 코드 변경 후 업로드

1. **변경사항 확인**
   ```bash
   git status
   ```

2. **변경사항 스테이징**
   ```bash
   git add .
   ```

3. **커밋**
   ```bash
   git commit -m "변경 내용 설명"
   ```

4. **푸시**
   ```bash
   git push origin main
   ```

## 🎨 코드 작성 규칙

1. **파일 헤더 필수**
   ```python
   # -*- coding: utf-8 -*-
   # 2025-11-03 - Smart Vocab Builder - 파일 설명
   # 파일 위치: 경로/파일명.py
   ```

2. **한글 주석 사용 권장**

3. **MVC 패턴 준수**
   - Model: 데이터 처리
   - View: UI 표시
   - Controller: 비즈니스 로직

## 📚 주요 문서

- [기획서](docs/기획/단어장_기획서_250929.md)
- [요구사항정의서](docs/기획/단어장_요구사항정의서_250929.md)
- [화면 설계서](docs/설계/단어장_화면%20설계서_251013.md)
- [아키텍처](docs/설계/단어장_아키텍처_251013_초안.md)
- [구현 현황](docs/구현/단어장_구현%20현황_251020_1132.md)

## 🐛 문제 해결

### PyQt5 설치 오류
```bash
pip install PyQt5==5.15.11
```

### 가상환경이 활성화되지 않을 때
- Windows: `venv\Scripts\activate.bat` 시도
- PowerShell: `venv\Scripts\Activate.ps1` 시도

### 데이터베이스 초기화
프로그램 실행 시 자동으로 `resources/vocabulary.db`가 생성됩니다.
문제 발생 시 해당 파일을 삭제하고 재실행하세요.

## 📄 라이선스

이 프로젝트는 학습 목적으로 제작되었습니다.

## 👥 기여자

- 박원형 (wonhyoung-park)

---

**최종 업데이트**: 2025-11-03
