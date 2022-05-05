/* 
  아래에 코드를 작성해주세요.
*/
// https://jae04099.tistory.com/78
// Application name	studyAPI
// API key	2041030889063485929e18e914ce4bed
// Shared secret	a09a8043ce8f40b5d7949c20865336ee
// Registered to	jay0815_jay



// const keyword = document.querySelector('.search-box__input')
// console.log(keyword)

const searchBtn = document.querySelector('.search-box__button')

searchBtn.addEventListener('click', function fetchAlbums (event, page=1, limit=10) {
  const keyword = document.querySelector('.search-box__input').value
  const URI_API = `http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&api_key=2041030889063485929e18e914ce4bed&format=json`
  axios.get(URI_API)
    .then(respose => {
      console.log(respose.data.results.albummatches.album)
      const albums = respose.data.results.albummatches.album
      const searchResult = document.querySelector('.search-result')
      
      for (const album of albums) {
        const divTag = document.createElement('div')
        // const imgDivTag = document.createElement('div')
        console.log(album)
        
        const img = album.image.find(elem => {
          return elem.size ==='small'
        })
        divTag.innerText = `${album.name} ${img.size}`
        searchResult.append(divTag)
      }
    })
    .catch(error => alert('잠시 후 다시 시도해주세요'));
})
