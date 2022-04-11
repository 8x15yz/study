# [프로젝트 결과 사진](img.md)

# 만든 기능

1. CRUD 기능
2. 이미지 파일 받기 + 업로드 기능

# 0. 목차

1. 환경 초기구성
2. Model 구성하기
3. ModelForm 구성하기
4. create 페이지 만들기
5. detail 페이지 만들기
6. update 페이지 만들기
7. delete 구현하기
8. bootstrap 적용하기
8. 스틸컷 게시하기
9. 어려웠던 부분 + 오류났던 부분

# 1. 환경 초기구성

#### 1.1. 가상환경 생성

1. pyvenv + 가상환경 activate 하기
2. pip install django + pip install django_extensions
3. django-admin startproject pjt06 .
4. python manage.py startapp movies
5. settings.py에 앱+익스텐션 등록하기

#### 1.2. 디렉토리 구성하기

6. templates를 pjt 디렉토리 내에 넣기 => settings.py에 디렉토리 작성하는데

 이번에는 `BASE_DIR / 'pjt06' / 'templates'` 이렇게 settings에 작성

7. base.html 만들기

8. movies디렉토리에 templates/movies생성하기

#### 1.3. urls.py를 앱과 연결하기

9. `pjt06/ urls.py` => include 모듈 임포트 + path 에 앱 이름 써주고 `include('앱이름.urls')`

10. articles 앱에 urls.py 만들고 + 모듈이랑 urlpatterns 구성하기 + `(중요) 앱네임써주기`

#### 1.4. index 페이지 만들어놓고 잘 동작하나 확인

urls.py

```
path 작성하고 별명도 설정해주기
```

views.py

```
함수 만들어서 index 페이지 렌더해주고 + 게시글을 나오게 할 수 있도록 정보 받아오는것까지 만들어놓기
1. from .models import Movie 모듈 불러오기
2. 함수를 선언해주고 + 여기는 입력 파라미터가 하나밖에 없음 => request
3. movies 변수 생성해서 Movie 모듈을 통해 정보를 받아오기 => orderby로 받아오기
4. context에다가 값을 넣고
5. return render 끝에 context를 같이 보내기
```

11. movies/admin.py 파일에 Movie 객체가 관리자 인터페이스를 가진다는 것을 알리기

    ```
    python manage.py createsuperuser
    ```

# 2. Model 구성하기

1. models.py에 Movies 클래스 만들고 정보 저장해주기

   ```
   title : CharField          # 영화 제목
   audiance : IntegerField    # 관객 수
   release_date : DateField   # 개봉일
   genre : CharField          # 장르
   score : FloatField         # 평점
   poster_url : TextField     # 포스터 경로
   description : TextField    # 줄거리
   ```

2. str 함수 작성해서 admin 페이지에서 데이터를 볼 때 알아볼수있도록 설정하기

3. python manage.py makemigrations + migrate 적용하기

# 3. ModelForm 구성하기

1. movies/forms.py 만들기

2. movies/forms.py 에서 .models 임포트해서 Movie 모듈 임포트해주기

3. 클래스 이름은  MovieForm => 안으로 Meta 클래서 만들어서 데이터 field 정보를 form에 적용하기 위해 model = Movie 작성하기

4. 필드 속성 설정하기

   ```
   메타 클래스 바깥에 작성하기
   1. 장르: genre_choices 리스트를 만들고 genre 변수에 forms.ChoiceField() 지정해서 choices = genre_choices, widget=forms.Select() 넣기
   2. 스코어: score 변수에 forms.FloatField() 지정해서 step, max, min 속성값을 atter 딕셔너리에 넣어주기
   ```

# 4. create 페이지 만들기

#### 4.1. create 부분에서 => new 작업먼저 구현하기

urls.py

```
path('', views.create) + 별명 설정
```

views.py => create 함수랑 아주 유사한것이 이따가 update 함수 만드는건데 비교하면서 적어보자

```
1. 이제는 create += new 니까 => 분기를 만들기 : request 하는 method가 POST 인지 아닌지로 if문을 생성해야됨
2. 여기서 지금 create 페이지를 먼저 만들어볼거니까 윗 분기는 pass 처리해놓고 else: 부터 채우기
3. else:는 정보를 받아오는게 아니라 정보를 적는 form 페이지를 렌더하는 작업을 해줘야되니까 new 함수에 적었던 작업을 써주기
4. 먼저 from 해가지고 폼 모듈 불러오기 MovieForm
5. 이때 우리는 이제 forms.py를 사용하니까 => form 변수를 만들어서 MovieForm()모듈에서 폼 형식을 받아오자 => 그리고 context 딕셔너리에다가 form 변수 넣어주고 렌더할때 같이 보내주기
```

create.html

```
1. 상속받아서 base 가져오고
2. views 함수에서 받아온 form 변수 적기
3. 조금 이제 형식을 갖추고 싶으면  => as_p 태그를 html의 form 변수에 적용해주기
```

#### 4.2. create 부분에서 => 정보 받아서 저장하는 작업 구현하기

