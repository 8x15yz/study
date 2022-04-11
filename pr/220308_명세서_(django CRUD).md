# 0. 목차

1. 초기설정 (model 등록 + migrations)
2. shell으로 데이터 다루기
3. admin site 들어가기
4. 페이지 만들기 초기설정
5. 게시물 작성페이지 만들기(new.html)
6. 게시물작성 확인페이지 만들기 (create.html)
7. 게시물 디테일페이지 만들기 (detail.html)
8. 게시글 쓰면 가는 페이지 바꾸는 작업 구현
9. 게시글 지우는 작업 구현하기
10. 다음 단계로 넘어가기 전에: GET -> POST
11. 게시글 수정 페이지 만들기
12. 데이터 수정 완료 후 업데이트 페이지 만들기
13. 버튼으로 페이지들 연결하기 + 추가기능



# 1. 초기설정 (model 등록 + migrations)

##### 1. 앱 만들고 settings.py에 등록

##### 2. ipython, django_extensions 설치하고 settings.py에 등록

##### 3. 앱의 models.py에 코드등록

```
class Article(models.Model):
	title = models.Chafield(max_length=10)
	content = models.TextField()
```

##### 4. 터미널에 명령어 두개 순서대로 작성

```
python manage.py makemigrations
python manage.py migrate
```

##### 5. models.py에 새로운 코드 등록 + str 함수 써주기

`models.py에 새로운 코드 등록하게되면 꼭 4번과정 다시해줘야됨 !!`

`그리고 빈칸처리할까냐는 질문에 1으로 대답하면 됨`

```
class Article(models.Model):
	title = models.Chafield(max_length=10)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
    def __str__(self): # 이 함수 꼭 안으로 들여써줘야되는거 알지 ?? 클래스 내 함수니까
        return f'{self.pk} - {self.title} - {self.content} - {self.created_at} - {self.updated_at}'
```



# 2. shell으로 데이터 다루기

#### 1. 터미널에 쉘 환경으로 바꾸는 명령어 작성

```
python manage.py shell_plus
```



#### 2. 쉘환경으로 CRUD 작업 진행해보기

##### 1) READ

```
Article.objects.all() - 데이터 유무를 확인 (READ)
```

`all()`  `get()`  `filter()`  세가지 어떻게쓰는지 내일 공부다시



##### 2) CREATE (3가지)

```
article = Article()
article.title = '제목 넣기'
article.content = '내용 넣기'
article.save()
```

```
article = Article(title='제목 넣기', content='내용 넣기')
article.save()
```

```
Article,objects.create(title='제목 넣기', content='내용 넣기')
# save 필요없음
```

=> 테이블확인은 `sqilte.explorer`에서 가능



##### 3) DELETE + UPDATE - 완전 나중에 언급할거임

#### 일단은 이쯤하고 쉘환경 닫기

CREATE로 쿼리셋 몇개 만들어놓고  `exit()` 으로 쉘환경 빠져나오기



# 3. admin site 들어가기

##### 1. admin 접근하기 위해 관리자 계정 만들어주기

```
python manage.py createsuperuser
```

아이디 = admin 

비번 = 1234 로 적용해줌

##### 2. 앱 디렉토리/admin.py 파일에다가 객체가 관리자 인터페이스를 가진다는 것을 알려야됨

```
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

##### 3. admin 사이트 들어가서 Article 잘 생성됐나 확인해보기



# 4. 페이지 만들기 초기설정

#### 1. base.html 만들기 

```
1. 제일 상위 디렉토리에 만들고 네비게이션 바 만들어서 홈버튼이랑 글쓰기버튼 만들어놓기
2. DIRS에다가 베이스 템플릿 있는 곳 변경하기
```

#### 2. practice/urls.py + articles/urls.py 작업

```
1. urls.py에 include 모듈 임포트하고
2. 앱의 url과 연결시켜주기 => include('articles.urls')
3. article/urls.py 새로 만들어서 모듈 임포트하고 urlpatterns 지정해서 urls 환경 만들기
```

#### 3. 앱 디렉토리/템플릿 작업

```
1. articles/templates/articles/ 형태로 nested 구조 만들기
```

#### 4. index 페이지 만들어서 연결들이 잘 됐나 확인하기

`articles/urls.py` 

```
1. from . import views => 모듈 임포트해주기
2. app_name = 'articles' => 앱네임 적용하기
3. path 작성하기 -> 이때 주소는 비우기 (articles/ 가 곧 인덱스 페이지가 됨)
```

`articles/views.py`

```
인덱스페이지가 게시글을 보여주는 곳이므로 렌더할때 context 변수도 함께 내보내야됨
1. 함수 생성하고 articles 변수 만들어서 오더바이 그거 써주기 
	=> 그니까 지금 이 과정이 CRUD 중에서 "READ" 작업을 하는거임
	   원래는 Articles.objects.all() 으로 모든 쿼리셋을 보는거였는데
	   지금은 Articles.objects.order_by('-pk') 써줘서 게시글을 최신글 먼저 보게되는
