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
            <a class="nav-link" href="#">Sign in</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Register</a>
          </li>
        </ul>
      </div>
    </nav>

  <Home :movies="movies"/>

</template>

<script>
import {onMounted, ref} from 'vue';
import Home from "./views/Home.vue";

export default {
  components: {Home},
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

