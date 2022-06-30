# 0502 pr : 댓글 API practice

# 0. 로직

1. DOM 구성하기
2. script 부분 구성하기
2. 추가 공부 : 댓글 삭제 기능 구현하기

# 1. DOM 구성하기

```html
<form>
    <input type="text" id="title">
    <input type="text" id="content">
    <button>제출</button>
</form>
<ul id="article-list"></ul>
```

1. form 태그로 input 요소 작성을 하는데

   input 태그를 두개를 만들어서  id를 title, content 두개로 하도록 함

2. ul 태그로 작성한 댓글이 나올 수 있도록 뿌리 심어놓기 + ul 태그에 id 작성하기

# 2. script 부분 구성하기

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
    const articleList = document.querySelector('#article-list')
    const API_URI = 'https://edutony.pythonanywhere.com/api/v1/articles/'

    const form = document.querySelector('form')

    form.addEventListener('submit', function (event) {

        event.preventDefault()
        axios.post(API_URI, {
            title: event.target.querySelector('#title').value,
            content: event.target.querySelector('#content').value
        })
    })

    axios.get(API_URI)
        .then(response => {
        response.data.forEach(article => {
            const articleItem = document.createElement('li')
            articleItem.innerText = `${article.id}. ${article.title} : ${article.content}`
            articleList.appendChild(articleItem)
        })
    })
</script>
```

### 2.1. axios 환경 구성

1. axios CDN 가져오기 : 

```html
 <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

2. script 따로 열어서 코드 작성해야됨 (cdn 있는 태그에 작성하면 안됨 왜그럴까 ?)
3. ul 태그, form 태그 가져오기 => querySelector으로 
4. API 지정하기 => https://edutony.pythonanywhere.com/api/v1/articles/

### 2.2. form에서 할 일 작성하기: input 태그에서 데이터 받고 post 로 보내기

1. form에서 할 일을 작성해줘야됨: `addEventListener 메서드` 활용하기

2. 일단 버튼 누르면 바로 발생하는 post 동작 막아주고 `event.preventDefault()`

3. post 동작으로 데이터 보내는 동작 추가해주기

   ```html
   axios.post(API_URI, {
   title: event.target.querySelector('#title').value,
   content: event.target.querySelector('#content').value
   })
   ```

   `event.target` = 이게 근본: form태그를 보여줌

   이제 저 객체에서 title과 content를 꺼내와야됨 => querySelector에서 id로 꺼내오기

   그렇게 하고 post 메서드 안에 data 쓰는 곳에다가 title, content 구분해서 써주기

   

### 2.3. ul에서 할 일 작성하기: 데이터 get으로 받아와서 페이지에 뿌리기

```html
<script>
    axios.get(API_URI)
        .then(response => {
        response.data.forEach(article => {
            const articleItem = document.createElement('li')
            articleItem.innerText = `${article.id}. ${article.title} :${article.content}`
            articleList.appendChild(articleItem)
        })
    })
</script>
```

1. axios 에서 get으로  api를 가져오고 promise로 다음 작업을 지정하기

2. response에서 data를 꺼내고  

3. data에 대해서 foreach로 각각의 데이터에 대해 다음의 작업을 적용하기

   1. li 태그 생성해서 상수에 할당하고

   2. li상수에 내용 담고

   3. 위에서 받아온 

      ```
       const articleList = document.querySelector('#article-list')
      ```

      이 상수에 appendChild 하기

# 3. 댓글 삭제기능 만들기