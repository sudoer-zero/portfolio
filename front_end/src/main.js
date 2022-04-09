import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import './index.css'
import Markdown from 'vue3-markdown-it';
import 'highlight.js/styles/monokai.css';

axios.defaults.baseURL = 'https://sudoer.pythonanywhere.com/';


createApp(App).use(router, VueAxios, axios, Markdown).mount('#app')
