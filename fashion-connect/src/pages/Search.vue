<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <!-- Fixed Background Container -->
    <div class="fixed inset-0 -z-10">
      <img
        src="/background.webp"
        alt="Background"
        class="w-full h-full object-cover object-center"
      />
      <div class="absolute inset-0 bg-black/60"></div>
    </div>

    <!-- Content Container -->
    <div class="flex-1 flex flex-col">
      <!-- Search Section (Always Centered when no results) -->
      <div class="flex-1 flex flex-col justify-center items-center px-4 py-8">
        <h1 class="text-5xl md:text-6xl font-bold uppercase tracking-wide mb-8 text-white text-center">
          Fashion Connect
        </h1>

        <div class="w-full max-w-3xl mx-auto">
          <div class="flex items-center bg-white rounded-full overflow-hidden shadow-lg">
            <input
              v-model="searchQuery"
              @keyup.enter="searchProducts"
              type="text"
              placeholder="Search for clothes (e.g., T-shirt, Jeans, Dress)..."
              class="w-full px-6 py-4 rounded-l-full focus:outline-none text-gray-700 text-lg"
            />
            <button
              @click="searchProducts"
              class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-r-full text-lg transition-colors"
            >
              🔍
            </button>
          </div>
        </div>
      </div>

      <!-- Results Section (Scrollable) -->
      <div
        v-if="products.length > 0"
        class="w-full max-w-6xl mx-auto px-4 pb-8"
      >
        <h3 class="text-3xl text-center text-white mb-6">Search Results</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          <div
            v-for="product in products"
            :key="product.title"
            class="bg-white rounded-lg shadow-md p-4 transform hover:scale-105 transition-transform duration-200"
          >
            <img
              :src="product.image"
              alt="Product image"
              class="w-full h-48 object-cover rounded-md mb-3"
            />
            <h4 class="font-semibold text-lg mb-2">{{ product.title }}</h4>
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
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const searchQuery = ref('');
const products = ref([]);

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

<style scoped>
/* Add any custom styles here if needed */
</style>

