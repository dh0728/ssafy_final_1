const budgetRoutes = [
    {
        path: '/budget/',
        name: 'Budget',
        component: () => import('@/views/budget/BudgetView.vue'),
        children: [
            {
                path: 'calendar',
                component: () => import('@/components/budget/MonthlyBudget.vue')
            },
            {
                path: 'schedule',
                component: () => import('@/components/schedule/Schedule.vue')
            },
            {
                path: 'budgetWrite',
                component: () => import('@/components/budget/BudgetAdd.vue')
            },
        ]
    }
]

export default budgetRoutes