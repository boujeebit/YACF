<template>
  <div>
    <div class="top-section logo">
      <a href="#">
        <img
          class="navbar-brand-minimized"
          src="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwitpLDs36vjAhURWs0KHRDhCUAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.kisspng.com%2Fpng-white-flag-wait-white-flag-82944%2F&psig=AOvVaw1lSmLL__LGGjmHHt_h_rO1&ust=1562896104731392"
          width="250"
          height="200"
          alt="Total Recon"
        />
      </a>
    </div>

    <div class="bottom-section text-center">
      <div class="form-signin">
        <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->

        <p>{{message}}</p>
        <input
          class="form-control"
          placeholder="Username"
          autocomplete="off"
          autocorrect="off"
          autocapitalize="off"
          spellcheck="false"
          v-model="username"
        />
        <input
          type="password"
          class="form-control"
          placeholder="Password"
          v-model="password"
          v-on:keyup.enter="login()"
        />

        <button class="btn btn-lg btn-block btn-secondary" @click="login()">Sign in</button>

        <!-- <p class="mt-5 mb-3 text-muted">
          <a @click="$router.push('/resigster/user');">Register Here</a>
        </p>-->
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
          that.$router.push("/challenges");
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
}
.bottom-section {
  height: 60vh;
  background-color: #f5f5f5;
}

.logo a img {
  display: block;
  margin: auto;
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

input {
  margin-top: 5px;
}

button {
  margin-top: 5px;
}
</style>