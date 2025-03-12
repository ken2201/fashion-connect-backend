<template>
  <div class="p-8 space-y-6">
    <h1 class="text-3xl font-bold text-center mb-6">Fashion Connect - Find Your Brand</h1>

    <!-- Search Bar -->
    <div class="flex justify-center">
      <input
        v-model="searchQuery"
        @keyup.enter="searchProducts"
        placeholder="Search for a product (e.g., T-shirt, Sneakers...)"
        class="w-full md:w-1/2 p-3 rounded border shadow"
      />
      <button
        @click="searchProducts"
        class="ml-2 bg-blue-500 text-white px-4 py-3 rounded hover:bg-blue-600"
      >
        Search
      </button>
    </div>

    <!-- Results -->
    <div v-if="products.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
      <div
        v-for="product in products"
        :key="product.id"
        class="bg-white rounded-lg shadow-md p-4 flex flex-col space-y-3"
      >
        <img :src="product.image_url" alt="Product Image" class="w-full h-48 object-cover rounded" />
        <h2 class="text-xl font-semibold">{{ product.name }}</h2>
        <p class="text-gray-600">{{ product.description }}</p>
        <p class="text-green-600 font-bold">{{ product.price }} €</p>
        <p class="text-gray-500 italic">Brand: {{ product.brand }}</p>
        <a
          :href="product.link"
          target="_blank"
          class="bg-indigo-500 text-white px-4 py-2 rounded text-center hover:bg-indigo-600"
        >
          See on {{ product.brand }}
        </a>
      </div>
    </div>

    <p v-else class="text-gray-500 text-center mt-8">No products found. Try another search.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const searchQuery = ref('');
const products = ref([]);

// Search products from backend
const searchProducts = async () => {
  try {
    const response = await axios.get(`https://fashion-connect-backend.onrender.com/search_products?query=${searchQuery.value}`);
    products.value = response.data;
  } catch (error) {
    console.error('Search error:', error);
  }
};
</script>

