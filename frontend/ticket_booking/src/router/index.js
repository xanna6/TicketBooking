import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import MovieDetails from '../views/MovieDetails.vue';
import SelectSeats from '../views/SelectSeats.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movieDetails/:id',
    name: 'MovieDetails',
    component: MovieDetails,
    props: true
  },
  {
    path: '/book/select-seats/',
    name: 'SelectSeats',
    component: SelectSeats,
    props: route => ({ id: route.query.id })
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;