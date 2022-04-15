

# 명세서 - Authentications 부터 1:N까지

과정만 적어보자 과정만

## 목차

1. 유저작업 이전에 초기화 사항 `v`
2. 로그인 작업 만들기`v`
3. 로그아웃 작업 만들기`v`
4. 기타작업`v`
5. 회원가입 작업 만들기`v`
6. 회원탈퇴 작업 만들기`v`
7. 회원정보 수정 작업`v`
8. 비밀번호 수정작업`v`
9. 중간에 데코레이터 정리`v`
10. 게시글에 댓글 사용할수있도록 (Article : Comment = 1 : N 관계 구현)
11. 여러 유저들이 각각 글을 쓰는걸 연결 (User : Article = 1 : N)
12. 여러 유저들이 각각 댓글을 쓰는걸 연결 (User : Comment = 1 : N)



# 과정

# 1. 유저작업 이전에 초기화 사항

## accounts 앱 생성

python manage.py startapp accounts



## urls, settings.py 초기구성

##### crud > urls.py

```
path('accounts/', include('accounts.urls')),
```

##### crud > settings.py

```
INSTALLED_APPS = [
    'articles',
    'accounts', ... ]
```

##### accounts > urls.py (생성)

```
from django.urls import path

app_name = 'accounts'
urlpatterns = []
```



## 계정만들어놓기 createsuperuser

```
python manage.py createsuperuser
```



# 2. 로그인 작업 만들기

## 로그인 폼 만들기 (내장폼 불러오기)

##### account > views.py

```
1. redirect 임포트
2. from django.contrib.auth.forms import AuthenticationForm 임포트
```

## urls + views + html 작성

##### accounts > urls.py

```
1. from . import views 임포트
2. path('login/', views.login, name="login"),
```

<hr>login form : views.py

1. GET 메서드로 요청을 받아올때 => login 폼 페이지를 렌더해주는 작업
2. POST 메서드로 요청을 받아올때 => 로그인 정보를 저장하는 작업

<hr>=> 1번 작업부터 진행할 것임

### 1. login 폼 페이지를 렌더

##### accounts > views.py

```
def login(request):
    if request.method == 'POST':
        pass
    else:
        forms = AuthenticationForm()
    context = {
        'forms':forms,
    }
    return render(request, 'accounts/login.html', context)
```

##### accounts > login.html (생성)

```
{% extends 'base.html' %}
{% block content %}
{{forms}}
<button>제출</button>
{% endblock content %}
```

### //2. POST 로 로그인정보 받아오기

##### accounts > views.py > login > pass 부분에

```
# 근데 나 이거 무슨 의민지 모르겠어 다시 강의를 들어야겟음
form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
```

##### base.html에 로그인 아이디 출력 + 로그인버튼 출력

##### accounts > login.html 마무리

form 태그를 만들고 `action 주소는 login`으로 + `메서드는post` + `csrf 토큰 `넣어주기

```
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'accounts:login'%}" method="POST">
    {% csrf_token %}
    {{forms.as_p}}
<button>제출</button>
</form>
{% endblock content %}
```



# 3. 로그아웃 작업 만들기

## urls + views + html 작성

##### accounts > urls.py

```
path('logout/', views.logout, name="logout"),
```

##### accounts > views.py