2. context 변수 만들어서 articles 변수 디셔너리 값으로 넣어주기
3. 리턴 값에 context 추가해주기
```

`templates/articles/indx.html`

```
1. extends + block 적용
2. for 태그 써서 게시글 여러개 내보낼 수 있도록 하기
3. 카드 스타일 써서 게시글을 하나단위로 묶기
4. 카드 내용에는 게시글 번호 + 제목만 보이도록 하기
```

`추가작업`

```
base.html에다가 홈버튼 가는거 주소 이제 index로 넣어주기
=> {% url 'articles:index' %}
** 여기서 articles:index 뭔지 알지? = 앱네임:패스별명인거야 **
```



# 5. 게시물 작성페이지 만들기(new.html)

`ulrs.py`

```
path 작성하고 별명은 new로 지정하기
```

`views.py`

```
throw 과정에서 view 함수는 다른 설정이 필요없음 그냥 new 페이지 렌더하는것만 필요하니까
```

`new.html`

```
1. form 태그 사용해서 title + content 받아와야됨
	form 태그에 필요한 두가지 : action + method 인데 
	action은 지금 주소 연결하면 에러나니까 #으로 채워두고
	method는 GET으로 지정
	form 태그 안에서 이제 제목이랑 내용 받아올거임
	
2. 제목 받아오기
	label + input 태그 필요함
	label 태그에는 for 가 필요하고 여기에 title 지정해주기
	input 태그에는 name, id 필요하고 각각title 넣어주기

3. 내용 받아오기
	label + input 태그 필요함
	label 태그에는 for 가 필요하고 여기에 content 지정해주기
	input 태그에는 name, id 필요하고 각각 content 넣어주기
	
3.1. 내용받아오는건 input 태그 말고 textarea 태그를 사용해도됨
	textarea 태그에도 역시 name, id 필요하고 각각 content 넣어주기
	입력창 크기는 무난하게 cols="30" rows="10" 으로 지정하기
```



# 6. 게시물작성 확인페이지 만들기 (create.html)

#### 여기서 지금 구현해야되는 작업 2가지

```
a) new페이지에서 받은 데이터들 DB에 저장해주는 작업
	지금은 디테일페이지가 없으니까 데이터가 저장된건 index 페이지에서 확인할 수 있어
b) 정상적으로 데이터가 받아졌다는확인페이지를 띄우는 작업
```

a 작업은 view 함수에서 진행할거고
b 작업은 html이랑 view  함수에서 진행할거임

`ulrs.py`

```
path 써주고 별명은 create로 하기
```

`views.py`

```
new페이지에서 받은 데이터를 DB에 저장하는 작업을 해줘야됨
1. 일단 원래 함수 쓰듯이 적어줌 -> 페이지 렌더하기 위함
	def create(request):
		return render(request, 'articles/create.html')
		
2. "데이터 저장작업"을 함수 안에 써줘야됨 
	article = Article()
	article.title = title
    article.content = content
    article.save()
	그니까 지금 CRUD 중 create 작업을 진행한거임 (쉘에서 썼던 명령어 여기로 온거임)
```

`new.html`

```
여기는 그냥 base.html 로드하고 
블록 열어서 정상적으로 데이터가 저장됐다는 작업만 진행해주면 됨
```



# 7. 게시물 디테일페이지 만들기 (detail.html)

#### 여기서 지금 구현해야되는 작업:

이제 지금은 게시물중에서 "특정 게시물" 만의 내용을 가져와야되니까
고유키값을 사용해서 데이터를 그 고유키값이 가리키는 데이터만 가져오는 작업을 할거임

```
a) 고유키값은 view함수에서 request할때 사용자가 주소창에 번호를 적으면 variable routing으로 view 함수에서 두번째 파라미터에 받아올거임 (파라미터명을 여기서는 article_pk로 받음)

