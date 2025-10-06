#!/bin/bash
# PythonAnywhere Django 프로젝트 상태 확인 스크립트
# requirements.txt를 통해 패키지가 자동 설치되므로 수동 설치 불필요

echo "=== PythonAnywhere Django 프로젝트 상태 확인 ==="

# 가상환경 활성화
source /home/inwoo/.virtualenvs/inwoo.pythonanywhere.com/bin/activate

echo "가상환경 활성화 완료"

# 설치된 패키지 확인
echo "설치된 패키지 확인:"
pip list | grep -E "(djongo|pymongo|dataclasses|Django|dnspython)"

echo "=== 패키지 확인 완료 ==="

# Django 설정 확인
echo "Django 설정 테스트:"
cd /home/inwoo/inwoo.pythonanywhere.com
python manage.py check

echo "=== 상태 확인 완료 ==="
