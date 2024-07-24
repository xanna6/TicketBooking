<template>
    <div class="card m-3">
        <div class="card-body">
            <div v-if="users">
                <h5>Users</h5>
                <ul class="mb-0">
                    <li v-for="user in users" :key="user.id">{{user.name}}</li>
                </ul>
            </div>
            <div v-if="!users" class="text-center">
                <div class="spinner-border spinner-border-sm"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const users = ref(null);

fetch('http://localhost:8000/users/')
    .then(response => response.json())
    .then(data => users.value = data);
</script>

