import Vue from 'vue';
import Router from 'vue-router';

// Views
import Form from '../views/Form';


Vue.use(Router);

export default new Router({
  mode: 'hash', // hash or hash = Demo is living in GitHub.io, so required!
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
      {
      path: '/',
      name: 'Home',
      component: Form
    },
    
  ]
});
