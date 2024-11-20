import { createRouter, createWebHistory } from 'vue-router'
import accountRoutes from './accounts'
import cardsRoutes from "@/router/cards.js";
import budgetRoutes from "@/router/budget.js";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    ...accountRoutes,
    ...cardsRoutes,
    ...budgetRoutes
  ]
})

export default router