<template>
  <a @click="$router.go(-1)">
    <button class="btn btn-outline-dark btn-back" type="submit"><i class="bi bi-chevron-left"></i> Back</button>
  </a>
  <div v-if="movie" class="container">
    <div class="shadow-sm p-3 mb-5 bg-white rounded">
      <h2>{{ movie.title }}</h2>
      <div class="row">
        <div class="col-6 movie-poster">
          <img class="movie-details-poster" :src="movie.image_path" alt="movie poster">
        </div>
        <div class="col-6">
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {onMounted, ref} from 'vue';

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const movie = ref(null);

    const fetchMovieDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/movies/${props.id}/`);
        movie.value = await response.json();
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      fetchMovieDetails();
    });

    return {
      movie
    };
  }
};
</script>

<style>
body {
  background-color: #eee;
}
.movie-details-poster {
  width: 300px;
  height: 400px;
}
.btn-back {
  margin-top: 30px;
  margin-left: 100px;
}
</style>