<template>
  <div>
      <TodoListItem 
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
      />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
export default {
    name: 'TodoList',
    components: {
        TodoListItem
    },
    computed: {
        todos() {
            return this.$store.state.todos
        }
    },

}
</script>

<style>

</style>