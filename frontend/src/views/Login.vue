<template>
  <div>
    <div class="top-section logo" :style="{backgroundColor: $store.state.theme.primary}">
      <div class="frame">
        <img src="https://github.com/yacf/docs/blob/master/_assets/images/logo-p.png?raw=true" alt="YACF" />
      </div>
    </div>

    <div class="bottom-section text-center" :style="{backgroundColor: $store.state.theme.secondary}">
      <div class="form-signin">
        <h3>CTF Login</h3>

        <p>{{message}}</p>
        <input class="form-control" placeholder="Username" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="username" />
        <input type="password" class="form-control" placeholder="Password" v-model="password" v-on:keyup.enter="login()" />

        <button class="btn btn-lg btn-block btn-secondary" @click="login()">Sign in</button>

        <p class="mt-5 mb-3 text-muted">
          <!-- <a @click="$router.push({name: "RegisterUser"});">Register Here</a> -->
          <router-link :to="{name: 'RegisterUser'}">Register Here</router-link>
        </p>
      </div>
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
      password: "",
      message: ""
    };
  },
  methods: {
    login() {
      let that = this;
      api(
        `mutation { login(username:"${that.username}", password:"${that.password}") { id } }`
      ).then(data => {
        if (data.login) {
          that.$store.commit("user/SET_USER", data.login);
          that.$router.push({ name: "Home" });
        } else {
          that.message = "Login incorrect";
        }
      });
    }
  }
};
</script>

<style scoped>
.top-section {
  height: 40vh;
  border-bottom: 1px solid black;
  background-color: #181b1f;
}
.bottom-section {
  height: 60vh;
  background-color: #1e2125;
}
.frame {
  padding: 35px;
}
.logo img {
  display: block;
  margin-left: auto;
  margin-right: auto;
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
  padding-top: 10px;
  padding-bottom: 40px;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  /* margin: 0 auto; */
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

h3 {
  color: white;
}
p {
  color: white;
}
input {
  margin-top: 5px;
  background-color: #181b1f;
  border-color: black;
}

/* input:focus {
  margin-top: 5px;
  background-color: #181b1f;
  border-color: purple;
  outline: none;
  -webkit-box-shadow: none !important;
  -moz-box-shadow: none !important;
  box-shadow: none !important;
}

button {
  margin-top: 5px;
  background-color: #181b1f;
  border-color: purple;
  color: purple;
} */
</style>