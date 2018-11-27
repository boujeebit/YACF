<template>
  <div class="text-center">

    <div class="form-signin">
      <!-- <img class="mb-4" src="" alt="" width="125" height="125"> -->
      <h1 class="h3 mb-3 font-weight-normal">Team Register</h1>
      <p>{{message}}</p>
      <input class="form-control" placeholder="Team Name" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="teamname">
      <input class="form-control" placeholder="Admin Email" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="email">

      <input class="form-control" placeholder="Affiliation" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="affiliation">

      <p class="text-muted">Access Code will be sent to you via email.</p>

      <button class="btn btn-lg btn-block btn-secondary" @click="Register()">Register Team</button>

      <p class="mt-5 mb-3 text-muted"><a @click="$router.push('/Login');">Sign In</a></p>
      <p class="text-muted">&copy; 2018</p>
    </div>
  </div>
</template>

<script>
import { api } from '@/utils/api'

export default {
  name: '',
  data () {
    return {
        teamname    : "",
        email       : "",
        affiliation : "",
        message     : ""
    }
  },
  methods: {
    Register() {
      let that = this;
      api(`mutation { addteam(name:"${this.teamname}", affiliation:"${this.affiliation}", email:"${this.email}"){ code } }`).then(data => {
        if (data.addteam.code === 0){
              that.message = "Team created successfully"
          } else {
              that.message = "An error occured."
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

input {
  margin-top: 5px;
}

button {
  margin-top: 5px;
}


</style>