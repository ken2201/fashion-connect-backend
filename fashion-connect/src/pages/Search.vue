<template>
  <div class="p-4 max-w-6xl mx-auto">
    <input
      v-model="searchQuery"
      @keyup.enter="search"
      placeholder="Rechercher un produit (ex: T-shirt)"
      class="border p-2 w-full rounded"
    />
    <button @click="search" class="bg-blue-500 text-white p-2 mt-2 rounded">Rechercher</button>

    <div v-if="products.length" class="mt-4 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div v-for="(product, index) in products" :key="index" class="border p-2 rounded shadow">
        <img :src="product.image" alt="Product Image" class="w-full h-40 object-cover rounded" />
        <h3 class="font-bold mt-2 text-sm">{{ product.title }}</h3>
        <p class="text-gray-600 text-sm">{{ product.price }}</p>
        <a :href="product.link" target="_blank" class="text-blue-500 underline block mt-1 text-center">Voir</a>
      </div>
    </div>
    <div v-else class="mt-4 text-gray-500">Aucun résultat trouvé pour cette recherche.</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchQuery: "",
      products: [],
    };
  },
  methods: {
    async search() {
      try {
        const response = await axios.get(`https://fashion-connect-backend.onrender.com/search?query=${this.searchQuery}`);
        this.products = response.data.results;
      } catch (error) {
        console.error("Erreur lors de la recherche :", error);
      }
    },
  },
};
</script>
