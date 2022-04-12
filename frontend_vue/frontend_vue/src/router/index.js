import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TokenView from '../views/TokenView.vue'
import UnsubscribeView from '../views/UnsubscribeView.vue'
import InfoCourseView from '../views/InfoCourseView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      title: 'Страница для списка курсов'
    }
  },
  {
    path: '/token',
    name: 'token',
    component: TokenView,
    meta:{
      title: 'Страница для просмотра своего токена авторизации'
    }
  },
  {
    path: '/unsubscribe',
    name: 'unsubscribe',
    component: UnsubscribeView,
    meta: {
      title: 'Возможность отписаться от курса'
    }
  },
  {
    path: '/info-course',
    name: 'info-course',
    component: InfoCourseView,
    meta:{
      title: 'Возможность просмотра информации по курсу, на который записан студент'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
