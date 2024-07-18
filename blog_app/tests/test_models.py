# blog_app/tests/test_models.py

import pytest
from django.contrib.auth.models import User
from blog_app.models import Post, Comment

@pytest.mark.django_db
def test_post_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='This is a test post.', author=user)
    assert post.title == 'Test Post'
    assert post.content == 'This is a test post.'
    assert post.author == user

@pytest.mark.django_db
def test_comment_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='This is a test post.', author=user)
    comment = Comment.objects.create(post=post, author='commenter', text='This is a test comment.')
    assert comment.text == 'This is a test comment.'
    assert comment.author == 'commenter'
    assert comment.post == post