views.py

```
1. 우리는 이제 메서드가 post일때의 작업을 구현해야됨 
	=> 데이터 POST로 받아오고
	=> isvalid로 유효성 검사를 진행한다음 
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
이때 어쨌든 context를 return을 해야돼서 => 동일한 레벨에 context + return을 적어주게 되는 것
```



# 5. detail 페이지 만들기

urls.py

```
variable routing으로 웹페이지 받아와야됨
path('<int:movie_pk>/', views.detail, name="detail"),
```

views.py

```
1. variable routing으로 값 받아왔으니까 함수 두번째 입력 파라미터 만들어주기
2. 여기서는 이제 request에서 variable routing으로 받아온 번호의 데이터를 return 해야되니까
	movies 변수에 request에서 가져오는 값을 저장해주고 (여기서 받아오는 메서드는 get object or 404니까 모듈도 동시에 임포트를 해주기)
	context에 담은 다음에
	return해주는 작업이 필요함 => 여기는 페이지+context를 렌더해줄것임
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
path를 '<int:movie_pk>/update/'으로 적어주기 + 별명 지정해주기
```

views.py

```
여기도 create와 동일하게 분기를 만들어줘야됨
else: 먼저 만들어주기
1. movie 변수에 get object or 404로 내용 받아오고 (Movie, pk=movie_pk)
2. form 변수를 생성해서 메서드를 통해 폼데이터도 받아오기 : 이때 instance를 movie로 받아오기(instance=movie)
3. 요거를 이제 context에 받아서 다같이 렌더해주기
```

update.html => 여거는 지금 create.html 으로 같이 공유하는거임

이렇게 하고 detail에서 수정버튼 연결하자

#### 6.2. update 부분에서 => update 작업 구현하기

views.py

```
데이터를 수정을 완료하고 이제 save() 해야되는 부분이니까 article 변수에 데이터를 받아오고 폼도 받아오고 요거를 이제 유효성검사를 진행한다음에 
디테일주소를 리디렉트하도록 작성해줘애됨 => 그러니까 지금 create랑 완전 똑같은데 여기서 인스턴스를 받아와야된다는 것 정도가 추가된것임
article = get_object_or_404(Movie, pk=article_pk)
form = MovieForm(request.POST, instance=movies)
```



# 7. delete 구현하기

urls.py

```
update랑 완전 구조 똑같게 path 쓰면 됨 
```

views.py

```
여기도 베리어블 라우팅으로 데이터 번호를 받아오고 있는 모습이니까 => 입력 파라미터가 두개
1. 정보를 get object 404로 받아오고 
2. method가 post인 경우에만 데이터를 삭제하도록 함 + index 페이지 리디렉트
3. 그게 아닌경우 디테일페이지 리디렉트
```

detail.html

```
views.py 함수에서 이제 post 메서드인 경우에만 delete 작업을 진행한다고 했으니까 
삭제 버튼에 폼태그를 씌워주고 csrf 토큰을 작성해줘야됨
*****create나 update는 action 안써도 되는데 여기는 써줘야돼 
{% url 'movies:delete' movies.pk%}*****
```

##### +) 모달폼의 id, aria-labelledby, data-bs-target 값 지정

id : deleteModal

aria-labelledby : deleteModalLabel

data-bs-target : #deleteModal



# 8. bootstrap 적용하기

#### 8.1. forms.py

공통적인 필드 속성 설정:

1. label을 한글으로 보이게 하기 위해 라벨 태그에 직접 작성 ('title'을 '영화 제목' 으로 바꾸는 등 ..)
2. widget을 사용:
   1. class 속성에는 form-control 혹은 form-select로 지정하고 margin bottom을 3으로 설정
   2. placeholder 속성을 사용하여 데이터 형식 등을 어떻게 입력해야 될지를 명시함 (ex 개봉일의 형식은 yyyy-mm-dd 입니다 .. etc)
   3. style 속성에 max widh를 600px 로 고정함

#### 8.2.  html 파일 class 속성 공통적용사항

forms.py에서 지정해놓은 form 속성 바깥으로 카드를 씌워서 가운데로 정렬할 수 있도록:

1. 맨 바깥에는 container h-100 를 적용하고 
2. 안쪽에는 row d-flex justify-content-center align-items-center h-100 를 적용하였음

#### 8.3. detail.html 삭제 동작

삭제버튼을 누르면 새로운 창이 뜨게 하여 삭제여부를 한번 더 묻도록 하였음





# 9. 스틸컷 게시하기

Media files를 받고 + detail 페이지에서 스틸컷 버튼을 누르면 모달폼이 나타나는 기능

#### 9.1. 이미지 파일 받아오기

[Media files 작업 자세히 작성](9_Media_files.md)

#### 9.2. 이미지 파일 게시 => modal form으로 게시





# 10. 어려웠던 부분 + 오류났던 부분

1. no such table 오류

   ```
   create 작업을 마치고 데이터를 생성해봤는데 생긴 오류이다
   해결 => makemigrations + migrate 했더니 해결됨
   ```