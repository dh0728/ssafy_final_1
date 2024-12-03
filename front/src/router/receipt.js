const receiptRoutes = [
    {
        path: '/receipt/',
        name: 'Receipt',
        component: () => import('@/views/receipt/ReceiptView.vue')
    },
    {
        path: '/receipt/result',
        name: 'ResultReceipt',
        component: () => import('@/views/receipt/ResultReceiptView.vue')
    },
    {
        path: '/receipt/loading',
        name: 'LoadingReceipt',
        component: () => import('@/views/receipt/ReceiptLoadingView.vue')
    }
]

export default receiptRoutes