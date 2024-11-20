const budgetRoutes = [
    {
        path: '/main/',
        name: 'Main',
        component: () => import('@/views/budget/CalendarView.vue')
    }
]

export default budgetRoutes