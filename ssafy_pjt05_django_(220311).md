# 1. 초기설정

## Model  초기 설정

```
1. requirments에 있는것들 다 설치
2. 프로젝트 만들고 앱 만들기
```

## Movies 디렉토리 초기 설정

```
1.앱의 모델 파일에다 Movie 클래스 만들어서 각각 7개 필드 만들어주기
(꼭 makemigrations랑 migrate 적용해줘여ㅑ됨 )

2. urls.py를 새로 만들어줌
3. Movies/templates/Movies의 경로로 템플릿 파일 저장할 디렉토리 만들어줌
```

## pjt05/url.py 작성하기

```
1. inclde를 임포트하여 Movies path에다가 Movies urls.py를 반영하도록 include 메서드를 적용해줌
```

## templates/base.html

```
1. 간단한 Navbar를 적용해주기 위해 부트스트랩CDN 사용함
2. block을 사용하여 앞으로 만들 템플릿 각각 내용이 담기도록 함

3. 셋팅에 템플릿 란에 BASE_DIR / 'templates' 적요ㅕㅇ
```

# 2. Movies app에서 진행

```
movies/admin.py 파일에 Movie 객체가 관리자 인터페이스를 가진다는 것을 알려야됨
```

## 전체 게시글 조회 페이지 만들기

```
1. Movies/urls.py 만들고
2. 현재 경로에서 views 모듈 불러오기
3. 앱네임을 movies로 적용
4. Movies/urls.py에 index 경로 만들기
5. Movies/views.py에 index 함수 만들기
```

## 게시글 생성 페이지 만들기('C'rud)

```
1. movies/url.py 파일에 새로운 게시물 작성 위한 path 생성
2. movies/url.py 파일에 새로운 create동작 위한 path 생성
3. movies/views.py 파일에 new 함수 생성 - new 템플릿 반환
4. movies/views.py 파일에 create 함수 생성 - new,html페이지에서 받아온 정보를 POST로 받아오고 CURD 중 C 진행:
변수 생성하고 변수.속성 = 가져온정보
...
변수.save()
create 함수는 게시글을 생성하고 바로 index 페이지로 가기 위해 redirect(새 url으로 요청을 보내서 그에 맞는 views 함수가 다시 실행되도록 함)
```

## 게시글 개별 조회 페이지 만들기(c'R'ud)

```
1. movies/url.py 파일에 상세 페이지 번호로 접근할 수 있도록 주소를 variable routing 을 사용함
2. movies/views.py detail 함수에서는 해당하는 페이지 번호가 없을 시 404페이지를 내보내도록 지정하였음
3. 템플릿에는 views에서 가져온 정보를 보일 수 있도록 작성하였음
```

## 게시글 삭제 동작 만들기(cru'D')

```
1. movies/url.py 작성
2. movies/views.py delete 함수 적용
3. detail page에 삭제버튼을 생성함 - 삭제의 경우 모달 폼을 내보내 한번 더 삭제여부를 묻는 동작을 추가함
```

## 게시글 수정 동작 만들기(cr'U'd)

```
1. movies/url.py 작성
2. movies/views.py edit 함수와 update함수 적용
```





## 어려웠던 점

```
수정 페이지를 작성할 때 날짜 영역에서 템플릿에 노출되는 그대로 값이 돌아왔기 때문에 그걸 잘 처리하지 않으면 에러가 났음 -> 보완할 방법을 좀 더 생각해봐야될 듯
=> 해결:
edit.html 페이지에 value ="{{movie.release_date}}" 를 value ="{{movie.release_date|date:'Y-m-d'}}"로 변경
```

