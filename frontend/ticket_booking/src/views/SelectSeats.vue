<template>
  <div v-if="screening" class="container">
    <div>{{ screening.date}} {{ screening.time}}</div>
    <div>Hall: {{ screening.hall.id}} - {{ screening.hall.name}}</div>
    <h3>Select your seats</h3>

    <div class="screen">Screen</div>
    <div v-for="rowIndex in screening.hall.rows" :key="rowIndex" class="row">
      <span class="rowIndex">{{ rowIndex }}</span>
      <span v-for="seatIndex in screening.hall.seats_in_row" :key="seatIndex" class="seat">
        <button class="seatBtn" @click="toggleSeat(rowIndex, seatIndex)">
          <i :class="{'bi bi-square-fill fs-4 seat-selected': isSelected(rowIndex, seatIndex),
           'bi bi-square-fill fs-4 seat-available': !isSelected(rowIndex, seatIndex)}"></i>
        </button>
      </span>
    </div>
    <div class="seat-legend">
      <div class="seat-legend-item">
        <i class="bi bi-square-fill fs-4 seat-available"></i><label class="seat-legend-label"> Available </label>
      </div>
      <div class="seat-legend-item">
        <i class="bi bi-square-fill fs-4 seat-selected"></i><label class="seat-legend-label"> Selected </label>
      </div>
      <div class="seat-legend-item">
        <i class="bi bi-square-fill fs-4 seat-occupied"></i><label class="seat-legend-label"> Occupied </label>
      </div>
    </div>
    <div class="button-container">
      <button class="btn btn-success">Next</button>
      <a @click="$router.go(-1)">
        <button class="btn btn-outline-secondary" type="submit"><i class="bi bi-chevron-left"></i> Back</button>
      </a>
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
    const selectedSeats = ref([]);

    const fetchScreeningDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/screening/${props.id}/`);
        screening.value = await response.json();
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      fetchScreeningDetails();
    });

    const toggleSeat = (rowIndex, seatIndex) => {
      const seat = { row: rowIndex, seat: seatIndex };

      const seatIndexInArray = selectedSeats.value.findIndex(
        (s) => s.row === rowIndex && s.seat === seatIndex
      );

      if (seatIndexInArray > -1) {
        selectedSeats.value.splice(seatIndexInArray, 1);
      } else {
        selectedSeats.value.push(seat);
      }
    };

    const isSelected = (rowIndex, seatIndex) => {
      return selectedSeats.value.some(
        (s) => s.row === rowIndex && s.seat === seatIndex
      );
    };

    return {
      screening,
      toggleSeat,
      isSelected,
      selectedSeats
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
  width: 40px;
}
.bi {
  border-radius: 4px;
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
.seat-selected {
  color: orange;
}
.seat-available {
  color: limegreen;
}
.seatBtn {
  border: none;
}
.seat-occupied  {
  color: grey;
}
.seat-legend {
  display: flex;
  align-items: center;
  margin: 50px auto 10px auto;
  justify-content: space-around;
  width: 50%;
}
.seat-legend-item {
  display: inline;
  margin-right: 100px;
}
.seat-legend-label {
  margin-left: 10px;
}
.button-container {
  width: 300px;
  align-items: center;
  margin: 0 auto 80px auto;
}
.btn {
  margin-top: 20px;
  width: 300px;
}
</style>