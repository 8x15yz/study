import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {title: '점심 먹기', isCompleted: false, date: new Date().getTime()},
      {title: '복습하기', isCompleted: false, date: new Date().getTime()},
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state) {
      state.todos.push({ title:1, isCompleted: true, date: 'asdf'})
    }
  },
  actions: {
    createTodo({ commit }) {
      commit('CREATE_TODO')
    }
  },
  modules: {
  }
})
