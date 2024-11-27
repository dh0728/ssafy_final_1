const accountsRoutes = [
    {
        path: '/accounts/login',
        name: 'Login',
        component: () => import('@/views/accounts/LoginView.vue')
    },
    {
        path: '/accounts/registration',
        name: 'Registration',
        component: () => import('@/views/accounts/RegistrationView.vue')
    },
    {
        path: '/accounts/profile',
        name: 'UpdateProfile',
        component: () => import('@/views/accounts/UpdateProfileView.vue')
    }
]

export default accountsRoutes