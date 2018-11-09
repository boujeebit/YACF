<template>
    <div>
        <h3>{{this.$route.params.category}} - {{this.$route.params.points}}</h3>
        <hr>
        <div v-if="loading">
            Loading Stats, hold on.
        </div>
        <div v-else>
            <h5>Solves</h5>
            <div v-if="teams[0]">
            <table id="statistics" class="table table-hover">
                <thead>
                    <tr>
                    <th>Rank</th>
                    <th>Team name</th>
                    <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(team, index) in teams" :key="team.id" style="cursor: pointer;" @click="$router.push(`/team/${team.teamSet[0].name}`);">
                        <td>{{index+1}}</td>
                        <td>{{team.teamSet[0].name}}</td>
                        <td>{{team.timestamp | moment("dddd, MMMM Do YYYY, h:mm:ss a") }}</td>
                    </tr>
                </tbody>
            </table>
            </div>
            <div v-else>
                <p style="text-align: center;">No team has solved this challenge yet.</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Statistic',
  data () {
    return {
        loading: true,
        teams: ""
    }
  },
  methods: {
      
  },
  beforeMount () {
    console.log("Making call to get Stats for: ", this.$route.params.category, this.$route.params.points);
    let that = this;
    axios
        .post('http://127.0.0.1:8000/graphql/', {
            'query': 
            `query{
                statistic(category:"${this.$route.params.category}", points:${this.$route.params.points}){ 
                    id
                    solvedchallengeSet{
                        timestamp
                        teamSet{
                            id
                            name
                        }
                    }
                }
            }` 
        })
        .then(r => r.data.data.statistic)
        .then(statistic => {
        console.log(statistic);
        that.teams = statistic.solvedchallengeSet;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>