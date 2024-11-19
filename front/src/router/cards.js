const cardsRoutes = [
    {
        path: '/cards/',
        name: 'CardList',
        component: () => import('@/views/cards/CardView.vue')
    },
    {
        path: '/cards/detail/:card_id',
        name: 'CardDetail',
        component: () => import('@/components/cards/CardDetail.vue')
    },
]

export default cardsRoutes