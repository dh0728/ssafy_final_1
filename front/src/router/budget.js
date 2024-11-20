const budgetRoutes = [
    {
        path: '/main/',
        name: 'Main',
        component: () => import('@/views/budget/BudgetView.vue'),
        children: [
            {
                path: 'calendar',
                component: () => import('@/components/budget/MonthlyBudget.vue')
            },
            {
                path: 'schedule',
                component: () => import('@/components/budget/Schedule.vue')
            },
            {
                path: 'budgetWrite',
                component: () => import('@/components/budget/BudgetWrite.vue')
            },
        ]
    }
]

export default budgetRoutes