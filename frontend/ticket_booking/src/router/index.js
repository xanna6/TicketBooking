import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import MovieDetails from '../views/MovieDetails.vue';
import SelectSeats from '../views/SelectSeats.vue';
import Checkout from '../views/Checkout.vue';
import Summary from "@/views/Summary.vue";

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
    path: '/select-seats/',
    name: 'SelectSeats',
    component: SelectSeats,
    props: route => ({ id: route.query.id })
  },
  {
    path: '/order-summary/',
    name: 'Summary',
    component: Summary,
    props: true
  },
    {
    path: '/checkout/',
    name: 'Checkout',
    component: Checkout
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;