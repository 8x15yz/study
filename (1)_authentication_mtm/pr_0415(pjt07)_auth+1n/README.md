# 0415/ pjt07

# [pjt07_img](./pjt07_img.md)

# 0. 목차

1. 초기환경 설정
2. Authentication System
   1. 로그인
   2. 로그아웃
   3. 회원가입
   4. 회원탈퇴
   5. 회원정보 수정
   6. 비밀번호 수정
3. 1 : N
   1. 게시글에 댓글 사용할수있도록 (Movie : Comment = 1 : N 관계 구현)
   2. 여러 유저들이 각각 글을 쓰는걸 연결 (User : Movie = 1 : N)
   3. 여러 유저들이 각각 댓글을 쓰는걸 연결 (User : Comment = 1 : N)
4. 추가 작업

# 1. 초기환경 설정

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
    'movies',
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
2. path('login/', views.login , name= 'login'), 
```

<hr>login form : views.py


1. GET 메서드로 요청을 받아올때 => login 폼 페이지를 렌더해주는 작업
2. POST 메서드로 요청을 받아올때 => 로그인 정보를 저장하는 작업

<hr>=> 폼을 먼저 보여줘야 되므로 1번 작업부터 진행해야됨


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

accounts > login.html 작성하기

### 2. POST 로 로그인정보 받아오기

##### accounts > views.py > login > pass 부분에

```
form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
```

##### base.html에 로그인 아이디 출력 + 로그인버튼 출력

##### accounts > login.html 마무리

form 태그를 만들고 `action 주소는 login`으로 + `메서드는post` + `csrf 토큰 `넣어주기



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
    return redirect('movies:index')
```

base.html에 로그아웃버튼 출력



## 로그아웃 + create작업 접근제한로직 만들기

##### base.html

if 태그를 사용하여 분기를 작성

```
{% if request.user.is_authenticated %}
게시글 작성 버튼 + 로그아웃 버튼
{% endif %}
```

##### movies > views.py

데코레이터를 사용하기 => 로그인 안하고 세가지 작업에 접근하려고 하면 login페이지를 리디렉트하고

```
1. from django.contrib.auth.decorators import login_required 모듈 임포트
2. create/ delete/ update 세가지에 대해 @login_required 붙여주기
```

리디렉트 하면서 주소창에 `?next=` 문자열과 함께 주소가 나옴:



# 4. 회원가입 작업 만들기

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

<hr>


### 1. signup폼 페이지를 렌더

##### accounts > views.py 완성코드

```
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

##### accounts > signup.html

폼 태그 불러와서 폼 넣어주기

## 회원가입과 동시에 자동 로그인 기능 주기

user = form.save()
auth_login(request, user) 를 추가해주면 됨



# 5. 회원탈퇴 작업 만들기

## urls + views + html 작성

##### accounts > urls.py

```
path('delete/', views.delete, name="delete"),
```

##### accounts > views.py

```
def delete(request):
    request.user.delete()
    return redirect('movies:index')
```



# 6. 회원정보 수정 작업

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



## 유저정보를 가져오는거에 로그인 강제성 부여

이거는 : 데코레이터를 쓰거나 is_authenticated 쓰거나 둘 중 하나 하라는 소리



## 회원정보 수정 페이지 정보 노출 제한 (UserchangeForm 커스텀)

### 1. accounts > forms.py

지금 내장폼을 사용하느라 모델 구조가 어떤지 알수없지만 모델을 일단 임포트를 할수있음 : get_user_model

 필드는 장고 공식문서를 보면 알수있고 거기서 이제 이메일정도만 불러옴

```
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomchangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = 'email' , 
```



## 커스텀 후 베이스코드 갈무리해주기 

##### accounts > views.py

UserChangeForm 삭제하고 CustomUserChangeForm으로 바꿔주기

update 함수에서도 UserChangeForm 지우고 CustomUserChangeForm으로 변경하기

```
from .forms import CustomUserChangeForm
```

나머지 update 함수 코드 채워주기

```
form = CustomUserChangeForm(request.POST, instance=request.user)
if form.is_valid():
      form.save()
      return redirect('movies:index')
