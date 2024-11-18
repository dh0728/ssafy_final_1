import { createRouter, createWebHistory } from 'vue-router'
import accountRoutes from './accounts'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    ...accountRoutes
  ]
})

export default router