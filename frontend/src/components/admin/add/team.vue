<template>
    <div style="padding:20px">
        <h3>Add Team</h3>
        <label>Team name:</label>
        <input class="form-control" v-model="name">
        <label>Access Code:</label>
        <input class="form-control" v-model="code">
        <p>{{message}}</p>
        <button class="btn btn-secondary" @click="addTeam()">Add Team</button>
    </div>
</template>

<script>
import { api } from '@/utils/api'

export default {
  name: 'AddTeam',
  data () {
    return {
        name: "",
        code: "",
        message: ""
    }
  },
  methods: {
      addTeam () {
        let that = this;
        api(`mutation { addteam(name:"${this.name}", accesscode:"${this.code}"){ message } }` ).then(data => {
            that.message = data.addteam.message;
        })
      }
  }
}
</script>

<style scoped>
</style>