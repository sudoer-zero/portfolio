import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Logo from '../views/Logo.vue'
import Blog from '../views/Blog.vue'
import Work from '../views/Work.vue'
import ArticleDetail from '../views/ArticleDetail'

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
  {
    path: '/:article_slug',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
