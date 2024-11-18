const cardsRoutes = [
    {
        path: '/cards/',
        name: 'CardList',
        component: () => import('@/views/cards/CardView.vue')
    },

]

export default cardsRoutes