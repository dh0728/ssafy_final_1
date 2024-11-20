const budgetRoutes = [
    {
        path: '/main/',
        name: 'Main',
        component: () => import('@/views/budget/BudgetView.vue'),
        children: [
            {
                path: 'calendar',
                component: () => import('@/views/budget/CalendarView.vue')
            },
        ]
    }
]

export default budgetRoutes