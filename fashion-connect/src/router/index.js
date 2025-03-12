import { createRouter, createWebHistory } from 'vue-router';
import Login from '../pages/Login.vue';
import Admin from '../pages/Admin.vue';
import Search from '../pages/Search.vue'; // ✅ Page publique

const routes = [
  { path: '/', component: Search },    // ✅ Page publique
  { path: '/admin', component: Admin }, // Admin
  { path: '/login', component: Login }  // Login
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
