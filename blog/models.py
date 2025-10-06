from django.db import models
from django.utils import timezone
from djongo import models as djongo_models


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


# MongoDB 전용 모델들
class UserProfile(djongo_models.Model):
    """MongoDB에서 사용자 프로필 정보를 저장하는 모델"""
    user_id = djongo_models.IntegerField()
    username = djongo_models.CharField(max_length=100)
    email = djongo_models.EmailField()
    bio = djongo_models.TextField(blank=True)
    avatar_url = djongo_models.URLField(blank=True)
    social_links = djongo_models.JSONField(default=dict)  # MongoDB의 유연한 JSON 필드
    created_at = djongo_models.DateTimeField(default=timezone.now)
    updated_at = djongo_models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
    
    def __str__(self):
        return f"{self.username} Profile"


class BlogPost(djongo_models.Model):
    """MongoDB에서 블로그 포스트를 저장하는 모델"""
    title = djongo_models.CharField(max_length=200)
    content = djongo_models.TextField()
    author_id = djongo_models.IntegerField()
    author_name = djongo_models.CharField(max_length=100)
    tags = djongo_models.JSONField(default=list)  # JSON 배열로 태그 저장
    metadata = djongo_models.JSONField(default=dict)  # 추가 메타데이터
    views_count = djongo_models.IntegerField(default=0)
    likes_count = djongo_models.IntegerField(default=0)
    is_published = djongo_models.BooleanField(default=False)
    created_at = djongo_models.DateTimeField(default=timezone.now)
    updated_at = djongo_models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'blog_posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Comment(djongo_models.Model):
    """MongoDB에서 댓글을 저장하는 모델"""
    post_id = djongo_models.CharField(max_length=100)  # ObjectId 대신 CharField 사용
    author_name = djongo_models.CharField(max_length=100)
    author_email = djongo_models.EmailField()
    content = djongo_models.TextField()
    is_approved = djongo_models.BooleanField(default=False)
    created_at = djongo_models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author_name} on {self.post_id}"