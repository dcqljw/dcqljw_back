import {createRouter, createWebHashHistory} from 'vue-router'
import IndexView from '../views/IndexView.vue'

const routes = [
    {
        path: '/',
        name: 'index',
        component: IndexView
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
    // mode: 'hash'
})

export default router
