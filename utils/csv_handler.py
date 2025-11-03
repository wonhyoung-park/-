# 2025-11-03 - Smart Vocab Builder - CSV 처리 유틸리티
# 파일 위치: utils/csv_handler.py

import csv
import os
import logging

logger = logging.getLogger(__name__)


class CSVHandler:
    """CSV 파일 임포트/엑스포트 처리"""

    @staticmethod
    def parse_csv(file_path, encoding='utf-8'):
        """
        CSV 파일 파싱

        Args:
            file_path (str): CSV 파일 경로
            encoding (str): 파일 인코딩 (기본: utf-8)

        Returns:
            tuple: (success: bool, data: list or error_message: str)
        """
        if not os.path.exists(file_path):
            return False, "파일을 찾을 수 없습니다."

        try:
            words = []
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                # BOM 제거
                content = f.read()
                if content.startswith('\ufeff'):
                    content = content[1:]

                # CSV 파싱
                csv_reader = csv.DictReader(content.splitlines())

                # 필수 컬럼 확인
                if 'english' not in csv_reader.fieldnames or 'korean' not in csv_reader.fieldnames:
                    return False, "CSV 파일에 'english', 'korean' 컬럼이 필요합니다."

                for row_num, row in enumerate(csv_reader, start=2):
                    english = row.get('english', '').strip()
                    korean = row.get('korean', '').strip()
                    memo = row.get('memo', '').strip()

                    # 빈 행 건너뛰기
                    if not english and not korean:
                        continue

                    # 필수 필드 검증
                    if not english:
                        return False, f"{row_num}번째 줄: 영어 단어가 비어있습니다."
                    if not korean:
                        return False, f"{row_num}번째 줄: 한국어 뜻이 비어있습니다."

                    words.append({
                        'english': english,
                        'korean': korean,
                        'memo': memo if memo else None
                    })

            if not words:
                return False, "유효한 단어 데이터가 없습니다."

            logger.info(f"CSV 파싱 성공: {len(words)}개 단어")
            return True, words

        except UnicodeDecodeError:
            # UTF-8 실패시 CP949로 재시도
            if encoding == 'utf-8':
                logger.info("UTF-8 실패, CP949로 재시도")
                return CSVHandler.parse_csv(file_path, encoding='cp949')
            else:
                return False, "파일 인코딩을 읽을 수 없습니다. (UTF-8 또는 CP949 형식이어야 합니다)"

        except Exception as e:
            logger.error(f"CSV 파싱 오류: {e}")
            return False, f"CSV 파일 읽기 오류: {str(e)}"

    @staticmethod
    def export_to_csv(data, file_path, encoding='utf-8-sig'):
        """
        단어 데이터를 CSV 파일로 저장

        Args:
            data (list): 단어 데이터 리스트 (dict)
            file_path (str): 저장할 파일 경로
            encoding (str): 파일 인코딩 (기본: utf-8-sig, Excel 호환)

        Returns:
            tuple: (success: bool, error_message: str or None)
        """
        try:
            # 디렉토리가 없으면 생성
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_path, 'w', encoding=encoding, newline='') as f:
                fieldnames = ['english', 'korean', 'memo']
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                # 헤더 작성
                writer.writeheader()

                # 데이터 작성
                for word in data:
                    writer.writerow({
                        'english': word.get('english', ''),
                        'korean': word.get('korean', ''),
                        'memo': word.get('memo', '')
                    })

            logger.info(f"CSV 내보내기 성공: {file_path}, {len(data)}개 단어")
            return True, None

        except Exception as e:
            logger.error(f"CSV 내보내기 오류: {e}")
            return False, f"CSV 파일 저장 오류: {str(e)}"

    @staticmethod
    def get_csv_preview(file_path, max_rows=10):
        """
        CSV 파일 미리보기

        Args:
            file_path (str): CSV 파일 경로
            max_rows (int): 최대 표시 행 수

        Returns:
            tuple: (success: bool, preview_data: list or error_message: str)
        """
        success, result = CSVHandler.parse_csv(file_path)

        if not success:
            return False, result

        # 최대 행수만큼만 반환
        preview = result[:max_rows]
        return True, preview

    @staticmethod
    def validate_csv_format(file_path):
        """
        CSV 파일 형식 검증

        Args:
            file_path (str): CSV 파일 경로

        Returns:
            tuple: (is_valid: bool, error_message: str or word_count: int)
        """
        success, result = CSVHandler.parse_csv(file_path)

        if not success:
            return False, result

        # 성공시 단어 개수 반환
        return True, len(result)
