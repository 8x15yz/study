<template>
  <li @click="setSelectedVideo">
    <img :src="video.snippet.thumbnails.default.url" >
      {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  props: {
      video: {
        type: Object,
        required: true
      }
  },
  methods: {
    setSelectedVideo() {
      this.$emit('set-selected-video', this.video)
      console.log('여긴 됨')
    }
  }
}
</script>

<style>

</style>