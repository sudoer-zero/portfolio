import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import './index.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000';

createApp(App).use(router, VueAxios, axios).mount('#app')
