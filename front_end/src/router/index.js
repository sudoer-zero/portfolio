import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Logo from '../views/Logo.vue'
import Blog from '../views/Blog.vue'
import Work from '../views/Work.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/logo',
    name: 'logo',
    component: Logo
  },
  {
    path: '/blog',
    name: 'blog',
    component: Blog
  },
  {
    path: '/work',
    name: 'work',
    component: Work
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
