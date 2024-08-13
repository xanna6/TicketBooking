<template>
  <a @click="$router.go(-1)">
    <button class="btn btn-outline-dark btn-back" type="submit"><i class="bi bi-chevron-left"></i> Back</button>
  </a>
  <div v-if="movie" class="container">
    <div class="shadow-sm p-4 mb-4 bg-white rounded">
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
    <div id="movieDetailsScreenings">
      <h4 class="inline">Screenings</h4>
      <div class="inline date-picker">
        <i class="bi bi-calendar-week"></i>
        <button @click="previousDay" :disabled="isPreviousDisabled"><i class="bi bi-chevron-left"></i></button>
        <span>{{ formattedDate }}</span>
        <button @click="nextDay"><i class="bi bi-chevron-right"></i></button>
      </div>
      <div style="clear: both">
      </div>
      <div id="screening" v-for="screening in movie.screenings" v-bind:key="screening.hall_screening_time.id">
        <button class="btn btn-secondary btn-screening">{{ screening.hall_screening_time.time }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref, watch} from 'vue';

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const movie = ref(null);
    const currentDate = ref(new Date());


    const fetchMovieDetails = async (date) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/movieDetails/${props.id}/?date=${date.toISOString().split('T')[0]}`);
        movie.value = await response.json();
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
      fetchMovieDetails(newDate);
    }, {immediate: true});

    onMounted(() => {
      fetchMovieDetails(currentDate.value);
    });

    return {
      movie,
      previousDay,
      nextDay,
      formattedDate,
      isPreviousDisabled
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

#movieDetailsScreenings {
  margin-bottom: 100px;
}
</style>