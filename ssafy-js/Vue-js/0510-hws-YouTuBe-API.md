# workshop-03

## Project setup

```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

<br>

# 과정?

1.  사용하는 vue + extra file 
2.  초기 작업
3.  App.vue 초기 작업
4. 1. TheSearchBar에서 App으로 emit 보내기
   2.  App.vue에서 emit으로 보낸 데이터 받기
5.  request로 받아온 videos 데이터를 prop으로 VideoList 컴포넌트에 보내기
6.  VideosList.vue에서 하위 컴포넌트 등록하기
7.  videos array를 videosListItem으로 prop해서 보내기
8.  Item 하나 클릭하면 VideoDetail에서 플레이어가 나오도록 해야됨
    1.  `videoListItem.vue ` => `videoList.vue ` => `App.vue` (emit)
    2.  `App.vue` =>  `videoDetail.vue `  (prop)

9.  ``

<tr>

## 1. 사용하는 vue + extra file

```
workshop03
	|..... components
	|			|..... TheSearchBar.vue
	|			|..... VideoDetail.vue
	|			|..... VideoList.vue
	|			|..... VideoListItem.vue
	|
	|..... App.vue
	|..... .env.local
```

이대로 파일 구성하기

<br>

## 2. 초기 작업

1. App.vue에서 script 태그 안에 컴포넌트 임포트하기 ( `TheSearchBar` / `VideoDetail` / `VideoList`)
2. 각 앱의 template 태그 안에 제목 넣기 (TheSearchBar.vue에는 input 태그 넣기)

<br>

## 3. App.vue 초기 작업

1. axios 가져오기 ( `npm i axios` / `import axios from 'axios'` )
2. scripts 태그 부분에 쓴 요소 4개: ( `name` / `components` / `data()` / `methods`  )
   1. name : 기본설정으로 그냥 두기
   2. components : 하위 컴포넌트들 등록하는 곳
   3. data() : 3개 데이터  ( `inputValue` / `videos` / `selectedVideo` )
      1. `inputValue` : 이따가 TheSearchBar에서 emit으로 받아오는 데이터 저장하는 곳
      2. `videos` : VideoList에서 역시 emit으로 받아오는 데이터 넣어두는 곳
      3. `selectedVideo` : 이따가 설명
   4. methods : 2개 함수 ( `setInputValue` / `setSelectedVideo` )
      1. setInputValue : get 으로 api에서 데이터 받아오는 함수
      2. setSelectedVideo : video detail 에서 emit으로 받는 함수

<br>

## 4-1. TheSearchBar에서 App으로 emit 보내기

#### 지금 하려는 일 : imput 태그 안에서 받은 문자열 (event.target.vlaue)을 상위 컴포넌트로 보내서 -> App.vue에서 API로 get요청 보낼 때 config에 필요한 키워드에 문자열을 할당해야됨

1. inupt 태그 안에 엔터키 누르면 search 함수 실행되도록 하는 코드 작성 (@keyup.enter="search")
1. script 부분에 method 안에 search 함수 만들고 emit으로 App에 emit 키워드와 함께 `event.target.vlaue` 보내기

<br>

## 4-2. App.vue에서 emit으로 보낸 데이터 받기

template에서 `<TheSearchBar />`태그 쓴 부분에 emit 키워드 를 @로 불러오고  이게 이제 App.vue의 methods에 함수 중 `setInputValue`함수와 연결됨

#### setInputValue 함수 :

- this의 input parameter( `newValue` )를 this의 `InputValue`에다가 할당하고 
- 유튜브 API에서 데이터 요청하기 위해 config  상수 중 파라미터 p에 또 그 `InputValue`를 할당해줌
- axios로 get요청 보내기 => 요청으로 받은 데이터를 videos에 할당

#### 이렇게 하고 InputValue랑 videos 잘 받아왔는지 console.log로 확인해보기

<br>

## 5. request로 받아온 videos 데이터를 prop으로 VideoList 컴포넌트에 보내기

1. App.vue의 template 부분에 `<VideoList />` 태그에다가 Dynamic props로 바인딩하기 => `:videos="videos"`
2. videosList.vue에서도  scripts 부분에 `props: {}` 만들어서 수신하는 데이터를 선언해주기 

<br>

## 6. VideosList.vue에서 하위 컴포넌트 등록하기

#### 지금 하려고 하는것: 받아온 videos 리스트를 VideoListItem 컴포넌트로 또 보내려고 하는 중

1. templates에서 `<VideoListItem />` 태그 만들고
2. scripts 태그 안에서 VideoListItem  컴포넌트 import 하고 경로도 적기

<br>

## 7. videos array를 videosListItem으로 prop해서 보내기

1. videosList 컴포넌트에서  `<VideoListItem />`  태그에다가 이제 prop하기 위한 코드를 적어야 되는데 : 

   배열에서 하나씩 꺼내서 바인딩 하기 ?? => 문법을 다시 보기

2. 그리고  VideoListItem  컴포넌트로 넘어가서 scipts 안에 props 써서 선언하기

3. 그리고 template 태그 안에 li 태그 만들고 변수 만들어서 데이터 넣어주기 ( `video.snippet.title` )

4. 이미지 태그도 만들어서 src에 썸네일 url 넣어주기 ( `video.snippet.thumbnails.default.url` )

<br>

## 여기까지 한거:

![](./record_img_dir/02.png)

<br>

## 8. Item 하나 클릭하면 VideoDetail에서 플레이어가 나오도록 해야됨

그러면 다음과 같은 경로가 돼야돼:

![](./record_img_dir/03.jpg)

그니까 크게 두개를 해야돼

1. `videoListItem.vue ` => `videoList.vue ` => `App.vue` (emit)
2. `App.vue` =>  `videoDetail.vue `  (prop)

<br>

## 8-1 `videoListItem.vue ` => `videoList.vue ` => `App.vue` (emit)

1. videoListItem 에서 method 열고 안에다가 setSelectedVideo 함수 만들어서 emit하기 (이때 this의 video 객체(클릭한 객체)를 올려보내야됨)
2. videoList으로 넘어와서 `<videoListItem />`태그에서 @로 키워드와 함께 함수를 듣고, 여기서도 method에서 setSelectedVideo 함수 만듷어서 App.vue로 emit 올리기 (파라미터로 받은거 그대로 올리기)
3. App.vue로 넘어와서 `<videoList />` 태그에서 또 받고, 여기서도 methods에서 똑같이 함수를 setSelectedVideo 를 만드는데 이번에는 이제 데이터에다가 emit으로 받은 데이터를 지정해주는 코드를 쓰기(그래서 이 단계에서 data() 에다가  selectedVideo: null 만들어야됨)

#### 여기까지가 클릭하면 App으로 emit올리는 과정이 끝

<br>

## 8-2 `App.vue` =>  `videoDetail.vue `  (prop)

1. App.vue에서  `<videoDetail />` 태그 안에다가 prop 해주기 ( `:selected-video="selectedVideo"` )
2. videoDetail.vue 넘어가서 scripts에 props 열고 선언해t서 객체 받고 template에 잘 나오나 변수로 넣어보기
3. `selectedVideo.snippet` 에 제목 + 영상 소개 요소를 꺼내올 수 있음 (title, description)

#### cf) v-if="selectedVideo" 를 App.vue 에 VideoDetail에 안쓰면:

TypeError: Cannot read properties of null (reading 'snippet') 이런 에러가 남

<br>

## 9. VideoDetail 컴포넌트에서 비디오 플레이어 켜기

[참고 문서](https://developers.google.com/youtube/player_parameters)

위 문서에서 iframe태그를 가져오기 

그리고 src부분에서 비디오아이디 넣는 부분에 `selectedVideo.id.videoId` 넣기