b) 그리고 데이터를 받아서 보여줘야되는거니까 이게 지금 catch 동작을 하는거지
	request에서 pk값의 데이터만 뽑아가지고 context 함수에 넣을거야
	
c) 이렇게 받아온 context 값을 html 페이지에서는 그 값중에서 title, content, 작성시간, 수정시간을 나눠서 보여주는 행동을 하게되는거임
```

`ulrs.py`

```
1. path를 써주는데 주소창에서 게시글번호를 받아야되니까 variable routing을 써주겠음
```

```
=> path('<int:article_pk>/', views.detail, name="detail")
```

`views.py`

```
1. 디테일 함수는 두번째 파라미터로 variable routing 값을 받아온거를 적어줌

2. 그렇게 하고 article변수 하나 만들어서  get메서드를 사용하는데 그 요소를
	pk값을 가진 데이터만 가져온다는 뜻으로 pk=article_pk로 적어줌
	이 의미가 지금 pk는 데이터 번호
	article_pk는 베리어블라우팅으로 가져온 번호
3. context 딕셔너리 키에는 article 변수를 넣어주기

4. 리턴값으로 역시 렌더함수를 써주고 마지막인자로 context값을 넣어주기
```

```
=> 이런식으로 쓰라는거임
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = { 'article':article }
    return render(request, 'articles/detail.html', context)
```

`new.html`

```
상세페이지는 각자 스타일로 만들기
이제 비추게 되는 데이터는 제목, 번호, 내용, 작성시각, 수정시각
```



# 8. 게시글 쓰면 가는 페이지 바꾸는 작업 구현

지금 원래는 게시글 쓰면 작성이 완료됐다는 확인페이지를 비추게 됐었는데

게시글 쓰면 바로 디테일 페이지로 가도록 하는 작업을 구현해볼거야

이때 redirect 기능이 필요함

`view.py`

```
1. import render옆에다가 redirect써주고

2. create 함수에 return 내용을 
return redirect('articles:detail', article.pk) 이걸로 바꿔주기만 하면 됨

이제 그러면 create.html 페이지는 쓸데가 없어진거임
```



# 9. 게시글 지우는 작업 구현하기

#### 9.1. 주소창에 게시글 번호/delete/ 를 작성해서 삭제하는 작업 만들기

`CRUD 중에서 D작업을 진행하게 되는거임`

이 작업은 `url path`와 `view` 함수만 있으며, html 파일은 당연히 없음

```
url path에는 detail path처럼 쓰면 되고 여기는 경로를 
'<variabe routing>/delete/' 이렇게 꼭 써주기 
```



`url.py`

```
1. 삭제할 게시글 번호를 주소창에 쓰고 /delete/ 적어서 삭제할 수 있도록 해야됨

=> path('<int:article_pk>/delete/', views.delete, name="delete"),
```

`views.py`

```
1. delete 함수를 선언하고 파라미터를 두개를 받아와야됨 왜냐면 삭제할 게시글 페이지가 필요하니까
	그래서 url에서도 variable routing으로 게시글 번호를 가져왔잖아
	두번째 파라미터를 베리어블라우팅으로 지정하고
	함수 내에 다음과 같이 쉘에서 DELETE 작업에 해당하는 명령어를 써주기

	article = Article.objects.get(pk=article_pk)
	article.delete()

2. 그리고 return값은 redirect 해서 index 페이지로 가도록 해주기

	return redirect('articles:index')
```



#### 9.2. 삭제한 페이지 번호를 다시 접근할 때 404 페이지 보내도록 하는 방법

`views.py`에서 detail 함수를 변경해야됨 !! 

```
1. 뷰파이 파일에서 import render, redirect옆에다가 get_object_or_404 임포트하기 

2. 디테일함수에서 article 변수 가져오는 메서드 바꾸기
=> article = get_object_or_404(Article, pk=article_pk)
```



# 10. 다음 단계로 넘어가기 전에: GET -> POST

#### GET 메서드를 POST 메서드로 바꾸기

`왜 그래야 되는지?`

```
get은 쿼리스트링이 주소창에 노출된다는 단점이 있거든
POST는 이걸 가려줘가지고 아이디 비밀번호같은 개인정보를 가려주면서 서버간에 주고받고 하는 기능이 있어
```



적용하는 방법은 간단함:

```
1. GET을 다 POST로 바꿔주고
	new.html
	views.py - create 함수
	
