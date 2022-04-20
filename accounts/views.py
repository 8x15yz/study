from django.shortcuts import render
from .models import User, Article, Comment
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ArticleCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def userindex(request):
    userindexs = User.objects.all()
    context = {
        'userindexs':userindexs
    }
    return render(request, 'accounts/userindex.html', context)

def profile(request, username):
    user_name = get_object_or_404(User, username=username)
    user_pk = User.objects.filter(username=username).values('id').get().get('id')
    print(user_pk, type(user_pk))
    user_articles = Article.objects.filter(user_id=user_pk)
    context = {
        'user_name':user_name,
        'user_articles':user_articles,
    }
    return render(request, 'accounts/profile.html', context)

def signup(request):
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

def login(request):
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

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:userindex')

def create(request):
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