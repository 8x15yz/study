import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
    PasswordChangeForm
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.views.decorators.http import require_POST

from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 이게 무슨의미지?
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')            # 여기까지 이부분 강의를 다시 들어야갰다
    else:
        forms = AuthenticationForm()
    context = {
        'forms':forms,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form, 
    }
    return render(request, 'accounts/change_password.html', context)