<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <div v-for="team in teams" v-bind:key="team.id">
                {{team.name}} 
                <p>Team: {{team}}</p>
                <hr>
            </div>
        </div>
    
    </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'AdminTeam',
  data () {
    return {
        loading: true,
        teams: []
    }
  },
  methods: {
      
  },
  beforeMount () {
    let that = this;
    axios
    .post('http://127.0.0.1:8000/graphql/', {
        'query': 
        `query {
            allTeams{
                id
                name
                points
                wrongFlags
                correctFlags
                accesscode
            }
        }` 
    })
    .then(r => r.data.data.allTeams)
    .then(allTeams => {
        console.log(allTeams);
        that.teams = allTeams;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>