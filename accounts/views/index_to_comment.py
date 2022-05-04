from ..models import User, Article, Comment
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from ..forms import CustomUserCreationForm, ArticleCreationForm, CommentCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# 로그인 안했을때 사이트 소개 페이지
def forAnonymousUser(request):
    return render(request, 'accounts/openingpage.html')


# 유저목록 보여주는 페이지 (이후 팔로우기능 추가되면 바뀔예정)
def userindex(request):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')

    userindexs = User.objects.all()
    context = {
        'userindexs':userindexs
    }
    return render(request, 'accounts/userindex.html', context)


# 개인계정 페이지 로드
def profile(request, username):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')
    
    user_name = get_object_or_404(User, username=username)
    user_pk = User.objects.filter(username=username).values('id').get().get('id')
    user_articles = Article.objects.filter(user_id=user_pk).order_by('-pk')
    context = {
        'user_name':user_name,
        'user_articles':user_articles,
    }
    return render(request, 'accounts/profile.html', context)


# 회원가입 페이지 로드
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:userindex')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.save()
        return redirect('accounts:userindex')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)


# 로그인 페이지 로드
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:userindex')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:userindex')
        
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:userindex')



# 게시글 작성 페이지 로드
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')

    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('accounts:profile', request.user)
    else:
        form = ArticleCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/create.html', context)



# 게시글 디테일 페이지 로드
def retrieve(request, username, p_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:forAnonymousUser')
        
    article = get_object_or_404(Article, pk=p_pk)
    form = CommentCreationForm()
    comments = article.comment_set.all()
    context = {
        'article':article,
        'form':form,
        'comments':comments
    }
    return render(request, 'accounts/detailpage.html', context)



# 댓글 작성 로직
def comments_create(request, username, p_pk):
    article = Article.objects.get(pk=p_pk)
    form = CommentCreationForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('accounts:retrieve', username, p_pk)
