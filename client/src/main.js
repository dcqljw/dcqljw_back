import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from "element-plus";
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import 'element-plus/theme-chalk/display.css'
import axios from "axios";

// axios.defaults.baseURL = "https://dcqljw.xyz:8000"
axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)
app.use(store).use(router).use(ElementPlus).mount('#app')

