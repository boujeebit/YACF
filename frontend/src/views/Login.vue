<template>
  <div class="text-center">

    <div class="form-signin">
      <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->
      <h1 class="h3 mb-3 font-weight-normal">YACF Login</h1>
      <p>{{message}}</p>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input class="form-control" placeholder="Username" v-model="username">
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" class="form-control" placeholder="Password" v-bind:autocapitalize="none" v-model="password">

      <button class="btn btn-lg btn-block btn-secondary" @click="login()">Sign in</button>

      <p class="mt-5 mb-3 text-muted"><a href="/account/register">Register Here</a></p>
      <p class="text-muted">&copy; 2017-2018</p>
    </div>
  </div>
</template>

<script>
import { api } from '@/utils/api'

export default {
  name: '',
  data () {
    return {
        username: "",
        password: "",
        message : ""
    }
  },
  methods: {
    login() {
      let that = this;
      api(`mutation { login(username:"${that.username}", password:"${that.password}") { id } }`).then(data => {
        if (data.login){
              that.$store.commit("user/SET_USER", data.login)
              that.$router.push('/challenges')
          } else {
              that.message = "Login incorrect"
        }
      })
    }
  }
}
</script>

<style scoped>
html,
.text-center {
  height: 100%;
}

.text-center {
  display: -ms-flexbox;
  display: -webkit-box;
  display: flex;
  -ms-flex-align: center;
  -ms-flex-pack: center;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
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
.form-signin input[type="email"] {
  margin-bottom: -1px;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
}

input {
  margin-top: 5px;
}

button {
  margin-top: 5px;
}
</style>