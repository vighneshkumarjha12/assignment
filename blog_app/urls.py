# blog_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import BlogPostViewSet, CommentViewSet, LikeViewSet
from . import views

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),  # <- new detail route
]
