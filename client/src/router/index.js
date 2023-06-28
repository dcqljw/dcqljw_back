import {createRouter, createWebHashHistory} from 'vue-router'
import IndexView from '../views/IndexView.vue'
import FortuneTellerView from "@/views/FortuneTellerView.vue";

const routes = [
    {
        path: '/',
        name: 'index',
        component: IndexView
    }, {
        path: '/FortuneTeller',
        name: 'FortuneTellerView',
        component: FortuneTellerView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
    // mode: 'hash'
})

export default router
