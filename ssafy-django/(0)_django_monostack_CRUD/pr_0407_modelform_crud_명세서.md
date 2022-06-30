# 0. 목차

1. 환경 초기화
2. 모델 구성해주기
3. ModelForm 구성하기
4. create 페이지 만들기
5. detail 페이지 만들기
6. update 페이지 만들기
7. delete 구현하기

# 1. 환경 초기화

#### 1.1. 가상환경 생성

1. pyvenv + 가상환경 activate 하기
2. pip install django + pip install django_extends 
3. django-admin startproject config . 
4. python manage.py startapp articles
5. settings.py에 앱+익스텐션 등록하기

#### 1.2. 디렉토리 구성하기

6. 이번에는 templates를 pjt 디렉토리 내에 넣기 => settings.py에 디렉토리 작성

​		이번에는 `BASE_DIR / 'config' / 'templates'` 이렇게 settings에 작성해야겠지

6. base.html 만들기
7. articles 디렉토리에 templates/articles 생성하기

#### 1.3. urls.py를 앱과 연결하기

8. `config / urls.py` => include  모듈 임포트 + path 에 앱 이름 써주고 `include('앱이름.urls')`
9. articles  앱에 urls.py 만들고 + 모듈이랑 urlpatterns 구성하기 + `(중요) 앱네임써주기`

#### 1.4. index 페이지 만들어놓고 잘 굴러가나 확인

urls.py 

```
path('', views.index) 하고 별명도 설정해주고
```

views.py

```
함수 만들어서 index 페이지 렌더해주기 => 인데 이제 우리는 여기서 미리 게시글을 나오게 할 수 있도록 
"정보 받아오는것까지 세팅을 해줘야됨"
1. from .models import Article 모듈 불러오기
2. 함수를 선언해주고 + 일단 여기는 입력 파라미터가 하나밖에 없음 => request
3. 일단 articles 변수 생성해서 Article 모듈을 통해 정보를 받아오기 => orderby로 받아올거임
4. context 딕셔너리에다가 값을 넣어주고 
5. return render 끝에 context를 같이 렌더시키기
```

index.html

```
1. base.html 상속받고 적절히 제목이랑 그런거 써주기
2. 게시글 보여주는 작업 작성하기 => for 태그 만들어가지고 
```



# 2. 모델 구성해주기

1. models.py에 기본 구성 코드 작성하기 => 이거는 이제 좀 외우자 ..

   ```
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return f'{self.pk} - {self.title}'
   ```

2. python manage.py makemigrations + migrate 적용하기

# 3. ModelForm 구성하기

1. articles/forms.py  만들고 + 가서 modelform 코드 구성하기 => forms는 변경해도 뭐 등록할건 딱히 없음

   ```
   from django import forms
   from .models import Article
   
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields = '__all__'
   ```

# 4. create 페이지 만들기

#### 4.1. create 부분에서 => new 작업먼저 구현하기

urls.py 

```
path('', views.create) + 별명 설정
```

views.py  => create 함수랑 아주 유사한것이 이따가 update 함수 만드는건데 비교하면서 적어보자

```
1. 이제는 create += new 니까 => 냅다 분기먼저 만들어야 되는거임
	request 하는 method가 지금 POST 인지 아닌지로 if문을 생성해야됨
2. 여기서 지금 create 페이지를 먼저 만들어볼거니까 윗 분기는 pass 처리해놓고 else: 부터 채우기
3. else:는 정보를 받아오는게 아니라 정보를 적는 form 페이지를 렌더하는 작업을 해줘야되니까 new 함수에 적었던 작업을 써주기
4. 이때 우리는 이제 forms.py를 사용하니까 => form 변수를 만들어서 ArticleForm()모듈에서 폼 형식을 받아오자 => 그리고 context 딕셔너리에다가 form 변수 넣어주고 렌더할때 같이 보내주기
**** 이때 from 해가지고 폼 모듈 불러와야됨 ****
```

create.html

```
1. 상속받아서 base 가져오고
2. views 함수에서 받아온 form 변수를 페이지에 뿌리기
3. 조금 이제 형식을 갖추고 싶으면  => as_p 태그를 html의 form 변수에 적용해주기
```

#### 4.2. create 부분에서  => 정보 받아서 저장하는 작업 구현하기

views.py

