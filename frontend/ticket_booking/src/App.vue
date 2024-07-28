<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand ms-3" href="/">TicketBooking</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <form class="form-inline mx-auto my-2 my-lg-0 d-flex">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
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

  <Home />

</template>

<script setup>
  import Home from './views/Home.vue'
</script>

