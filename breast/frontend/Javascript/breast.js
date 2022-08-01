window.Vue = require('vue');
window.axios = require('axios');

import router from './router';
import App from './App.vue';

Vue.component('App', require('./App.vue'));

router.beforeEach((to, from, next) => {
    next();
})

new Vue({
	el : "#app",
	router,
	template: '<App/>',
    components: { App },
});
