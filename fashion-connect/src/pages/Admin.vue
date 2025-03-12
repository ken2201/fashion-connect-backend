<template>
  <div class="p-8 space-y-6">
    <h1 class="text-3xl font-bold mb-4">Admin Panel - Manage Products</h1>

    <!-- Formulaire d'ajout de produit -->
    <div class="space-y-4 bg-gray-100 p-4 rounded shadow">
      <h2 class="text-2xl font-semibold">Add Product</h2>
      <input v-model="newProduct.name" placeholder="Product Name" class="w-full p-2 rounded border" />
      <input v-model="newProduct.price" type="number" placeholder="Price (€)" class="w-full p-2 rounded border" />
      <input v-model="newProduct.description" placeholder="Description" class="w-full p-2 rounded border" />
      <input v-model="newProduct.image_url" placeholder="Image URL" class="w-full p-2 rounded border" />
      <input v-model="newProduct.brand" placeholder="Brand" class="w-full p-2 rounded border" />
      <input v-model="newProduct.link" placeholder="Official Store Link" class="w-full p-2 rounded border" />
      <button @click="addProduct" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        Add Product
      </button>
    </div>

    <!-- Liste des produits -->
    <h2 class="text-2xl font-semibold mt-6">Product List</h2>
    <div v-if="products.length" class="space-y-4">
      <div v-for="product in products" :key="product.id" class="bg-white p-4 rounded shadow space-y-2">
        <img :src="product.image_url" class="w-full h-40 object-cover rounded" />
        <h3 class="text-xl font-bold">{{ product.name }}</h3>
        <p><strong>Brand:</strong> {{ product.brand }}</p>
        <p><strong>Price:</strong> {{ product.price }} €</p>
        <p><strong>Description:</strong> {{ product.description }}</p>
        <a :href="product.link" target="_blank" class="text-blue-500 underline">Visit Store</a>

        <!-- Boutons actions -->
        <div class="flex space-x-2 mt-2">
          <button @click="editProductForm(product)" class="bg-yellow-400 px-3 py-1 rounded">Edit</button>
          <button @click="deleteProduct(product.id)" class="bg-red-500 text-white px-3 py-1 rounded">Delete</button>
        </div>
      </div>
    </div>
    <p v-else>No products available.</p>

    <!-- Formulaire de modification -->
    <div v-if="editingProduct" class="space-y-4 bg-gray-100 p-4 rounded shadow mt-6">
      <h2 class="text-2xl font-semibold">Edit Product</h2>
      <input v-model="editingProduct.name" placeholder="Product Name" class="w-full p-2 rounded border" />
      <input v-model="editingProduct.price" type="number" placeholder="Price (€)" class="w-full p-2 rounded border" />
      <input v-model="editingProduct.description" placeholder="Description" class="w-full p-2 rounded border" />
      <input v-model="editingProduct.image_url" placeholder="Image URL" class="w-full p-2 rounded border" />
      <input v-model="editingProduct.brand" placeholder="Brand" class="w-full p-2 rounded border" />
      <input v-model="editingProduct.link" placeholder="Official Store Link" class="w-full p-2 rounded border" />
      <div class="flex space-x-2">
        <button @click="updateProduct" class="bg-green-500 text-white px-4 py-2 rounded">Update</button>
        <button @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const newProduct = ref({
  name: '',
  price: '',
  description: '',
  image_url: '',
  brand: '',
  link: ''
});

const editingProduct = ref(null);
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLZW4iLCJleHAiOjE3NDE4ODUzOTV9.Sflgc8t62tTnhNcQTtO3NNmInYuYArMJPD365j3Buds'; // ✅ Ton token

const fetchProducts = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/products');
    products.value = response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
  }
};

const addProduct = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/add_product', newProduct.value, {
      headers: { Authorization: `Bearer ${token}` }
    });
    await fetchProducts();
    newProduct.value = { name: '', price: '', description: '', image_url: '', brand: '', link: '' };
  } catch (error) {
    console.error('Error adding product:', error);
  }
};

const editProductForm = (product) => {
  editingProduct.value = { ...product };
};

const updateProduct = async () => {
  try {
    await axios.put(`http://127.0.0.1:8000/update_product/${editingProduct.value.id}`, editingProduct.value, {
      headers: { Authorization: `Bearer ${token}` }
    });
    await fetchProducts();
    editingProduct.value = null;
  } catch (error) {
    console.error('Error updating product:', error);
  }
};

const deleteProduct = async (id) => {
  try {
    await axios.delete(`http://127.0.0.1:8000/delete_product/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    await fetchProducts();
  } catch (error) {
    console.error('Error deleting product:', error);
  }
};

const cancelEdit = () => {
  editingProduct.value = null;
};

onMounted(fetchProducts);
</script>
