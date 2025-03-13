<template>
  <div
    class="min-h-screen flex flex-col justify-center items-center relative"
    style="background-image: url('/background.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;"
  >
    <!-- Overlay sombre -->
    <div class="absolute inset-0 bg-black opacity-40"></div>

    <!-- Contenu centré -->
    <div class="relative z-10 text-center text-white px-4 w-full">
      <!-- Nom du site -->
      <h2 class="text-3xl md:text-4xl font-semibold mb-4 uppercase tracking-widest">
        Fashion Connect
      </h2>

      <!-- Titre de recherche -->
      <h1 class="text-5xl md:text-6xl font-bold mb-10">
        Search Engine
      </h1>

      <!-- Barre de recherche -->
      <div class="flex items-center bg-white rounded-full overflow-hidden w-full max-w-2xl mx-auto shadow-lg">
        <input
          v-model="searchQuery"
          @keyup.enter="searchProducts"
          type="text"
          placeholder="Search Clothes..."
          class="w-full px-6 py-3 text-gray-700 focus:outline-none"
        />
        <button
          @click="searchProducts"
          class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3"
        >
          🔍
        </button>
      </div>

      <p class="mt-6 text-lg italic">Search Clothes</p>
    </div>

    <!-- Affichage des produits -->
    <div class="relative z-10 w-full max-w-5xl mt-10 px-4" v-if="products.length > 0">
      <h3 class="text-2xl text-white mb-4">Search Results:</h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div v-for="product in products" :key="product.title" class="bg-white rounded-lg shadow-md p-4">
          <img :src="product.image" alt="Product image" class="w-full h-48 object-cover rounded-md mb-2" />
          <h4 class="font-semibold text-lg">{{ product.title }}</h4>
          <a
            :href="product.link"
            target="_blank"
            class="text-blue-600 hover:underline"
          >
            View Product
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Requête de recherche
const searchQuery = ref('');
const products = ref([]);

// Fonction pour rechercher les produits
const searchProducts = async () => {
  if (searchQuery.value.trim() === '') return;
  try {
    const response = await axios.get(
      `https://fashion-connect-backend.onrender.com/search?query=${encodeURIComponent(searchQuery.value)}`
    );
    products.value = response.data;
  } catch (error) {
    console.error('Search failed:', error);
  }
};
</script>
