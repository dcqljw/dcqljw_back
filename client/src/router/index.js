import {createRouter, createWebHashHistory} from 'vue-router'
import IndexView from '../views/IndexView.vue'
import HotTopView from "@/views/HotTopView.vue";
import LearnGroupView from "@/views/LearnGroupView.vue";
import AccountView from "@/views/AccountView.vue";
import GroupDetailView from "@/views/GroupDetailView.vue";
import GroupIndexView from "@/views/GroupViews/IndexView.vue";
import GroupDocumentView from "@/views/GroupViews/DocumentView.vue";
import GroupCalendarView from "@/views/GroupViews/CalendarView.vue";
import GroupTodoView from "@/views/GroupViews/TodoView.vue";
import GroupChatView from "@/views/GroupViews/ChatView.vue";
import GroupNoteView from "@/views/GroupViews/NoteView.vue"
import CreateGroupView from "@/views/CreateGroupView.vue";


const routes = [
    {
        path: '/',
        name: 'index',
        component: IndexView
    }, {
        path: "/hot_top",
        name: "HotTop",
        component: HotTopView
    }, {
        path: "/learn_group",
        name: "LearnGroup",
        component: LearnGroupView
    }, {
        path: "/account",
        name: "Account",
        component: AccountView
    }, {
        path: "/group_detail/:id",
        name: "GroupDetailView",
        component: GroupDetailView,
        children: [
            {
                path: "groupIndex",
                name: "groupIndex",
                component: GroupIndexView
            }, {
                path: "document",
                name: "document",
                component: GroupDocumentView
            }, {
                path: "todo",
                name: "todo",
                component: GroupTodoView
            }, {
                path: "calendar",
                name: "calendar",
                component: GroupCalendarView
            }, {
                path: "chat",
                name: "chat",
                component: GroupChatView
            }, {
                path: "note",
                name: "note",
                component: GroupNoteView
            }
        ]
    }, {
        path: "/create_group",
        name: "create_group",
        component: CreateGroupView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
    // mode: 'hash'
})

export default router
