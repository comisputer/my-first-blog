#!/bin/bash
# PythonAnywhere에서 pa_autoconfigure_django.py 실행 후 패키지 설치 스크립트

echo "=== PythonAnywhere 패키지 자동 설치 시작 ==="

# 가상환경 활성화
source /home/inwoo/.virtualenvs/inwoo.pythonanywhere.com/bin/activate

echo "가상환경 활성화 완료"

# 필요한 패키지들 설치
echo "dataclasses 설치 중..."
pip install dataclasses

echo "djongo 설치 중..."
pip install djongo

echo "pymongo 설치 중..."
pip install pymongo

echo "설치된 패키지 확인:"
pip list | grep -E "(djongo|pymongo|dataclasses|Django)"

echo "=== 패키지 설치 완료 ==="

# Django 설정 확인
echo "Django 설정 테스트:"
cd /home/inwoo/inwoo.pythonanywhere.com
python manage.py check

echo "=== 모든 작업 완료 ==="
