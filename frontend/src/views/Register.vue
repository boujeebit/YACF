<template>
  <div class="text-center">

    <div class="form-signin">
      <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->
      <h1 class="h3 mb-3 font-weight-normal">YACF Register</h1>

      <label for="inputEmail" class="sr-only">Email address</label>
      <input class="form-control" placeholder="Username" v-model="username">
      <label for="inputPassword" class="sr-only">Password</label>
      <input class="form-control" placeholder="Password" v-model="password">

      <button class="btn btn-lg btn-block btn-secondary">Sign in</button>

      <!-- <p class="mt-5 mb-3 text-muted"><a href="/account/register">Register Here</a></p> -->
    </div>
  </div>
</template>

<script>

export default {
  name: '',
  data () {
    return {
        username: "",
        password: ""
    }
  },
  methods: {
      
  }
}
</script>

<style scoped>
    html,
    .login-wrapper {
      height: 100%;
    }
    
    .login-wrapper {
      display: -ms-flexbox;
      display: flex;
      -ms-flex-align: center;
      align-items: center;
      padding-top: 40px;
      padding-bottom: 40px;
      background-color: #f5f5f5;
    }
    
    .form-signin {
      width: 100%;
      max-width: 330px;
      padding: 15px;
      margin: auto;
    }
    .form-signin .checkbox {
      font-weight: 400;
    }
    .form-signin .form-control {
      position: relative;
      box-sizing: border-box;
      height: auto;
      padding: 10px;
      font-size: 16px;
    }
    .form-signin .form-control:focus {
      z-index: 2;
    }
    input {
        margin: 2.5px 0 2.5px 0;
    }
    input:focus input:active {
      outline: none;
    }
</style>