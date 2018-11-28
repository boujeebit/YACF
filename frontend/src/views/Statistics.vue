<template>
    <div style="margin: 15px;">
        <h3 style="text-align: center;">{{this.$route.params.category}} - {{this.$route.params.points}}</h3>
        <hr>
        <div v-if="loading">
            Loading Stats, hold on.
        </div>
        <div v-else>
            <h5>Solves</h5>
            <div v-if="solves">
            <table id="statistics" class="table table-hover">
                <thead>
                    <tr>
                    <th>Rank</th>
                    <th>Team name</th>
                    <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(solves, index) in solves" :key="solves.id" style="cursor: pointer;" @click="$router.push(`/team/${solves.team.name}`);">
                        <td>{{index+1}}</td>
                        <td>{{solves.team.name}}</td>
                        <td>{{solves.timestamp | moment("dddd, MMMM Do YYYY, h:mm:ss a") }}</td>
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
import { api } from '@/utils/api'

export default {
  name: 'Statistic',
  data () {
    return {
        loading  : true,
        challenge: "",
        solves: []
    }
  },
  methods: {
      
  },
  beforeMount () {
    let that = this;
    api(`query{ statistic(category:"${this.$route.params.category}", points:${this.$route.params.points}){ id solvedchallengeSet{ timestamp, team{ id, name } } } }`).then(data => {
        that.solves = data.statistic.solvedchallengeSet;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>