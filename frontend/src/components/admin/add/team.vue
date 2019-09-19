<template>
  <div>
    <h3>Add Team</h3>
    <label>Team name:</label>
    <input class="form-control" v-model="name" />
    <label>Affiliation:</label>
    <input class="form-control" v-model="affiliation" />
    <label>Primary Email:</label>
    <input class="form-control" v-model="email" />
    <label>Access Code:</label>
    <input class="form-control" v-model="code" />
    <p>{{message}}</p>
    <button class="btn btn-secondary" @click="addTeam()">Add Team</button>
  </div>
</template>

<script>
import { api } from "@/utils/api";

export default {
  name: "AddTeam",
  data() {
    return {
      name: "",
      affiliation: "",
      email: "",
      code: "",
      message: ""
    };
  },
  methods: {
    addTeam() {
      let that = this;
      api(
        `mutation { addteam(name:"${this.name}", affiliation:"${this.affiliation}", email:"${this.email}", accesscode:"${this.code}"){ code } }`
      ).then(data => {
        that.message = data.addteam.code;
      });
    }
  }
};
</script>

<style scoped>
</style>