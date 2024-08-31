<template>
  <div class="container">
    <h4>Checkout</h4>
    <div>
      Selected seats: {{ ticketIds }}
    </div>
  </div>
</template>

<script>
import {useRoute} from "vue-router";

export default {
  name: "Checkout.vue",
  props: {
    ids: {
      type: String
    }
  },
  setup(props) {
    const route = useRoute();
    const ticketIds = route.query.ids.split(',');
    console.log(ticketIds);

    return {
      ticketIds
    }
  }
}
</script>

<style scoped>

</style>