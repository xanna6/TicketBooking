<template>
  <div class="container">
    <h4>Screenings</h4>
    <div class="movie-list" v-for="movie in movies" v-bind:key="movie.id">
      <div class="row">
        <div class="col-3 movie-poster">
          <img class="poster" :src="movie.image_path" alt="movie poster">
        </div>
        <div class="col-9">
          <router-link :to="{ name: 'MovieDetails', params: { id: movie.id } }">
            <span class="movie-title">{{ movie.title }}</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movies: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>
.container {
  margin-top: 10px;
  width: 50%;
}
.movie-poster {
  float: left;
}
.poster {
  width: 150px;
  height: 200px;
}
.movie-title {
  float: left;
  font-size: 20px;
  font-weight: bold;
  color: black;
}
.movie-title:hover {
  color: grey;
  cursor: pointer;
}
.movie-list {
  padding: 30px 0;
  border-bottom: solid;
  border-color: lightgray;
}
</style>