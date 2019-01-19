<template>
    <div style="padding:20px">
        <div v-if="user">
            <h3>Edit User</h3>
            <label>User Name</label>
            <input class="form-control" v-model="user.username">
            <label>First Name</label>
            <input class="form-control" v-model="user.firstName">
            <label>Last Name</label>
            <input class="form-control" v-model="user.lastName">
            <label>Email</label>
            <input class="form-control" v-model="user.email">
            <label>Team (Not working)</label>
            <!-- <input class="form-control" v-model=""> -->
            <button class="btn btn-secondary" @click="update()">Update User</button>
        </div>
        <div v-else>
            Redirect.. You cannot access this page directly
        </div>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'User',
  props: ['user'],
  data () {
    return {
      message: ""
    }
  },
  methods: {
      update() {

        let that = this;
        api(`mutation { updateteam(id:${this.team.id}, name:"${this.team.name}", affiliation:"${this.team.affiliation}", email:"${this.team.email}", website:"${this.team.website}", accesscode:"${this.team.accesscode}"){ message } }`).then(data => {
            that.message = data.updateteam.message;
        })
      }
  }
}
</script>

<style scoped>
.stats {
  color: black;
  text-align: center;
  cursor: pointer;
  margin-bottom: 0;
}
.stats:hover {
  text-decoration: underline;
}
label {
    margin-top: 10px; 
    margin-bottom: 0px;
}
</style>