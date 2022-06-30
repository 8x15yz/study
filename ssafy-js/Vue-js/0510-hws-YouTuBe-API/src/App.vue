<template>
  <div id="app">
    <h2>my first youtube app</h2>
    <!-- <p>이걸 검색한게 맞나요 {{ inputValue }}</p> -->
    <TheSerchBar 
    @set-input-value="setInputValue"/>
    <VideoDetail 
    v-if="selectedVideo"
    :selectedVideo="selectedVideo"/>
    <VideoList 
    :videos="videos"
    @set-selected-video="setSelectedVideo"
    />
  </div>
</template>

<script>
import axios from 'axios'
 
import TheSerchBar from '@/components/TheSerchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'

export default {
  name: 'App',
  components: {
    TheSerchBar,
    VideoDetail,
    VideoList
  },
  data() {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    setInputValue(newValue) {
      this.inputValue = newValue

      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const config = {
        params : {
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue 
        }
      }
      axios.get(API_URL, config)
        .then(response => {
          this.videos = response.data.items
        })
    },
    setSelectedVideo(newSelectedVideo) {
      this.selectedVideo = newSelectedVideo
      console.log('여기가 안됐나??')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
