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
import axios from 'axios'

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
        console.log(this.name, this.code);

        let that = this;
        axios
        .post('http://localhost:8000/graphql/', {
            'query': 
            `mutation {
                addteam(name:"${this.name}", accesscode:"${this.code}"){
                    message
                }
            }` 
        })
        .then(r => r.data.data.addteam)
        .then(addteam => {
            console.log(addteam);
            if (addteam.message == "success") {
                that.message = "Team added successfully"
            } else {
                that.message = "Failed to add team"
            }
        })


      }
  }
}
</script>

<style scoped>
</style>