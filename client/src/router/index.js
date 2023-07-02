import {createRouter, createWebHashHistory} from 'vue-router'
import IndexView from '../views/IndexView.vue'
import FortuneTellerView from "@/views/FortuneTellerView.vue";
import HotTopView from "@/views/HotTopView.vue";
import DemoView from "@/views/DemoView.vue";

const routes = [
    {
        path: '/',
        name: 'index',
        component: IndexView
    }, {
        path: '/FortuneTeller',
        name: 'FortuneTellerView',
        component: FortuneTellerView
    }, {
        path: "/hot_top",
        name: "HotTop",
        component: HotTopView
    }, {
        path: "/demo",
        name: "demo",
        component: DemoView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
    // mode: 'hash'
})

export default router
