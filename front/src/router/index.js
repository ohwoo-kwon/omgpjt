import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import OMG from '../views/OMG.vue'
import Members from '../views/Members.vue'
import Albums from '../views/Albums.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/OMG',
    name: 'OMG',
    component: OMG
  },
  {
    path: '/members',
    name: 'Members',
    component: Members
  },
  {
    path: '/albums',
    name: 'Albums',
    component: Albums
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
