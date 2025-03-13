<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100 p-6">
    <!-- Titre du site -->
    <h1 class="text-5xl font-bold mb-8 text-gray-800">Fashion Connect</h1>

    <!-- Barre de recherche -->
    <div class="flex justify-center mb-10 w-full max-w-2xl">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search products..."
        class="w-full px-4 py-3 rounded-l-full focus:outline-none text-gray-700 border border-gray-300"
      />
      <button
        @click="searchProducts"
        class="bg-blue-600 text-white px-6 py-3 rounded-r-full hover:bg-blue-700"
      >
        Search
      </button>
    </div>

    <!-- Résultats -->
    <div v-if="products.length > 0" class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-6xl">
      <div
        v-for="product in products"
        :key="product.product_id"
        class="bg-white rounded-lg overflow-hidden shadow-md"
      >
        <img
          :src="product.product_main_image_url"
          alt="product"
          class="w-full h-64 object-cover"
        />
        <div class="p-4">
          <h3 class="font-bold text-lg truncate">{{ product.product_title }}</h3>
          <p class="text-gray-600">{{ product.app_sale_price }}</p>
          <a
            :href="product.product_detail_url"
            target="_blank"
            class="text-blue-600 hover:underline block mt-2"
          >
            View on AliExpress
          </a>
        </div>
      </div>
    </div>

    <!-- Message si pas de produit -->
    <div v-else-if="searched" class="text-gray-600 mt-10">
      No products found. Try another search.
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Déclaration des variables réactives
const searchQuery = ref('');
const products = ref([]);
const searched = ref(false);

// Fonction pour faire la recherche
const searchProducts = async () => {
  if (!searchQuery.value.trim()) return;
  try {
    const response = await axios.get('https://fashion-connect-backend.onrender.com/search', {
      params: { query: searchQuery.value }
    });
    console.log(response.data); // Pour vérifier les données
    products.value = response.data;
    searched.value = true;
  } catch (error) {
    console.error('Erreur de recherche :', error);
    products.value = [];
    searched.value = true;
  }
};
</script>
