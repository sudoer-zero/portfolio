import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ThanksView from '../views/ThanksView'
import Fun from '../views/Fun'
import ArticlesList from '../views/blogs/ArticlesList'
import ArticleDetail from '../views/blogs/ArticleDetail'
import LogosList from '../views/logos/LogosList'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/thanks',
    name: 'Thanks',
    component: ThanksView
  },
  {
    path: '/fun',
    name: 'Fun',
    component: Fun
  },
  {
    path: '/:article_slug',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/blogs',
    name: 'blogs',
    component: ArticlesList
  },
  {
    path: '/logos',
    name: 'logos',
    component: LogosList
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
