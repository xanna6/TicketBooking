<template>
<div class="container">
    <div class="shadow-sm p-4 mb-4 bg-white rounded">
      <h4>Sign in</h4>
      <form>
        <div>
          <label for="email">E-mail:</label>
          <input id="email" type="email" required />
        </div>

        <div>
          <label for="phone">Password:</label>
          <input id="password1" type="password" required />
        </div>

        <div class="button-container">
          <button type="submit" class="btn btn-success">Sign in</button><br>
          <div class="register">
            <p class="register-p">Don't have an account yet?  </p>
            <router-link :to="{name: 'Register'}">
              <a class="nav-link register-link">Sign up</a>
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login"
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

.register-link {
  color: #45a049;
  display: inline;
}

.register-p {
  display: inline;
}

.register {
  margin-top: 20px;
}
</style>