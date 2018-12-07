<template>
    <div style="float: right;">
        <!-- Modal Component -->
        <button class="btn btn-sm btn-danger" v-b-modal="team.id" style="margin-left: 5px;">Remove</button>
        <b-modal v-bind:id="team.id" v-bind:title="title" ok-title='Confirm Remove' ok-variant='danger' @ok="handleOk">
          <p>Are you sure you want to <strong>delete {{team.name}}</strong>? This action cannot be undone. Type in the team name below to confirm the deletion.</p>
          <label>Team Name</label>
          <input class="form-control" v-model="confirm">
          {{message}}
        </b-modal>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Team',
  props: ['team'],
  data () {
    return {
      loading: true,
      challenge: "",
      confirm: "",

      message: ""
    }
  },
  computed: {
    title() {
      return "Deleting " + this.team.name;
    }
  },
  methods: {
      handleOk ( evt ) {
        console.log("Delete");
        evt.preventDefault()

        // TODO: Delete out of list
        let that = this;
        if (this.confirm === this.team.name){
            api(`mutation { removeteam(name:"${this.team.name}"){ code } }`).then(data => {
                if (data.removeteam.code === 0) {
                    that.message = "Team deleted."
                } else {
                    that.message = "Team was not delete. API error"
                }
            })
        } else {
            that.message = "Team was not delete. Confirmation incorrect"
        }

      },
      loaddata () {
        let that = this;
        api(`query{ team(name:"team4"){ ${team.name} } }`).then(data => {
            that.team = data.challenge;
            that.loading   = false;
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