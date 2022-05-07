import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import vuetify from './plugins/vuetify'
import VueShowdown from 'vue-showdown'
import axios from 'axios'

// axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.baseURL = 'https://sudoer.pythonanywhere.com/';
Vue.config.productionTip = false

Vue.use(VueShowdown, {
  // set default flavor of showdown
  flavor: 'original',
  // set default options of showdown (will override the flavor options)
  options: {
    emoji: true,
  },
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
