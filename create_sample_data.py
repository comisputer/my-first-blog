#!/usr/bin/env python
"""
MongoDB에 샘플 데이터를 생성하는 스크립트
Django shell에서 실행하거나 직접 실행할 수 있습니다.
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blog.models import UserProfile, BlogPost, Comment

def create_sample_users():
    """샘플 사용자 프로필 생성"""
    sample_users = [
        {
            'user_id': 1,
            'username': '김철수',
            'email': 'kim@example.com',
            'bio': '웹 개발자입니다. Django와 MongoDB를 좋아합니다.',
            'avatar_url': 'https://via.placeholder.com/150/667eea/ffffff?text=김',
            'social_links': {
                'github': 'https://github.com/kim',
                'twitter': 'https://twitter.com/kim',
                'linkedin': 'https://linkedin.com/in/kim'
            }
        },
        {
            'user_id': 2,
            'username': '이영희',
            'email': 'lee@example.com',
            'bio': '풀스택 개발자로 일하고 있습니다. 새로운 기술을 배우는 것을 좋아합니다.',
            'avatar_url': 'https://via.placeholder.com/150/764ba2/ffffff?text=이',
            'social_links': {
                'github': 'https://github.com/lee',
                'blog': 'https://lee-blog.com'
            }
        },
        {
            'user_id': 3,
            'username': '박민수',
            'email': 'park@example.com',
            'bio': '데이터 분석가입니다. MongoDB와 Python을 주로 사용합니다.',
            'avatar_url': 'https://via.placeholder.com/150/667eea/ffffff?text=박',
            'social_links': {
                'github': 'https://github.com/park',
                'medium': 'https://medium.com/@park'
            }
        }
    ]
    
    created_users = []
    for user_data in sample_users:
        user, created = UserProfile.objects.get_or_create(
            user_id=user_data['user_id'],
            defaults=user_data
        )
        if created:
            created_users.append(user)
            print(f"사용자 생성: {user.username}")
        else:
            print(f"사용자 이미 존재: {user.username}")
    
    return created_users

def create_sample_blog_posts():
    """샘플 블로그 포스트 생성"""
    sample_posts = [
        {
            'title': 'Django와 MongoDB 연동하기',
            'content': '''Django에서 MongoDB를 사용하는 방법에 대해 알아보겠습니다.

## 1. djongo 설치
pip install djongo

## 2. 설정 파일 수정
settings.py에서 DATABASES 설정을 변경합니다.

## 3. 모델 정의
djongo.models를 사용하여 MongoDB 모델을 정의합니다.

이렇게 하면 Django ORM의 편리함을 유지하면서 MongoDB의 유연성을 활용할 수 있습니다.''',
            'author_id': 1,
            'author_name': '김철수',
            'tags': ['Django', 'MongoDB', 'Python', '웹개발'],
            'metadata': {
                'category': 'tutorial',
                'difficulty': 'intermediate',
                'reading_time': 5
            },
            'views_count': random.randint(50, 200),
            'likes_count': random.randint(10, 50),
            'is_published': True
        },
        {
            'title': 'MongoDB의 장점과 특징',
            'content': '''MongoDB는 NoSQL 데이터베이스로 다음과 같은 특징을 가지고 있습니다:

## 주요 특징
- 문서 기반 데이터 저장
- 스키마가 유연함
- 수평적 확장 가능
- JSON 형태의 데이터 저장

## 장점
1. 빠른 개발 속도
2. 유연한 스키마
3. 높은 성능
4. 쉬운 확장성

MongoDB는 특히 웹 애플리케이션에서 많이 사용되고 있습니다.''',
            'author_id': 2,
            'author_name': '이영희',
            'tags': ['MongoDB', 'NoSQL', '데이터베이스'],
            'metadata': {
                'category': 'guide',
                'difficulty': 'beginner',
                'reading_time': 3
            },
            'views_count': random.randint(30, 150),
            'likes_count': random.randint(5, 30),
            'is_published': True
        },
        {
            'title': 'Django REST Framework와 MongoDB',
            'content': '''Django REST Framework를 사용하여 MongoDB API를 구축하는 방법을 알아보겠습니다.

## 필요한 패키지
- django-rest-framework
- djongo
- pymongo

## API 구현
1. Serializer 정의
2. ViewSet 구현
3. URL 라우팅
4. 권한 설정

이를 통해 강력한 REST API를 구축할 수 있습니다.''',
            'author_id': 3,
            'author_name': '박민수',
            'tags': ['Django', 'REST', 'API', 'MongoDB'],
            'metadata': {
                'category': 'tutorial',
                'difficulty': 'advanced',
                'reading_time': 7
            },
            'views_count': random.randint(20, 100),
            'likes_count': random.randint(3, 20),
            'is_published': True
        },
        {
            'title': 'MongoDB 성능 최적화 팁',
            'content': '''MongoDB의 성능을 최적화하는 방법들을 정리해보겠습니다.

## 인덱스 활용
- 자주 쿼리되는 필드에 인덱스 생성
- 복합 인덱스 활용
- 인덱스 크기 모니터링

## 쿼리 최적화
- projection 사용
- limit과 skip 적절히 활용
- aggregation pipeline 활용

## 하드웨어 최적화
- SSD 사용
- 충분한 RAM 확보
- 네트워크 최적화''',
            'author_id': 1,
            'author_name': '김철수',
            'tags': ['MongoDB', '성능', '최적화', '인덱스'],
            'metadata': {
                'category': 'guide',
                'difficulty': 'advanced',
                'reading_time': 6
            },
            'views_count': random.randint(40, 180),
            'likes_count': random.randint(8, 40),
            'is_published': True
        },
        {
            'title': 'Django에서 MongoDB 트랜잭션 처리',
            'content': '''Django에서 MongoDB 트랜잭션을 처리하는 방법에 대해 알아보겠습니다.

## 트랜잭션의 필요성
- 데이터 일관성 보장
- 동시성 제어
- 롤백 기능

## 구현 방법
1. 세션 기반 트랜잭션
2. 컨텍스트 매니저 활용
3. 에러 처리

주의사항과 모범 사례도 함께 알아보겠습니다.''',
            'author_id': 2,
            'author_name': '이영희',
            'tags': ['Django', 'MongoDB', '트랜잭션', '데이터베이스'],
            'metadata': {
                'category': 'tutorial',
                'difficulty': 'intermediate',
                'reading_time': 8
            },
            'views_count': random.randint(25, 120),
            'likes_count': random.randint(4, 25),
            'is_published': False  # 임시저장 상태
        }
    ]
    
    created_posts = []
    for post_data in sample_posts:
        post = BlogPost.objects.create(**post_data)
        created_posts.append(post)
        print(f"블로그 포스트 생성: {post.title}")
    
    return created_posts

def create_sample_comments(posts):
    """샘플 댓글 생성"""
    sample_comments = [
        {
            'author_name': '홍길동',
            'author_email': 'hong@example.com',
            'content': '정말 유용한 정보네요! 감사합니다.',
            'is_approved': True
        },
        {
            'author_name': '정수진',
            'author_email': 'jung@example.com',
            'content': 'Django와 MongoDB 연동이 이렇게 간단할 줄 몰랐습니다. 좋은 글 감사합니다!',
            'is_approved': True
        },
        {
            'author_name': '최민호',
            'author_email': 'choi@example.com',
            'content': 'MongoDB의 장점이 잘 정리되어 있네요. 공유해주셔서 감사합니다.',
            'is_approved': True
        },
        {
            'author_name': '김지영',
            'author_email': 'kimji@example.com',
            'content': 'REST API 구축에 대한 내용이 도움이 많이 되었습니다.',
            'is_approved': True
        },
        {
            'author_name': '이준호',
            'author_email': 'leejun@example.com',
            'content': '성능 최적화 팁들이 실무에 바로 적용할 수 있을 것 같습니다.',
            'is_approved': True
        }
    ]
    
    created_comments = []
    for post in posts:
        # 각 포스트당 1-3개의 댓글 생성
        num_comments = random.randint(1, 3)
        selected_comments = random.sample(sample_comments, min(num_comments, len(sample_comments)))
        
        for comment_data in selected_comments:
            comment = Comment.objects.create(
                post_id=str(post.id),  # post_id를 문자열로 변환
                **comment_data
            )
            created_comments.append(comment)
            print(f"댓글 생성: {comment.author_name} -> {post.title}")
    
    return created_comments

def main():
    """메인 실행 함수"""
    print("=== MongoDB 샘플 데이터 생성 시작 ===")
    
    try:
        # 기존 데이터 삭제 (선택사항)
        print("\n1. 기존 데이터 확인...")
        print(f"기존 사용자 수: {UserProfile.objects.count()}")
        print(f"기존 블로그 포스트 수: {BlogPost.objects.count()}")
        print(f"기존 댓글 수: {Comment.objects.count()}")
        
        # 샘플 데이터 생성
        print("\n2. 샘플 사용자 생성...")
        users = create_sample_users()
        
        print("\n3. 샘플 블로그 포스트 생성...")
        posts = create_sample_blog_posts()
        
        print("\n4. 샘플 댓글 생성...")
        comments = create_sample_comments(posts)
        
        print("\n=== 샘플 데이터 생성 완료 ===")
        print(f"생성된 사용자: {len(users)}명")
        print(f"생성된 블로그 포스트: {len(posts)}개")
        print(f"생성된 댓글: {len(comments)}개")
        
        print("\n=== 생성된 데이터 요약 ===")
        print(f"총 사용자 수: {UserProfile.objects.count()}")
        print(f"총 블로그 포스트 수: {BlogPost.objects.count()}")
        print(f"총 댓글 수: {Comment.objects.count()}")
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
