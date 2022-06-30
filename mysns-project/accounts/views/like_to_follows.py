from django.views.decorators.http import require_POST
from ..models import User, Article, Comment
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from ..forms import CustomUserCreationForm, ArticleCreationForm, CommentCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# 프로필 페이지에서 좋아요를 눌렀을때
def likeProfile(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')

    article = get_object_or_404(Article, pk=pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)

    else:
        article.like_users.add(request.user)

    return redirect('accounts:profile', article.user)


# 디테일 페이지에서 좋아요를 눌렀을때
def likeRetrieve(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')

    article = get_object_or_404(Article, pk=pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)

    else:
        article.like_users.add(request.user)
    print(request.POST.get('next'))
    return redirect('accounts:retrieve', article.user, pk)


# 팔로우 기능
@require_POST
def follow(request, user_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
        
    followUser = get_object_or_404(User, pk=user_pk)
    
    if followUser != request.user:
        if followUser.followers.filter(pk=request.user.pk).exists():
            followUser.followers.remove(request.user)
        else:
            followUser.followers.add(request.user)
            
    return redirect('accounts:profile', followUser.username)