```
1. from django.contrib.auth import logout as auth_logout 모듈 임포트
2. def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

##### base.html에 로그아웃버튼 출력



# 4. 기타작업

## 로그인 + 로그아웃 + create작업 접근제한로직 만들기

##### base.html

if 태그를 사용하여 분기를 작성

```
{% if request.user.is_authenticated %}
<div><a href="{% url 'articles:create' %}"><button>[CREATE]</button></a></div>
<div><a href="{% url 'accounts:logout' %}"><button>로그아웃</button></a></div>
{% else %}
<div><a href="{% url 'accounts:login' %}"><button>로그인</button></a></div>
{% endif %}
```

##### articles > views.py

데코레이터를 사용하기 => 로그인 안하고 세가지 작업에 접근하려고 하면 login페이지를 리디렉트하고

```
1. from django.contrib.auth.decorators import login_required 모듈 임포트
2. create/ delete/ update 세가지에 대해 @login_required 붙여주기
```

리디렉트 하면서 주소창에 `?next=` 문자열과 함께 주소가 나옴:

## //next 파라미터 다루기 (views.py + login.html 변경)

원래 가려고 했던 주소를 로그인하면 보내준다는 뜻

이제 이 문자열을 views\.py에서 다뤄줘야 위의 문장처럼 실행될 수 있음

##### accounts > views.py > login 함수

리디렉트할때 `request.GET.get('next') or`  문장을 추가해주기

```
return redirect(request.GET.get('next') or 'articles:index')
```

or의 역할: nest가 있다면 그 주소로 리디렉트, 아니면 index로 리디렉트

##### accounts > login.html

action 란을 비워주기 =>  login으로 요청을 보내는게 아니라 next 쿼리에서 명시하는 주소로 요청을 보내고 싶은 것이기 때문에 action을 따로 지정하지 않고, next 쿼리가 써져있는 주소창에 작성되어있는 주소의 urls로 요청을 보내려고 하는 것이다

## //delete 동작에서 로그인에 성공할시 405 오류

데코레이터 조합 오류 => required_POST, login_required 데코레이터를 같이 쓰면 

요청할 때 오류가 생김:

여기서 우리는 login_required를 is_authenticated로 바꿔주면서 방지할수 있었음

##### articles > views.py > delete 함수

```
1. from django.views.decorators.http import require_POST 임포트
2. delete 함수 위에 @require_POST 작성
3. def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```



# 5. 회원가입 작업 만들기

## 회원가입 폼 만들기 (내장폼 불러오기)

##### accounts > views.py

```
1. from django.contrib.auth.forms 에 UserCreationForm 추가
```

## urls + views + html 작성

##### accounts > urls.py

```
path('signup/', views.signup, name="signup"),
```

<hr>signup form : views.py

1. GET 메서드로 요청을 받아올때 => signup폼 페이지를 렌더해주는 작업
2. POST 메서드로 요청을 받아올때 => 신규 회원정보를 저장하는 작업

<hr>=> 1번 작업부터 진행할 것임

### 1. signup폼 페이지를 렌더

##### accounts > views.py 완성코드

```
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

##### accounts > signup.html

```
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{form}}
    <button>횐가입</button>
</form>
{% endblock content %}
```

## 회원가입과 동시에 자동 로그인 기능 주기

```
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
```

user = form.save()
auth_login(request, user) 를 추가해주면 됨



# 6. 회원탈퇴 작업 만들기

## urls + views + html 작성

##### accounts > urls.py

```
path('delete/', views.delete, name="delete"),
```

##### accounts > views.py

```
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

##### base.html

```
<div><a href="{% url 'accounts:delete' %}"><button>횐탈퇴</button></a></div> 버튼 추가
```

#### futher logic : 데코레이터+is_auth~ 사용해서 로그인한 사용자만 횐탈퇴할수있도록 하는 코드

##### accounts > views.py

```
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # 요 로직은 로그아웃하면서 세션 지우려고 추가한 코드임
    return redirect('articles:index')
```



# 7. 회원정보 수정 작업

## 회원정보 수정  폼 만들기 (내장폼 불러오기)

##### accounts > views.py

```
from django.contrib.auth.forms 에 UserChangeForm 모듈 불러오기
```

## 베이스코드 작성

##### accounts > urls.py

```
path('update/', views.update, name="update"),
```

##### accounts > views.py

기본틀 로직으로 먼저 만들어놓기

```
def update(request):
    if request.method == 'POST':
        pass
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
```

##### accounts > update.html (생성)

```
{% extends 'base.html' %}   
{% block content %}
<form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>제출</button>
</form>
{% endblock content %}
```



## 유저정보를 가져오는거에 로그인을 해야된다는 강제성 부여

이거는 : 데코레이터를 쓰거나 is_authenticated 쓰거나 둘 중 하나 하라는 소리임



## 회원정보 수정 페이지 정보 노출 제한 (UserchangeForm 커스텀)

### 1. accounts > forms.py

여기서 좀 설명이 필요한데 =>지금 우리는 내장폼을 사용하느라 모델 구조가 어떤지 알수없음 

하지만 지금 우리는 페이지에서 노출하고싶은 필드만 골라서 커스텀할거니까 모델을 일단 임포트를 할수있음 : get_user_model

 필드는 장고 공식문서를 보면 알수있고 거기서 이제 이메일+ 이름 정도만 불러오려고 함

```
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```



## 커스텀 후 베이스코드 갈무리해주기 

##### accounts > views.py

UserChangeForm 삭제하고 CustomUserChangeForm으로 바꿔줄거셈

update 함수에서도 UserChangeForm 지우고 CustomUserChangeForm으로 변경하기

```
from .forms import CustomUserChangeForm
```

나머지 update 함수 코드 채워주기

```
form = CustomUserChangeForm(request.POST, instance=request.user)
if form.is_valid():
      form.save()
      return redirect('articles:index')
