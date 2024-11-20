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
        ]
    }
]

export default budgetRoutes