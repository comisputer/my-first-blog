"""
SQLite 호환 모델들 (PythonAnywhere용)
MongoDB 대신 SQLite를 사용할 때의 모델 정의
"""

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# SQLite 호환 모델들 (MongoDB 대신)
class UserProfile(models.Model):
    """SQLite에서 사용자 프로필 정보를 저장하는 모델"""
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True)
    social_links = models.JSONField(default=dict)  # Django 3.1+에서 지원
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
    
    def __str__(self):
        return f"{self.username} Profile"


class BlogPost(models.Model):
    """SQLite에서 블로그 포스트를 저장하는 모델"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_id = models.IntegerField()
    author_name = models.CharField(max_length=100)
    tags = models.JSONField(default=list)  # JSON 배열로 태그 저장
    metadata = models.JSONField(default=dict)  # 추가 메타데이터
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'blog_posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """SQLite에서 댓글을 저장하는 모델"""
    post_id = models.CharField(max_length=100)  # 포스트 ID
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author_name} on {self.post_id}"
