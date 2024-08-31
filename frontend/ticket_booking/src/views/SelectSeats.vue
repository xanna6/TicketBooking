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
      <router-link v-if="seatIds.length" :to="{ name: 'Checkout', query: { ids: seatIds } }">
        <button class="btn btn-success" :disabled="seatIds.length === 0">Next</button>
      </router-link>
      <button v-else class="btn btn-success" disabled>Next</button>
      <a @click="$router.go(-1)">
        <button class="btn btn-outline-secondary" type="submit"><i class="bi bi-chevron-left"></i> Back</button>
      </a>
    </div>
  </div>

</template>

<script>
import {computed, onMounted, ref} from "vue";

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
    let selectedSeats = ref([]);

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
      const seat = { row: rowIndex, seat_in_row: seatIndex };

      const seatIndexInArray = selectedSeats.value.findIndex(
        (s) => s.row === rowIndex && s.seat_in_row === seatIndex
      );

      if (seatIndexInArray > -1) {
        cancelSeat(selectedSeats.value.at(seatIndexInArray).id)
      } else {
        bookSeat(seat);
      }
    };

    const bookSeat = async (seat) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/ticket/?screening_id=${props.id}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(seat)
        });

        if (!response.ok) {
          throw new Error(`Couldn't book a seat - status: ${response.status}`);
        }

        const data = await response.json();
        selectedSeats.value.push(data);
      } catch (error) {
        console.error(error);
      }
    };

    const cancelSeat = async (seat_id) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/ticket/${seat_id}`, {
          method: 'DELETE'
        });

        if (!response.ok) {
          throw new Error(`Couldn't cancel a ticket - status: ${response.status}`);
        }

        selectedSeats.value = selectedSeats.value.filter(seat => seat.id !== seat_id);
      } catch (error) {
        console.error(error);
      }
    };

    const isSelected = (rowIndex, seatIndex) => {
      return selectedSeats.value.some(
        (s) => s.row === rowIndex && s.seat_in_row === seatIndex
      );
    };

    const seatIds = computed(() => {
      return selectedSeats.value.map(seat => seat.id).join(',');
    });

    return {
      screening,
      toggleSeat,
      isSelected,
      selectedSeats,
      seatIds
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