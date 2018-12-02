<template>
    <div style="float: right;">
        <!-- Modal Component -->
        <button class="btn btn-sm btn-danger" v-b-modal="challenge.id" style="margin-left: 5px;">Remove</button>
        <b-modal v-bind:id="challenge.id" v-bind:title="title" ok-title='Confirm Remove' ok-variant='danger' @ok="handleOk">
          <p>Are you sure you want to <strong>delete {{challenge.name}}</strong>? This action cannot be undone. If any team has solved this challenge their solves will also be removed. Type in the challenge name below to confirm the deletion.</p>
          <label>Challenge Name</label>
          <input class="form-control" v-model="confirm">
          {{message}}
        </b-modal>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Challenges',
  props: ['challenge'],
  data () {
    return {
      confirm: "",
      message: ""
    }
  },
  computed: {
    title() {
      return "Deleting " + this.challenge.name;
    }
  },
  methods: {
      handleOk ( evt ) {
        console.log("Delete");
        evt.preventDefault()

        // TODO: Delete out of list
        let that = this;
        if (this.confirm === this.challenge.name){
            api(`mutation { removeChallenge(id:${this.challenge.id}){ code } }`).then(data => {
                if (data.removeChallenge.code === 0) {
                    that.message = "Challenge deleted."
                } else {
                    that.message = "Challenge was not delete. API error"
                }
            })
        } else {
            that.message = "Challenge was not delete. Confirmation incorrect"
        }

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