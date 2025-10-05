from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('chart/', views.chart_page, name='chart_page'),
    path('chart/data/', views.chart_data, name='chart_data'),
]