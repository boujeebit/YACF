<template>
    <div style="padding:20px">
        <div v-if="team">
            <h3>Edit Team</h3>
            <label>Team Name</label>
            <input class="form-control" v-model="team.name">
            <label>Affiliation</label>
            <input class="form-control" v-model="team.affiliation">
            <label>Admin Email</label>
            <input class="form-control" v-model="team.email">
            <label>Website</label>
            <input class="form-control" v-model="team.website">
            <label>Access Code</label>
            <input class="form-control" v-model="team.accesscode">
            <p>{{message}}</p>
            <button class="btn btn-secondary" @click="update()">Update Team</button>
        </div>
        <div v-else>
            Redirect.. You cannot access this page directly
        </div>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Team',
  props: ['team'],
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