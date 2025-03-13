<template>
  <div
    class="min-h-screen w-full bg-cover bg-center bg-no-repeat flex flex-col justify-center items-center relative"
    style="background-image: url('/background.jpg');"
  >
    <!-- Overlay sombre -->
    <div class="absolute inset-0 bg-black opacity-40"></div>

    <!-- Contenu -->
    <div class="relative z-10 text-center text-white w-full px-4">
      <h1 class="text-4xl font-bold mb-6">Fashion Connect</h1>

      <!-- Barre de recherche -->
      <div class="flex items-center bg-white rounded-full shadow-lg max-w-2xl mx-auto overflow-hidden">
        <input
          v-model="searchQuery"
          @keyup.enter="searchProducts"
          type="text"
          placeholder="Search for clothes..."
          class="w-full px-6 py-3 text-gray-700 rounded-l-full focus:outline-none"
        />
        <button
          @click="searchProducts"
          class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-r-full"
        >
          🔍
        </button>
      </div>

      <!-- Résultats -->
      <div v-if="products.length > 0" class="mt-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div v-for="product in products" :key="product.title" class="bg-white p-4 rounded-lg shadow-lg">
          <img :src="product.image" alt="Product Image" class="w-full h-48 object-cover rounded-md mb-3" />
          <h3 class="font-semibold text-lg mb-2">{{ product.title }}</h3>
          <p class="text-gray-600">{{ product.price }}</p>
          <a :href="product.link" target="_blank" class="text-blue-600 hover:underline block mt-2">See on AliExpress</a>
        </div>
      </div>

      <!-- Message si rien trouvé -->
      <div v-if="products.length === 0 && searchDone" class="text-white mt-10 text-xl">
        No results found.
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const searchQuery = ref('');
const products = ref([]);
const searchDone = ref(false);

const searchProducts = async () => {
  if (!searchQuery.value.trim()) return;
  try {
    const response = await axios.get(
      `https://fashion-connect-backend.onrender.com/search?query=${encodeURIComponent(searchQuery.value)}`
    );
    products.value = response.data;
    searchDone.value = true;
  } catch (error) {
    console.error("Error fetching products:", error);
    searchDone.value = true;
  }
};
</script>