```





# 7. 비밀번호 수정작업

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



## 비번 변경시 자동 로그아웃 현상 해결

이러는 이유: 비번 변경하면 세션도 바뀜 - 그러다보니 기존의 세션과 매칭이 안돼서 서로 다른 유저로 판단이 된다는 뜻

따라서 새로운 요청과 새로운 세션으로 업데이트 된 객체를 자동으로 가져오는 작업이 필요하다

```
from django.contrib.auth import update_session_auth_hash 모듈 불러오고

user = form.save()
update_session_auth_hash(request, user) 해시함수 넣어주는 것으로 변경
```

<hr>

#### authentication 작업 끝 !!

이제 1:N 관계를 만들어보려고 하는데 세가지 정도로 나눌 수 있겠음

1. Movie : Comment = 1 : N (게시글에 댓글 사용)
2. User : Movie = 1 : N (여러 유저들이 글을 작성하는)
3. User : Comment = 1 : N (여러 유저들이 댓글을 작성하는)

<hr>



# 8. 게시글에 댓글 사용할수있도록 (Movie : Comment = 1 : N 관계 구현)

## 댓글 모델 만들기

movie 앱에 가서 모델을 만들어주기

```
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content}'
```



## 댓글폼 디테일페이지에 나오도록 하기

1. 댓글폼 커스터마이징

##### movies > models.py

폼을 그대로 출력하면 어떤 게시글에 쓸지까지도 나오기 때문에 content만 나오도록 지정 이후에 생기는 문제는 views.py에서 해결해주기

```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'content',
```

2. 디테일페이지에 폼 내보내기 (뷰 함수에 코멘트 폼 받아서 context에 추가)

##### movies > views.py > detail

```
commentform = CommentForm()
context = {
    'movie' : movie,
    'commentform' : commentform,
}
```



## 댓글 작성 로직 만들기

##### movies > views.py > comments_create

```
def comments_create(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            movie = get_object_or_404(Movie, pk=pk)
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.movie = movie
                comment.save()
            return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')   
```

여기서 

comment = commentform.save(commit=False)

comment.movie = movie

comment.save()

이 부분은 IntegrityError를 해결하려고 작성한 코드이다

저 부분을 안 쓰고 commentform을 바로 저장하면 => 위에서 폼 커스텀할때 가린 "몇번 글에 댓글을 쓰는지"의 정보가 들어오지 않았기 때문에 NOT NULL constraint failed: articles_comment.article_id 의 문장과 함께  IntegrityError가 발생하기 때문에 commit을 사용

commit 이란 실제 데이터베이스에 저장하는 과정을 말하는데 이걸 False해줌으로써 db에 저장은 안하고 대신 인스턴스를 만들어 주게 된다.

즉 데이터베이스에 아직 저장은 안하고 인스턴스만 남겨서 다음 변수에서 값을 받아와 저장하도록 지정하는 문장인 것임



## 댓글 데이터 디테일페이지에 나오도록 하기

조회한 article의 모든 댓글을 조회해야됨 => `역참조`

article/views.py

detail 함수 부분을 comment_set 사용해서 다음과 같이 코드 추가해주기

##### movies > views.py > detail

```
comments = movie.comment_set.all()
context = {
     'movie' : movie,
     'commentform' : commentform,
     'comments' : comments
}
```



## 댓글 삭제 기능 만들기

로그인 한 사용자에 한해서 삭제 진행해줄 것이기 때문에 is authenticated를 사용

##### movies > views.py > comments_delete

```
def comments_delete(request, m_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('movies:detail', m_pk)
```

detail.html에 삭제 버튼 추가해주기



# 9. 여러 유저들이 각각 글을 쓰는걸 연결 (User : Movie = 1 : N)

## 연결을 위해 유저 모델 커스텀

1. 내장 모델을 상속

##### accounts > models.py

User으로 모델을 새로 정의하기

```
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

##### pjt06 > settings.py

왜래키 불러오기 위해 settings를 모듈로 불러올때 필요한 문장이고 앱 이름.모델명으로 작성한다

```
AUTH_USER_MODEL = 'accounts.User'
```

2. 중간에 새로운 모델 만들었으므로 migrations  초기화해주고 다시 등록해야됨

   1. db.sqlite 파일 삭제
   2. migrations dir 내 설계도 삭제
   3. 그렇게 한 다음 다시 makemigrations + migrate

3. admin.py 에다가 custom User 등록하기

   ##### accounts > admin.py

   ```
   from django.contrib.auth.admin import UserAdmin
   from .models import User
   
   admin.site.register(User, UserAdmin)
   ```

지금까지 내장 폼 썼는데 user모델을 커스텀했으니 폼도 같이 수정해주러 가야됨

UserCreationForm + UserChangeForm 두개 수정해야되는데 유저체인지는 이미 커스텀 폼을 사용하고 있어서 넘어갈 수 있음

## UserCreationForm 변경

get_user_model : 현재 활성화된 유저모델을 리턴하는 메서드 => 폼을 상속받고 model 지정할때 사용

views.py 에서 델을 다 커스텀으로 바꿔주자

## 모델에 왜래키 발급해주고 다시 migrations

cf) django에서 user model을 참조할 때:

1. models.py 에서는 `settings.AUTH_USER_MODEL` 사용 (str를 반환하기 때문)
2. 그 외의 곳에서는 `get_user_model()` (객체를 반환하기 때문)

여기서는 from django.conf import settings 해서 왜래키에 settings.AUTH_USER_MODEL 사용

이후 다시 makemigratinos + migrate

## 게시글 생성 페이지에서 작성자 선택지 없애주기

forms.py + views.py 건들러 가기

##### movies > forms.py

```
MovieForm에서 fields = '__all__' 부분 수정 => exclude = 'user',
```

##### movies > views.py

save 부분에 commit 여부를 False로 하고 인스턴스만 남긴다음에 movie 변수로 받고

무비 변수의  user 값을 현재 작성한 user (즉 request에서 받아온 유저)로 지정한다음 save

```
movie = form.save(commit=False)
movie.user = request.user
movie.save()
```

이렇게 하면 특정 게시글에 어떤 유저가 작성한 것인지도 이제 알 수 있음 => 이 정보로 게시글 삭제+수정 여부도 작성자에 한해서 제공할 수 있음

## User : Movie에서의 게시글 delete + update

1. 작성자 유저에 한하여 수정+삭제작업 구현 => if request.user == movie.user: 사용하면 됨
2. 게시글에 작성한 유저 명시 => 디테일 html페이지에서 .by {{movie.user}} 작성해주기
3. delete + update 버튼 노출 제한 => {% if request.user == movie.user %} 태그로 감싸주기



# 10.여러 유저들이 각각 댓글을 쓰는걸 연결 (User : Comment = 1 : N)

## comment모델에 유저 왜래키 연결해주기 + migrations

##### movies > models.py

```
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```



## 댓글작성 로직 수정

##### movies > views.py > comment_create

댓글 쓰는 유저가 현재 작성하는 유저 ( 즉 request에서 받아온 정보에 있는 유저) 인 것으로 지정

```
 comment.user = request.user
```



## User : Comment에서의 댓글delete + update

1. 작성자 유저에 한하여 삭제작업 

   ##### movies > views.py > comments_delete

   Comment 모델에서 pk값의 데이터를 받아오는 작업을 함수 바깥으로 꺼내서 comment 변수에 넣고

   comment 변수에 담긴 user 데이터를 request.user와 비교하면 됨

   ```
   def comments_delete(request, m_pk, comment_pk):
       comment = get_object_or_404(Comment, pk=comment_pk)
       if request.user.is_authenticated:
           if request.user == comment.user:
               comment.delete()
       return redirect('movies:detail', m_pk)
   ```

2. 댓글에 작성한 유저 명시 => 디테일 페이지에 . by {{ comment.user }} 작성

3. delete  버튼 노출 제한 => 디테일 페이지에  {% if request.user == comment.user %}로 감싸기

# 11. 추가작업

detail 페이지에서 게시글정보와 댓글 관련으로 두개의 공간을 나눠서 양 옆으로 배치할 수 있도록 했음
