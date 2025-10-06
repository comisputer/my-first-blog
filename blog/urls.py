from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('chart/', views.chart_page, name='chart_page'),
    path('chart/data/', views.chart_data, name='chart_data'),
    path('chartjs/polar/', views.chartjs_polar_page, name='chartjs_polar_page'),
    
    # MongoDB 관련 URL들
    path('mongodb/blog/', views.mongodb_blog_list, name='mongodb_blog_list'),
    path('mongodb/blog/<str:post_id>/', views.mongodb_blog_detail, name='mongodb_blog_detail'),
    path('mongodb/users/', views.mongodb_user_profiles, name='mongodb_user_profiles'),
    path('mongodb/analytics/', views.mongodb_analytics, name='mongodb_analytics'),
    path('mongodb/create-post/', views.create_mongodb_blog_post, name='create_mongodb_blog_post'),
]