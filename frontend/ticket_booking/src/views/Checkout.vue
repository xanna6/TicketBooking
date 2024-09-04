<template>
<div class="container">
  <div class="shadow-sm p-4 mb-4 mt-4 bg-white rounded">
    <div class="statement">
      <h4>Tickets Booked Successfully</h4>
      <router-link :to="{name: 'Home'}">
        <button class=" btn btn-outline-secondary">Home page</button>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>

</script>

<style scoped>
.btn {
  width: 200px;
  margin-top: 10px;
}
.statement {
  width: 400px;
  margin: 30px auto;
  text-align: center;
}
</style>