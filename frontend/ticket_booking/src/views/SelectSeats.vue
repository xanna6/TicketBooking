<template>
  <div v-if="screening" class="container">
    <div>{{ screening.date}} {{ screening.time}}</div>
    <div>Hall: {{ screening.hall.id}} - {{ screening.hall.name}}</div>
    <h3>Select your seats</h3>

    <div class="screen">Screen</div>
    <div v-for="rowIndex in screening.hall.rows" :key="rowIndex" class="row">
      <span class="rowIndex">{{ rowIndex }}</span>
      <span v-for="seatIndex in screening.hall.seats_in_row" :key="seatIndex" class="seat">
        <i class="bi bi-square-fill fs-4"></i>
      </span>
    </div>
  </div>

</template>

<script>
import {onMounted, ref} from "vue";

export default {
  name: "SelectSeats",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const screening = ref(null);


    const fetchScreeningDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/screening/${props.id}/`);
        screening.value = await response.json();
        console.log(screening.value)
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      fetchScreeningDetails();
    });

    return {
      screening
    };
  }
}
</script>

<style scoped>
.row {
  display: flex;
  margin-bottom: 10px;
  justify-content: center;
}
.rowIndex {
  margin-top: 10px;
  width: 20px;
}
.seat {
  display: inline;
  width: 50px;
}
.bi {
  border-radius: 4px;
  color: grey;
}
.container {
  width: 100%;
  margin: 0 100px;
}
.screen {
  width: 100%;
  height: 20px;
  color: grey;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: 2px solid;
  text-align: center;
  margin: 20px 0;
}
</style>