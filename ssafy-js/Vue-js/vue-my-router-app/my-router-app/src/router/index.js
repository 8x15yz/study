import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LottoView from '../views/LottoView.vue'
import LunchView from '../views/LunchView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/LottoView',
    name: 'LottoView',
    component: LottoView
  },
  {
    path: '/LunchView',
    name: 'LunchView',
    component: LunchView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
