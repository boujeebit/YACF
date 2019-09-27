<template>
  <div class="text-center">
    <div class="form-signin">
      <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->
      <h1 class="h3 mb-3 font-weight-normal">User Register</h1>
      <p>{{message}}</p>
      <input class="form-control" placeholder="Username" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="username" />
      <input class="form-control" placeholder="Email" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="email" />
      <input class="form-control" type="password" placeholder="Password" v-model="password1" />
      <input class="form-control" type="password" placeholder="Confirm Password" v-model="password2" />
      <input class="form-control" placeholder="First name" v-model="firstname" />
      <input class="form-control" placeholder="Last name" v-model="lastname" />

      <input class="form-control" placeholder="Team Access Code" v-model="accesscode" />

      <button class="btn btn-lg btn-block btn-secondary" @click="Register()">Register</button>

      <p class="mt-5 mb-3 text-muted">
        <a @click="$router.push('/Login');">Sign In</a> |
        <a @click="$router.push('/resigster/team');">Register Team</a>
      </p>
      <p class="text-muted">&copy; 2018</p>
    </div>
  </div>
</template>

<script>
import { api } from "@/utils/api";

export default {
  name: "",
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      firstname: "",
      lastname: "",
      accesscode: "",
      message: ""
    };
  },
  methods: {
    Register() {
      let self = this;
      api(
        `mutation {  adduser(username:"${this.username}", email:"${this.email}", password:"${this.password1}", firstname:"${this.firstname}", lastname:"${this.lastname}", accesscode:"${this.accesscode}") { code } }`
      ).then(data => {
        if (data.adduser.code === 0) {
          self.$router.push({ name: "Home" });
        } else {
          self.message = "An error occured";
        }
      });
    }
  }
};
</script>

<style scoped>
html,
body {
  height: 100vh;
  background-color: #f5f5f5;
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

input {
  margin-top: 5px;
}

button {
  margin-top: 5px;
}
</style>