```





# 8. 비밀번호 수정작업

## 비밀번호 수정 폼 만들기 (내장폼 불러오기)

PasswordChangeForm 사용할거임 views.py에 모듈 임포트하기

## 베이스코드 작성

##### accounts > urls.py

```
path('password/', views.change_password, name="change_password"),
```

##### accounts > views.py

기본틀 로직으로 먼저 만들어놓기

```
def change_password(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordChangeForm()
    context = {
        'form':form, 
    }
    return render(request, 'accounts/change_password.html', context)
```

accounts > change_password.html (생성)

```
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <button>제출</button>
</form>
{% endblock content %}
```





## //필수 위치인자 `user`누락이슈 해결해주기

메서드에 request.user를 쓰먄 해결되는데 왜 그런건지 모르겠음 => 강의를 듣자 ?

```
def change_password(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordChangeForm()
    context = {
        'form':form, 
    }
    return render(request, 'accounts/change_password.html', context)
```



## 커스텀 후 베이스코드 갈무리해주기 

```
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form, 
    }
    return render(request, 'accounts/change_password.html', context)
```



## 비번 변경시 자동 로그아웃 이슈 해결해주기

이러는 이유: 비번 변경하면 세션도 바뀜 - 그러다보니 기존의 세션과 매칭이 안돼서 서로 다른 유저로 판단이 된다는 뜻

따라서 새로운 요청과 새로운 세션으로 업데이트 된 객체를 자동으로 가져오는 작업이 필요하다

```
from django.contrib.auth import update_session_auth_hash 모듈 불러오고

user = form.save()
update_session_auth_hash(request, user) 해시함수 넣어주는 것으로 변경
```

<hr>

#### authentication 작업 끝 !!

<hr>

# 9. 중간에 데코레이터 정리

 데ㅌ코레이터는 강의를 들어야됨



# 10. 게시글에 댓글 사용할수있도록 (Article : Comment = 1 : N 관계 구현)

## 댓글 모델 만들기

## 댓글폼 디테일페이지에 나오도록 하기

## 댓글 작성 로직 만들기

## 댓글 데이터 디테일페이지에 나오도록 하기

## 댓글 삭제 구현

# 11. 여러 유저들이 각각 글을 쓰는걸 연결 (User : Article = 1 : N)

## 연결을 위해 유저 모델 커스텀하기

1. 중간에 새로운 모델 만들었으므로 migrations  초기화해주고 다시 등록
2. 회원가입 폼 변경하기
3. 회원정보수정 폼 변경하기

## 모델에 왜래키 발급해주고 다시 migrations

## 왜래키 발급이슈로 인해 발생하는 잡음 정리해주기

## User : Article에서의 게시글 delete + update

1. 작성자 유저에 한하여 수정+삭제작업 구현
2. 게시글에 작성한 유저 명시
3. delete + update 버튼 노출 제한

# 12.여러 유저들이 각각 댓글을 쓰는걸 연결 (User : Comment = 1 : N)

## comment모델에 유저 왜래키 연결해주기 + migrations

## 댓글작성 로직에 왜래키 변경사항 잡음 정리해주러가기

## User : Comment에서의 게시글 delete + update

1. 작성자 유저에 한하여 수정+삭제작업 구현
2. 댓글에 작성한 유저 명시
3. delete + update 버튼 노출 제한

