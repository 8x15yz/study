<template>
  <div>
      <h2>VideoDetail</h2>
      <iframe id="ytplayer" type="text/html" width="640" height="360"
      :src="`https://www.youtube.com/embed/${selectedVideo.id.videoId}`"
      frameborder="0"></iframe>
      <h3>{{ selectedVideo.snippet.title }}</h3>
      <p>{{ selectedVideo.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  props: {
    selectedVideo: {
      type: Object,
      requeired: true
    }
  }
}
</script>

<style>

</style>