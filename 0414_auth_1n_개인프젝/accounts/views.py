from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 이게 무슨의미지?
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')            # 여기까지 이부분 강의를 다시 들어야갰다
    else:
        forms = AuthenticationForm()
    context = {
        'forms':forms,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')
