from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
def userindex(request):
    userindexs = User.objects.all()
    context = {
        'userindexs':userindexs
    }
    return render(request, 'accounts/userindex.html', context)

def profile(request, username):
    username = get_object_or_404(User, username=username)
    context = {
        'username':username
    }
    return render(request, 'accounts/profile.html', context)