from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, RegisterUserView, CustomAuthToken, LikePostAPIView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like-post'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