```
1. 우리는 이제 메서드가 post일때의 작업을 구현해야됨 
	=> 데이터 POST로 받아오고
	=> isvalid로 유효성 검사를 진행한다음 (**여기도 분기가 생기는거야**)
	=> 데이터를 저장해주고 detail url을 리다이렉트해주는 작업을 하셔야됨
		근데 지금 일단은 detail 페이지 없으니까 index 페이지 리디렉션하기
```

create.html

```
1. form 태그 열어서 method POST로 적용해주고 변수를 태그 안에 넣어주기
2. csrf 토큰 필요 !!!!
3. 태그 안에 버튼도 넣기
```

#### +) 추가사항

```
views 함수에서 context 받아오는거 레벨을 if랑 동일하게 해줘야됨!!!!!!!! 이 이유는:
메서드는 post인데 이제 유효성검사를 했을때 False값이 나오면 if문 탈출하고 바로 return을 하는데 
이때 어쨌든 context를 return을 해야돼서 => 동일한 레벨에 context + return을 심어주게 되는 것
```



# 5. detail 페이지 만들기

urls.py

```
variable routing으로 웹페이지 받아와야됨
path('<int:article_pk>/', views.detail, name="detail"), => 외우자 ....... 
```

views.py

```
1. variable routing으로 값 받아왔으니까 함수 두번째 입력 파라미터 만들어주기
2. 여기서는 이제 request에서 variable routing으로 받아온 번호의 데이터를 return 해야되니까
	articles 변수에 request에서 가져오는 값을 저장해주고 (여기서 받아오는 메서드는 get object or 404니까 모듈도 동시에 임포트를 해주기)
	context에 담은 다음에
	return해주는 작업이 필요함
```

detail.html

```
여기서는 받은 정보를 html으로 보여주는 작업 + 삭제버튼 + 수정버튼 만들어야됨
근데 일단 다 만들어놓고 
삭제랑 수정버튼에 url은 아직 연결하지말고 #으로 채워놓기
```

# 6. update 페이지 만들기

#### 6.1. update 부분에서 => edit 페이지 먼저 구현하기

urls.py

```
path를 '<int:article_pk>/update/'으로 적어주기 + 별명 지정해주기
```

views.py

```
여기도 create와 동일하게 분기를 만들어줘야됨
else: 먼저 만들어주기 => 내용 받아오고 => (Article, pk=article_pk)
form 변수를 생성해서 메서드를 통해 폼데이터도 받아오기 : 이때 instance를 article으로 받아오기(instance=article)
요거를 이제 context에 받아서 다같이 렌더해주기
context 레벨을 if랑 이제 그냥 미리 동일하게 만들기 => 이유 아니까 바로 그냥 적용해주기
```

update.html  => 알지? 여거는 지금 create.html 공유하는거임

이렇게 하고 detail에서 수정버튼 연결하자

#### 6.2. update 부분에서 => update 작업 구현하기

views.py

```
데이터를 수정을 완료하고 이제 save() 해야되는 부분이니까 article 변수에 데이터를 받아오고 폼도 받아오고 요거를 이제 유효성검사를 진행한다음에 
디테일주소를 리디렉트하도록 작성해줘애됨 => 그러니까 지금 create랑 완전 똑같은데 여기서 인스턴스를 받아와야된다는 것 정도가 추가된것임
article = get_object_or_404(Article, pk=article_pk)
form = ArticleForm(request.POST, instance=article)
```

# 7. delete 구현하기

urls.py

```
update랑 완전 구조 똑같게 path 쓰면 됨 
```

views.py

```
여기도 베리어블 라우팅으로 데이터 번호는 받아오고 있는 모습이니까 => 입력 파라미터가 두개
1. 정보를 get object 404로 받아오고 
2. method가 post인 경우에만 데이터를 삭제하도록 함 + index 페이지 리디렉트
3. 그게 아닌경우 디테일페이지 리디렉트
```

detail.html

```
views.py 함수에서 이제 post 메서드인 경우에만 delete 작업을 진행한다고 했으니까 
삭제 버튼에 폼태그를 씌워주고 csrf 토큰을 작성해줘야됨
*****야 create나 update는 action 안써도 되는데 여기는 써줘야돼 
{% url 'articles:delete' article.pk%}*****
```





# 8. 나머지작업

1. 버튼들 이제 주석풀어주고 path 연결하기

