<template>
  <input type="text" @keyup.enter="search">
</template>

<script>
export default {
  methods: {
    search(event) {
    this.$emit('set-input-value', event.target.value)
    console.log(event.target.value)
    }
  }
  
}
</script>

<style>

</style>