# 2025-11-03 - Smart Vocab Builder - 입력 검증 유틸리티
# 파일 위치: utils/validators.py

import re


def validate_english_word(word):
    """
    영어 단어 검증

    Args:
        word (str): 검증할 영어 단어

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not word or not word.strip():
        return False, "영어 단어를 입력해주세요."

    word = word.strip()

    if len(word) > 100:
        return False, "영어 단어는 100자 이하로 입력해주세요."

    # 영어, 공백, 하이픈만 허용
    if not re.match(r'^[a-zA-Z\s\-]+$', word):
        return False, "영어 단어는 영문자, 공백, 하이픈(-)만 사용할 수 있습니다."

    return True, ""


def validate_korean_meaning(meaning):
    """
    한국어 뜻 검증

    Args:
        meaning (str): 검증할 한국어 뜻

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not meaning or not meaning.strip():
        return False, "한국어 뜻을 입력해주세요."

    meaning = meaning.strip()

    if len(meaning) > 200:
        return False, "한국어 뜻은 200자 이하로 입력해주세요."

    return True, ""


def validate_memo(memo):
    """
    메모 검증

    Args:
        memo (str): 검증할 메모

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not memo:
        return True, ""  # 메모는 선택사항

    memo = memo.strip()

    if len(memo) > 500:
        return False, "메모는 500자 이하로 입력해주세요."

    return True, ""


def validate_word_entry(english, korean, memo=None):
    """
    단어 입력 전체 검증

    Args:
        english (str): 영어 단어
        korean (str): 한국어 뜻
        memo (str, optional): 메모

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    # 영어 단어 검증
    is_valid, error = validate_english_word(english)
    if not is_valid:
        return False, error

    # 한국어 뜻 검증
    is_valid, error = validate_korean_meaning(korean)
    if not is_valid:
        return False, error

    # 메모 검증
    if memo:
        is_valid, error = validate_memo(memo)
        if not is_valid:
            return False, error

    return True, ""


def validate_positive_integer(value, min_value=1, max_value=None, field_name="값"):
    """
    양의 정수 검증

    Args:
        value: 검증할 값
        min_value (int): 최소값
        max_value (int, optional): 최대값
        field_name (str): 필드명 (에러 메시지용)

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    try:
        int_value = int(value)

        if int_value < min_value:
            return False, f"{field_name}은(는) {min_value} 이상이어야 합니다."

        if max_value and int_value > max_value:
            return False, f"{field_name}은(는) {max_value} 이하여야 합니다."

        return True, ""
    except (ValueError, TypeError):
        return False, f"{field_name}은(는) 숫자여야 합니다."


def validate_time_limit(minutes):
    """
    시간 제한 검증 (분 단위)

    Args:
        minutes: 제한 시간 (분)

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    return validate_positive_integer(minutes, min_value=1, max_value=180, field_name="시간 제한")


def validate_question_count(count):
    """
    문제 수 검증

    Args:
        count: 문제 수

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    return validate_positive_integer(count, min_value=5, max_value=100, field_name="문제 수")


def validate_daily_goal(count):
    """
    일일 목표 검증

    Args:
        count: 목표 단어 수

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    return validate_positive_integer(count, min_value=1, max_value=200, field_name="일일 목표")
