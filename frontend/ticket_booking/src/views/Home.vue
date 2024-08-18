<template>
  <div class="container">
    <h4 class="inline">Screenings</h4>
    <div class="inline date-picker">
      <i class="bi bi-calendar-week"></i>
      <button @click="previousDay" :disabled="isPreviousDisabled"><i class="bi bi-chevron-left"></i></button>
      <span>{{ formattedDate }}</span>
      <button @click="nextDay"><i class="bi bi-chevron-right"></i></button>
    </div>
    <div class="movie-list" v-for="movie in moviesThatDay" v-bind:key="movie.id">
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
            <div id="screening" v-for="screening in movie.screenings" v-bind:key="screening.id">
              <button class="btn btn-secondary btn-screening">{{ screening.time }}</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref, watch} from "vue";

export default {
  props: {
    movies: {
      type: Array,
      required: true
    }
  },

  setup(props) {
    const currentDate = ref(new Date());
    const moviesThatDay = ref(props.movies);

    const fetchMovies = async (date) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/movies/?date=${date.toISOString().split('T')[0]}`);
        moviesThatDay.value = await response.json();
      } catch (error) {
        console.error(error);
      }
    };

    const previousDay = () => {
      currentDate.value = new Date(currentDate.value.setDate(currentDate.value.getDate() - 1));
    };

    const nextDay = () => {
      currentDate.value = new Date(currentDate.value.setDate(currentDate.value.getDate() + 1));
    };

    const formattedDate = computed(() => {
      const options = {weekday: 'long', day: '2-digit', month: '2-digit'};
      return currentDate.value.toLocaleDateString('en-GB', options);
    });

    const isPreviousDisabled = computed(() => {
      return currentDate.value.toDateString() === new Date().toDateString();
    });

    watch(currentDate, (newDate) => {
      fetchMovies(newDate);
    }, {immediate: true});

    onMounted(() => {
      fetchMovies(currentDate.value);
    });

    return {
      currentDate,
      moviesThatDay,
      previousDay,
      nextDay,
      formattedDate,
      isPreviousDisabled
    };
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

.inline {
  display: inline-block;
  vertical-align: middle;
}

.date-picker {
  display: inline-block;
  vertical-align: middle;
  font-size: 18px;
  margin: 20px 20px 20px 100px;
}

.date-picker button {
  border: none;
  margin: 0 10px;
}
</style>