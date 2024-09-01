<template>
  <div class="container">
    <div class="shadow-sm p-4 mb-4 bg-white rounded">
      <h4>Checkout</h4>
      <div class="number-of-tickets">Number of tickets: <b>{{ ticketIds.length }}</b>
        <h5>Personal data</h5>
      </div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="firstName">First Name:</label>
          <input v-model="form.firstname" id="firstName" type="text" required />
        </div>

        <div>
          <label for="lastName">Last Name:</label>
          <input v-model="form.lastname" id="lastName" type="text" required />
        </div>

        <div>
          <label for="email">Email:</label>
          <input v-model="form.email" id="email" type="email" required />
        </div>

        <div>
          <label for="phone">Phone Number:</label>
          <input v-model="form.phone" id="phone" type="tel" required />
        </div>
        <div class="button-container">
          <button type="submit" class="btn btn-success">Confirm</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {useRoute} from "vue-router";
import {ref} from 'vue';

export default {
  name: "Checkout.vue",
  props: {
    ids: {
      type: String
    }
  },
  setup() {
    const route = useRoute();
    const ticketIds = route.query.ids.split(',');

    const form = ref({
      firstname: '',
      lastname: '',
      email: '',
      phone: ''
    });

    async function submitForm() {
      try {
        console.log(JSON.stringify(form.value))
        const response = await fetch('http://127.0.0.1:8000/customer/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(form.value)
        });

        if (!response.ok) {
          throw new Error('Failed to submit form');
        }

        const result = await response.json();
        console.log('Form submitted successfully:', result);

      } catch (error) {
        console.error('Error submitting form:', error);
      }
    }

    return {
      ticketIds,
      form,
      submitForm
    }
  }
}

</script>

<style scoped>
form {
  max-width: 400px;
  margin: auto;
}

div {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border: none;
  border-radius: 20px;
  background-color: #f1f1f1;
  font-size: 16px;
}

input:focus {
  outline: none;
  background-color: #e9e9e9;
}

button {
  padding: 10px 20px;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  width: 300px;
  margin: auto;
}

button:hover {
  background-color: #45a049;
}
.button-container {
  margin-top: 40px;
  text-align: center;
}
.number-of-tickets {
  max-width: 400px;
  font-size: 18px;
  margin: 20px auto;
}
h5 {
  margin-top: 25px;
}
</style>