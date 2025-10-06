from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Post, UserProfile, BlogPost, Comment


# def post_list(request):
#     return HttpResponse("Blog index is working.")

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def chart_data(request):
    """Return JSON data for a mixed bar + line chart."""
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    bar_values = [120, 180, 130, 160, 210, 190]
    line_values = [100, 150, 140, 170, 200, 220]

    return JsonResponse(
        {
            "labels": labels,
            "bar": {
            "name": "Sales",
                "values": bar_values,
            },
            "line": {
                "name": "Forecast",
                "values": line_values,
            },
        }
    )


def chart_page(request):
    return render(request, 'blog/chart.html')


def chartjs_polar_page(request):
    return render(request, 'blog/chartjs_polar.html')


# MongoDB 데이터를 사용하는 새로운 뷰들
def mongodb_blog_list(request):
    """MongoDB에서 블로그 포스트 목록을 가져오는 뷰"""
    try:
        # MongoDB에서 모든 블로그 포스트 가져오기
        blog_posts = BlogPost.objects.filter(is_published=True)
        
        # 조회수 증가 (첫 번째 포스트만 예시)
        if blog_posts.exists():
            first_post = blog_posts.first()
            first_post.views_count += 1
            first_post.save()
        
        context = {
            'blog_posts': blog_posts,
            'total_posts': blog_posts.count(),
        }
        return render(request, 'blog/mongodb_blog_list.html', context)
    except Exception as e:
        context = {
            'error': f"MongoDB 연결 오류: {str(e)}",
            'blog_posts': [],
            'total_posts': 0,
        }
        return render(request, 'blog/mongodb_blog_list.html', context)


def mongodb_user_profiles(request):
    """MongoDB에서 사용자 프로필 목록을 가져오는 뷰"""
    try:
        user_profiles = UserProfile.objects.all()
        context = {
            'user_profiles': user_profiles,
            'total_users': user_profiles.count(),
        }
        return render(request, 'blog/mongodb_user_profiles.html', context)
    except Exception as e:
        context = {
            'error': f"MongoDB 연결 오류: {str(e)}",
            'user_profiles': [],
            'total_users': 0,
        }
        return render(request, 'blog/mongodb_user_profiles.html', context)


def mongodb_blog_detail(request, post_id):
    """MongoDB에서 특정 블로그 포스트의 상세 정보를 가져오는 뷰"""
    try:
        blog_post = get_object_or_404(BlogPost, id=post_id)
        
        # 조회수 증가
        blog_post.views_count += 1
        blog_post.save()
        
        # 관련 댓글 가져오기 (post_id를 문자열로 변환)
        comments = Comment.objects.filter(post_id=str(post_id), is_approved=True)
        
        context = {
            'blog_post': blog_post,
            'comments': comments,
            'comments_count': comments.count(),
        }
        return render(request, 'blog/mongodb_blog_detail.html', context)
    except Exception as e:
        context = {
            'error': f"포스트를 찾을 수 없습니다: {str(e)}",
        }
        return render(request, 'blog/mongodb_blog_detail.html', context)


@csrf_exempt
def create_mongodb_blog_post(request):
    """MongoDB에 새로운 블로그 포스트를 생성하는 뷰"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # 새로운 블로그 포스트 생성
            blog_post = BlogPost.objects.create(
                title=data.get('title', ''),
                content=data.get('content', ''),
                author_id=data.get('author_id', 1),
                author_name=data.get('author_name', 'Anonymous'),
                tags=data.get('tags', []),
                metadata=data.get('metadata', {}),
                is_published=data.get('is_published', False)
            )
            
            return JsonResponse({
                'success': True,
                'message': '블로그 포스트가 성공적으로 생성되었습니다.',
                'post_id': str(blog_post.id),
                'title': blog_post.title
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'오류가 발생했습니다: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'POST 요청만 허용됩니다.'
    })


def mongodb_analytics(request):
    """MongoDB 데이터를 사용한 분석 정보를 제공하는 뷰"""
    try:
        # 통계 데이터 수집
        total_posts = BlogPost.objects.count()
        published_posts = BlogPost.objects.filter(is_published=True).count()
        total_views = sum(post.views_count for post in BlogPost.objects.all())
        total_likes = sum(post.likes_count for post in BlogPost.objects.all())
        
        # 인기 태그 (간단한 예시)
        all_posts = BlogPost.objects.all()
        tag_counts = {}
        for post in all_posts:
            for tag in post.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # 상위 5개 태그
        popular_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # 최근 포스트
        recent_posts = BlogPost.objects.filter(is_published=True)[:5]
        
        context = {
            'total_posts': total_posts,
            'published_posts': published_posts,
            'total_views': total_views,
            'total_likes': total_likes,
            'popular_tags': popular_tags,
            'recent_posts': recent_posts,
        }
        return render(request, 'blog/mongodb_analytics.html', context)
    except Exception as e:
        context = {
            'error': f"분석 데이터를 가져오는 중 오류가 발생했습니다: {str(e)}",
            'total_posts': 0,
            'published_posts': 0,
            'total_views': 0,
            'total_likes': 0,
            'popular_tags': [],
            'recent_posts': [],
        }
        return render(request, 'blog/mongodb_analytics.html', context)