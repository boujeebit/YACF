<template>
    <div>
        <!-- Modal Component -->
        <b-modal v-bind:id="chal.id" v-bind:title="chal.name" ok-title='Submit Flag' ok-variant='secondary'  @shown="loaddata" @ok="handleOk">
          <div v-if="loading">
            Challenge details are loading, please hold!
          </div>
          <div v-else>
            <p class="my-4">Description:</p>
            <span v-html="details.description"></span>
            <p class="my-4">Flag: {{details.flag}}</p>
            <button class="btn btn-secondary" @click="$router.push(`/challenge/${categoryInLowerCase}/${details.points}`);">View Stats</button>
            <div v-if="solved">
              <p>Congrats, you solved the challenge! On to the next one!</p>
            </div>
            <div v-else>
            <b-form-group id="flaggroup" label-for="chad.id" description="Flags are not case sensitive">
              <b-form-input id="chad.id" type="text" required placeholder="Enter Flag" v-model="flag"> </b-form-input>
            </b-form-group>
            <p>{{message}}</p>
            </div>
            
            
          </div>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Challenges',
  props: ['chal'],
  data () {
    return {
      loading: true,
      detials: "",
      flag: "",
      solved: false,
      message: ""
    }
  },
  computed: {
    categoryInLowerCase() {
      return this.details.category.name.toLowerCase().trim();
    }
  },
  methods: {
      handleOk ( evt ) {
        console.log("Here is the flag enter: ", this.flag);
        evt.preventDefault()
        let that = this
        axios({
          method: 'post',
          url: 'http://localhost:8000/graphql/',
          withCredentials: true,
          data: {'query': `mutation{ submitflag(challenge:${that.chal.id}, flag:"${that.flag}"){ code } }` }
        })
        .then(r => r.data.data.submitflag)
        .then(code => {
            console.log(code);
            if (code.code == 1){
              that.solved = true
            } else {
              that.message = "That didn't do it, try again!"
            }
        });          
      },
      loaddata () {
          console.log("Getting details on chanllenge", this.chal.id)
          let that = this
          axios
            .post('http://localhost:8000/graphql/', {'query': `query{ challenge(id:${that.chal.id}){ id, description, points, flag, category { name } } }` })
            .then(r => r.data.data.challenge)
            .then(challenge => {
              console.log(challenge);
              that.details = challenge;
              that.loading = false;
          })
      }
  }
}
</script>

<style scoped>

</style>