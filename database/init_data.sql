-- 2025-11-03 - Smart Vocab Builder - 초기 데이터
-- 파일 위치: database/init_data.sql

-- 사용자 설정 초기값
INSERT OR IGNORE INTO user_settings (setting_key, setting_value) VALUES
('theme', 'light'),
('font_size', '14'),
('daily_word_goal', '50'),
('daily_time_goal_minutes', '30'),
('exam_time_limit_minutes', '20'),
('flashcard_time_limit_seconds', '0'),
('window_width', '1200'),
('window_height', '800'),
('last_backup_date', '');
