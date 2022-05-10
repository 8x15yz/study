<template>
  <div>
      <h2>videoList</h2>
      <!-- {{ videos }} -->
      <VideoListItem 
          v-for="video in videos"
          :key="video.id.videoId"
          :video="video"
          @set-selected-video="setSelectedVideo"/>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  components: {
    VideoListItem
  },
  props: {
    videos: {
      type: Array,
      required: true
    }
  },
  methods: {
    setSelectedVideo(newSelectedVideo) {
      this.$emit('set-selected-video', newSelectedVideo)
      console.log('여기도 됐는디')
    }
  }
}
</script>

<style>

</style>