-- 2025-11-03 - Smart Vocab Builder - 데이터베이스 스키마 (전체)
-- 파일 위치: database/schema.sql

-- 1. 단어 테이블
CREATE TABLE IF NOT EXISTS words (
    word_id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT NOT NULL UNIQUE,
    korean TEXT NOT NULL,
    memo TEXT,
    is_favorite INTEGER DEFAULT 0,
    correct_count INTEGER DEFAULT 0,
    wrong_count INTEGER DEFAULT 0,
    last_learned_at TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    is_deleted INTEGER DEFAULT 0
);

-- 2. 학습 세션 테이블
CREATE TABLE IF NOT EXISTS learning_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_type TEXT NOT NULL CHECK(session_type IN ('flashcard', 'review')),
    study_mode TEXT NOT NULL CHECK(study_mode IN ('en_to_ko', 'ko_to_en')),
    order_type TEXT NOT NULL CHECK(order_type IN ('sequential', 'random', 'personalized')),
    total_words INTEGER NOT NULL DEFAULT 0,
    correct_count INTEGER NOT NULL DEFAULT 0,
    wrong_count INTEGER NOT NULL DEFAULT 0,
    started_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    ended_at TEXT,
    duration_seconds INTEGER DEFAULT 0
);

-- 3. 학습 이력 테이블
CREATE TABLE IF NOT EXISTS learning_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
    is_correct INTEGER NOT NULL,
    response_time_seconds INTEGER,
    learned_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (session_id) REFERENCES learning_sessions(session_id),
    FOREIGN KEY (word_id) REFERENCES words(word_id)
);

-- 4. 시험 이력 테이블
CREATE TABLE IF NOT EXISTS exam_history (
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_type TEXT NOT NULL CHECK(exam_type IN ('short_answer', 'multiple_choice', 'mixed')),
    question_mode TEXT NOT NULL CHECK(question_mode IN ('en_to_ko', 'ko_to_en', 'mixed')),
    order_type TEXT NOT NULL CHECK(order_type IN ('random', 'personalized')),
    total_questions INTEGER NOT NULL,
    score REAL NOT NULL,
    correct_count INTEGER NOT NULL,
    wrong_count INTEGER NOT NULL,
    time_limit_minutes INTEGER,
    time_taken_seconds INTEGER,
    started_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    ended_at TEXT
);

-- 5. 시험 문제 테이블
CREATE TABLE IF NOT EXISTS exam_questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
    question_number INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    user_answer TEXT,
    is_correct INTEGER,
    choice_1 TEXT,
    choice_2 TEXT,
    choice_3 TEXT,
    choice_4 TEXT,
    FOREIGN KEY (exam_id) REFERENCES exam_history(exam_id),
    FOREIGN KEY (word_id) REFERENCES words(word_id)
);

-- 6. 오답 노트 테이블
CREATE TABLE IF NOT EXISTS wrong_note (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    exam_id INTEGER,
    wrong_count INTEGER DEFAULT 1,
    is_resolved INTEGER DEFAULT 0,
    added_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    resolved_at TEXT,
    FOREIGN KEY (word_id) REFERENCES words(word_id),
    FOREIGN KEY (exam_id) REFERENCES exam_history(exam_id)
);

-- 7. 사용자 설정 테이블
CREATE TABLE IF NOT EXISTS user_settings (
    setting_key TEXT PRIMARY KEY,
    setting_value TEXT NOT NULL,
    updated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);

-- 8. 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_words_english ON words(english);
CREATE INDEX IF NOT EXISTS idx_words_favorite ON words(is_favorite);
CREATE INDEX IF NOT EXISTS idx_words_deleted ON words(is_deleted);
CREATE INDEX IF NOT EXISTS idx_learning_history_session ON learning_history(session_id);
CREATE INDEX IF NOT EXISTS idx_learning_history_word ON learning_history(word_id);
CREATE INDEX IF NOT EXISTS idx_exam_questions_exam ON exam_questions(exam_id);
CREATE INDEX IF NOT EXISTS idx_exam_questions_word ON exam_questions(word_id);
CREATE INDEX IF NOT EXISTS idx_wrong_note_word ON wrong_note(word_id);
CREATE INDEX IF NOT EXISTS idx_wrong_note_resolved ON wrong_note(is_resolved);