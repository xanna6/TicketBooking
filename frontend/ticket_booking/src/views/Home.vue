<template>
  <div class="container">
    <h4>Screenings</h4>
    <div class="movie-list" v-for="movie in movies" v-bind:key="movie.id">
      <div class="row">
        <div class="col-3 movie-poster">
          <img class="poster" :src="movie.image_path" alt="movie poster">
        </div>
        <div class="col-9">
          <div id="movie-title">
            <router-link :to="{ name: 'MovieDetails', params: { id: movie.id } }">
            <span class="movie-title">{{ movie.title }}</span>
          </router-link>
          </div>
          <div class="screenings">
            <div id="screening" v-for="screening in movie.screenings" v-bind:key="screening.hall_screening_time.id">
              <button class="btn btn-secondary btn-screening">{{ screening.hall_screening_time.time }}</button>
            </div>
          </div>
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
.screenings {
  margin-top: 100px;
}
#screening {
  display: inline;
  margin-right: 20px;
}
.btn-screening {
  margin-top: 30px;
  background-color: darkorange;
  border-color: darkorange;
}
.btn-screening:hover {
  background-color: orangered;
  border-color: orangered;
}
.btn-screening:active {
  background-color: red !important;
  border-color: red !important;
}
</style>