# blog_app/tests/test_views.py

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from blog_app.models import Post, Comment
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    response = client.post('/api/register/', {'username': 'newuser', 'password': 'newpassword'}, format='json')
    assert response.status_code == 201
    assert User.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_create_post_authenticated():
    user = User.objects.create_user(username='testuser', password='testpassword')
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.post('/api/posts/', {'title': 'New Post', 'content': 'This is a new post.', 'author': '1'}, format='json')
    print(response.content)
    assert response.status_code == 201

@pytest.mark.django_db
def test_create_post_unauthenticated():
    client = APIClient()
    response = client.post('/api/posts/', {'title': 'New Post', 'content': 'This is a new post.'}, format='json')
    assert response.status_code == 401

@pytest.mark.django_db
def test_like_post():
    user = User.objects.create_user(username='testuser', password='testpassword')
    token = Token.objects.create(user=user)
    post = Post.objects.create(title='Test Post', content='This is a test post.', author=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.patch(f'/api/posts/{post.id}/like/')
    assert response.status_code == 200
    assert post.likes.count() == 1

@pytest.mark.django_db
def test_create_comment_authenticated():
    user = User.objects.create_user(username='testuser', password='testpassword')
    token = Token.objects.create(user=user)
    post = Post.objects.create(title='Test Post', content='This is a test post.', author=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.post(f'/api/posts/{post.id}/comments/', {'text': 'This is a comment.', 'author': '1', 'post': '1'}, format='json')
    print(response.content)
    assert response.status_code == 201

@pytest.mark.django_db
def test_create_comment_unauthenticated():
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='This is a test post.', author=user)
    client = APIClient()
    response = client.post(f'/api/posts/{post.id}/comments/', {'text': 'This is a comment.'}, format='json')
    assert response.status_code == 401
