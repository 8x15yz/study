from msilib.schema import CreateFolder
from django.shortcuts import render, redirect
from django.contrib.auth.forms import(
    AuthenticationForm,
    PasswordChangeForm
) 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from accounts.forms import CustomchangeForm, CustomUserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('movies:index')
    else :
        form = AuthenticationForm()
    context = {
       'form' : form
        }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.save()
        return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:login')


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('accounts:login')


def update(request):
    if request.method == 'POST':
        form = CustomchangeForm(request.POST, instance = request.user )
        form.save()
        return redirect('movies:index')

    else :
        form = CustomchangeForm(instance = request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)


def password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():        
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('movies:index')
        else: 
            form = PasswordChangeForm(request.user)
        context = {
            'form' : form
        }
        return render(request, 'accounts/password.html',context)
    return redirect('accounts:login')

    