<template>
  <div class="text-center">

    <div class="form-signin">
      <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->
      <h1 class="h3 mb-3 font-weight-normal">YACF Login</h1>
      <p>{{message}}</p>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input class="form-control" placeholder="Username" v-model="username">
      <label for="inputPassword" class="sr-only">Password</label>
      <input class="form-control" placeholder="Password" v-model="password">

      <button class="btn btn-lg btn-block btn-secondary" @click="login()">Sign in</button>

      <!-- <p class="mt-5 mb-3 text-muted"><a href="/account/register">Register Here</a></p> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: '',
  data () {
    return {
        username: "user5",
        password: "Password123!",
        message : ""
    }
  },
  methods: {
      login() {
        let that = this;
        axios({
          method: 'post',
          url: 'http://localhost:8000/graphql/',
          withCredentials: true,
          data: {
              'query': `mutation { login(username:"${that.username}", password:"${that.password}") { id } }`
          },
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(r => r.data.data.login)
        .then(login => {
            if (login){
                that.$store.commit("SET_USER", login)
                that.message = "Login successful"
            } else {
                that.message = "Login incorrect"
            }
            // commit('SET_BOARD', board)
            console.log(login);
        });
      }
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