<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand ms-3" href="/">TicketBooking</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <form @submit.prevent="fetchMovies" class="form-inline mx-auto my-2 my-lg-0 d-flex">
          <input v-model="searchQuery" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
        <ul class="navbar-nav ml-auto me-3">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Register'}">
              <span>Sign up</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Login'}">
              <span>Sign in</span>
            </router-link>
          </li>
        </ul>
      </div>
    </nav>

  <router-view :movies="movies"/>

</template>

<script>
import {onMounted, ref} from 'vue';

export default {
  setup() {
    const searchQuery = ref('');
    const movies = ref([]);

    const fetchAllMovies = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/movies/');
        movies.value = await response.json();
      } catch (error) {
        console.error(error);
      }
    };

    const fetchMovies = async () => {
      if (searchQuery.value.length > 0) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/movies/?search=${searchQuery.value}`);
          movies.value = await response.json();
        } catch (error) {
          console.error(error);
        }
      } else {
        await fetchAllMovies();
      }
    };

    onMounted(() => {
      fetchAllMovies();
    });

    return {
      searchQuery,
      movies,
      fetchMovies
    };
  }
};
</script>

<style scoped>
.loginBtn {
  text-decoration: none;
}
</style>