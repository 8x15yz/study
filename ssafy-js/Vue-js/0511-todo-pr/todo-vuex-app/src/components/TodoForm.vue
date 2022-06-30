<template>
  <div>
      form
      <input type="text">
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    created() {
        this.$store.dispatch('createTodo')
    }

}
</script>

<style>

</style>