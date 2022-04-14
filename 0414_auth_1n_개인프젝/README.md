

# 명세서 - Authentications 부터 1:N까지

과정만 적어보자 과정만

## 목차

1. 유저작업 이전에 초기화 사항 `v`
2. 로그인 작업 만들기`v`
3. 로그아웃 작업 만들기
4. 기타작업
5. 회원가입 작업 만들기
6. 회원탈퇴 작업 만들기
7. 회원정보 수정 작업
8. 비밀번호 수정작업
9. 중간에 데코레이터 정리
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

## 로그인 + 로그아웃 작업 접근제한로직 만들기

## next 파라미터 다루기 

## delete 동작에서 로그인에 성공할시 405 오류

# 5. 회원가입 작업 만들기

## 회원가입 폼 만들기 (내장폼 불러오기)

## urls + views + html 작성

## 회원가입과 동시에 자동 로그인 기능 주기

# 6. 회원탈퇴 작업 만들기

## urls + views + html 작성

# 7. 회원정보 수정 작업

## 회원정보 수정  폼 만들기 (내장폼 불러오기)

## 베이스코드 작성

## 유저정보를 가져오는거에 로그인을 해야된다는 강제성 부여

## 회원정보 수정 페이지 정보 노출 제한 (UserchangeForm 커스텀)

## 커스텀 후 베이스코드 갈무리해주기 

# 8. 비밀번호 수정작업

## 비밀번호 수정 폼 만들기 (내장폼 불러오기)

## 베이스코드 작성

## 필수 위치인자 `user`누락이슈 해결해주기

## 커스텀 후 베이스코드 갈무리해주기 

## 비번 변경시 자동 로그아웃 이슈 해결해주기

# 9. 중간에 데코레이터 정리

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