2. html 파일의 form 태그 안쪽에 csrf 토큰을 넣어주면 됨
```





# 11. 게시글 수정 페이지 만들기

#### 여기서 지금 구현해야되는 작업 2가지:

```
a) 게시글 생성 페이지와 동일한 폼 안에 `작성했었던 내용`이 들어가 있어야 됨
b) edit 페이지의 form 태그에서 action은 update페이지 , 즉 수정 이후의 페이지로 연결되어야 함
```



`urls.py`

```
1. 수정할 게시글 번호를 주소창에 쓰고 /edit/ 써서 해당 게시글의 수정 페이지로 갈 수 있도록 해야됨

=> path('<int:article_pk>/edit/', views.edit, name="edit"),
```

`views.py`

```
1. get object 404로 데이터 불러오고 
2. context 딕셔너리에 데이터를 담아서
3. edit.html 페이지에 값을 렌더하기
```

`edit.html`

```
1. new.html과 구성이 동일해야 하므로 new.html 페이지 내용 전체를 복사해오기
2. 바뀔 부분:
	1) form의 action부분 -> 이따가 수정된 페이지로 이동할 수 있도록 변경해야되는데 
		지금 만들지를 않았으니 #으로 잠깐 채워놓음
	2) input 태그에 속성 value를 추가해서 여기에 title 변수를 넣어놓기
	3) textarea 태그 사이에 content 변수 넣기
	
    =>
    1) <form action="#" method="POST">
    2) <input type="text" id="title" name="title" value="{{article.title}}">
    3) <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
```



# 12. 데이터 수정 완료 후 업데이트 페이지 만들기

#### 12.1. 페이지 만들기

`urls.py`

```
1. 수정된 게시글 번호로 연결된 해당 게시글의 디테일 페이지로 갈 수 있도록 해야됨

	path('<int:article_pk>/update/', views.update, name="update"),
```

`views.py`

```
1. get object 404로 데이터 불러오고 
	article = get_object_or_404(Article, pk=article_pk)
	
2. title 값, content 값을 POST 로 받은 다음

	title = request.POST.get('title')
    content = request.POST.get('content')

3. CRUD 과정중에서 U 과정을 진행해야됨 우리 쉘에서 썼던 명령어를 사용해야됨
	=> 지금 그러니까 수정될 내용은 1번으로 받아왔고
	=> 수정할 내용은 새롭게 2번에서 받아온거임
	=> 즉 ""수정될 내용 = 수정할 내용"" 이 구조라는거
	
    article.title = title
    article.content = content
    article.save()

4. 리턴값으로 redirect 함수 써서 디테일함수 호출되도록 함

	return redirect('articles:detail', article_pk)
```



#### 12.2. 페이지를 수정페이지와 연결하기

edit.html 페이지에서 아까 form 태그에 action #으로 비워놓은거

`{% url 'articles:update' article.pk %}`으로 변경해주기





# 13. 버튼으로 페이지들 연결하기 + 추가기능

#### 구현하려고 하는 기능들

```
1. index 페이지의 게시글 나열된거 누르면 디테일 페이지로 이동하는 기능
2. 디테일 페이지에서 수정버튼 만들기
3. 디테일 페이지에서 삭제버튼 만들기
4. 디테일 페이지에서 삭제버튼 누르면 모달폼 나타나서 한번더 물은 다음 삭제하는 기능
```



`1. index 페이지의 게시글 나열된거 누르면 디테일 페이지로 이동하는 기능 `

```
index.html에서 a태그 이용해서 {% url 'articles:detail' article.pk %} 로 주소 연결하기
```



`2. 디테일 페이지에서 수정버튼 만들기`

```
detail.html에서 a태그 이용해서 {% url 'articles:edit' article.pk %} 로 주소 연결하기
```



`3. 디테일 페이지에서 삭제버튼만듪기`

```
detail.html에서 a태그 이용해서 {% url 'articles:delete' article.pk %} 로 주소 연결하기
```



`4. 삭제버튼 누르면 모달폼 나타나서 한번더 물은 다음 삭제하는 기능`

```
```

