import { createRouter, createWebHistory } from 'vue-router';

// Import uniquement la page Search (page vitrine publique)
import Search from '../pages/Search.vue';

// Définition des routes
const routes = [
  {
    path: '/',
    name: 'Search',
    component: Search, // Page d'accueil = Search
  },
];

// Création du routeur
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
