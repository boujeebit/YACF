<template>
    <div style="float: right;">
        <!-- Modal Component -->
        <button class="btn btn-sm btn-secondary" v-b-modal="openid">Edit</button>
        <b-modal v-bind:id="openid" v-bind:title="team.name" ok-title='Update' ok-variant='success'>
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
        </b-modal>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Challenges',
  props: ['team'],
  data () {
    return {
      message: ""
    }
  },
  computed: {
    openid() {
      return "edit-"+this.team.id;
    }
  },
  methods: {
      handleOk ( evt ) {
        evt.preventDefault()

        let that = this;
        api(`mutation{ submitflag(challenge:${this.chal.id}, flag:"${this.flag}"){ code } }`).then(data => {
            
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