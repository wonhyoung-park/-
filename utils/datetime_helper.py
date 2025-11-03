# 2025-11-03 - Smart Vocab Builder - 날짜/시간 처리 유틸리티
# 파일 위치: utils/datetime_helper.py

from datetime import datetime, timedelta


def get_current_datetime():
    """
    현재 날짜/시간 반환 (ISO 8601 형식)

    Returns:
        str: YYYY-MM-DDTHH:MM:SS 형식
    """
    return datetime.now().isoformat()


def get_current_date():
    """
    현재 날짜 반환 (날짜만)

    Returns:
        str: YYYY-MM-DD 형식
    """
    return datetime.now().strftime('%Y-%m-%d')


def get_current_time():
    """
    현재 시간 반환 (시간만)

    Returns:
        str: HH:MM:SS 형식
    """
    return datetime.now().strftime('%H:%M:%S')


def format_datetime(dt_str, format='%Y-%m-%d %H:%M'):
    """
    ISO 형식 날짜/시간을 원하는 형식으로 변환

    Args:
        dt_str (str): ISO 8601 형식 날짜/시간
        format (str): 출력 형식

    Returns:
        str: 포맷된 날짜/시간
    """
    try:
        if not dt_str:
            return ""

        # ISO 형식 파싱
        dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        return dt.strftime(format)
    except Exception:
        return dt_str


def format_date(dt_str):
    """
    ISO 형식을 날짜만 반환 (YYYY-MM-DD)

    Args:
        dt_str (str): ISO 8601 형식 날짜/시간

    Returns:
        str: YYYY-MM-DD 형식
    """
    return format_datetime(dt_str, '%Y-%m-%d')


def format_time(dt_str):
    """
    ISO 형식을 시간만 반환 (HH:MM:SS)

    Args:
        dt_str (str): ISO 8601 형식 날짜/시간

    Returns:
        str: HH:MM:SS 형식
    """
    return format_datetime(dt_str, '%H:%M:%S')


def format_duration_seconds(seconds):
    """
    초를 MM:SS 또는 HH:MM:SS 형식으로 변환

    Args:
        seconds (int): 초

    Returns:
        str: 포맷된 시간
    """
    if not seconds or seconds < 0:
        return "00:00"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def format_duration_minutes(minutes):
    """
    분을 "N분" 형식으로 변환

    Args:
        minutes (int): 분

    Returns:
        str: "N분" 형식
    """
    if not minutes or minutes < 0:
        return "0분"

    return f"{minutes}분"


def get_days_ago(days):
    """
    N일 전 날짜 반환

    Args:
        days (int): 일 수

    Returns:
        str: YYYY-MM-DD 형식
    """
    date = datetime.now() - timedelta(days=days)
    return date.strftime('%Y-%m-%d')


def get_date_range(start_date_str, end_date_str):
    """
    시작일과 종료일 사이의 날짜 리스트 반환

    Args:
        start_date_str (str): YYYY-MM-DD 형식 시작일
        end_date_str (str): YYYY-MM-DD 형식 종료일

    Returns:
        list: 날짜 문자열 리스트
    """
    try:
        start = datetime.strptime(start_date_str, '%Y-%m-%d')
        end = datetime.strptime(end_date_str, '%Y-%m-%d')

        dates = []
        current = start
        while current <= end:
            dates.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=1)

        return dates
    except Exception:
        return []


def get_week_dates():
    """
    이번 주 날짜 리스트 반환 (월~일)

    Returns:
        list: 날짜 문자열 리스트
    """
    today = datetime.now()
    weekday = today.weekday()  # 월요일=0, 일요일=6

    # 이번 주 월요일 찾기
    monday = today - timedelta(days=weekday)

    dates = []
    for i in range(7):
        date = monday + timedelta(days=i)
        dates.append(date.strftime('%Y-%m-%d'))

    return dates


def get_weekday_name(date_str):
    """
    날짜에 해당하는 요일명 반환

    Args:
        date_str (str): YYYY-MM-DD 형식 날짜

    Returns:
        str: 요일명 (월, 화, 수, 목, 금, 토, 일)
    """
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        weekdays = ['월', '화', '수', '목', '금', '토', '일']
        return weekdays[date.weekday()]
    except Exception:
        return ""


def is_today(date_str):
    """
    오늘 날짜인지 확인

    Args:
        date_str (str): YYYY-MM-DD 형식 날짜

    Returns:
        bool: 오늘이면 True
    """
    return date_str == get_current_date()


def calculate_days_between(start_date_str, end_date_str):
    """
    두 날짜 사이의 일수 계산

    Args:
        start_date_str (str): YYYY-MM-DD 형식 시작일
        end_date_str (str): YYYY-MM-DD 형식 종료일

    Returns:
        int: 일수 (end - start)
    """
    try:
        start = datetime.strptime(start_date_str, '%Y-%m-%d')
        end = datetime.strptime(end_date_str, '%Y-%m-%d')
        return (end - start).days
    except Exception:
        return 0


def get_relative_time_str(dt_str):
    """
    상대적 시간 문자열 반환 (예: "2시간 전", "어제", "3일 전")

    Args:
        dt_str (str): ISO 8601 형식 날짜/시간

    Returns:
        str: 상대적 시간 표현
    """
    try:
        if not dt_str:
            return "알 수 없음"

        dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        now = datetime.now()
        diff = now - dt

        seconds = diff.total_seconds()

        if seconds < 60:
            return "방금 전"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes}분 전"
        elif seconds < 86400:
            hours = int(seconds / 3600)
            return f"{hours}시간 전"
        elif seconds < 172800:  # 2일
            return "어제"
        elif seconds < 604800:  # 7일
            days = int(seconds / 86400)
            return f"{days}일 전"
        else:
            return format_date(dt_str)

    except Exception:
        return dt_str
