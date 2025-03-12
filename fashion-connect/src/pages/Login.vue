<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold mb-6 text-center">🛍️ Fashion Connect - Admin Login</h1>

      <!-- Formulaire de connexion -->
      <form @submit.prevent="login" class="space-y-4">
        <input
          v-model="form.username"
          type="text"
          placeholder="Username"
          required
          class="w-full p-2 rounded border"
        />
        <input
          v-model="form.password"
          type="password"
          placeholder="Password"
          required
          class="w-full p-2 rounded border"
        />
        <button
          type="submit"
          class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          Login
        </button>
      </form>

      <!-- Message d'erreur -->
      <p v-if="error" class="text-red-500 mt-4 text-center">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      error: ''
    };
  },
  methods: {
    async login() {
      try {
        const params = new URLSearchParams();
        params.append('username', this.form.username);
        params.append('password', this.form.password);

        const response = await axios.post('http://127.0.0.1:8000/token', params);

        const token = response.data.access_token;
        // Stocker le token pour les futures requêtes
        localStorage.setItem('token', token);

        // Redirection vers Admin.vue après connexion
        this.$router.push('/admin');
      } catch (error) {
        console.error('Login error:', error);
        this.error = "❌ Incorrect username or password";
      }
    }
  }
};
</script>

<style scoped>
/* Styles personnalisés si besoin */
</style>

