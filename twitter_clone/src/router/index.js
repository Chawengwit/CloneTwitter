import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import User from '../views/User.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/:name',  //dinamic routing
    props:true,
    name: 'User',
    component: User

  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
