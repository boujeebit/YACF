<template>
    <div>
        <sgraph />

        <hr>
        <h3>Teams</h3>
        <table id="socreboard" class="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team name</th>
              <th>Correct Flags</th>
              <th>Wrong Flags</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(team, index) in this.$store.getters['teams/ranks']" :key="team.id" style="cursor: pointer;" @click="$router.push(`/team/${team.name}`);">
                <td>{{index+1}}</td>
                <td>{{team.name}}</td>
                <td>{{team.correctFlags}}</td>
                <td>{{team.wrongFlags}}</td>
                <td>{{team.points}}</td>
            </tr>
          </tbody>
        </table>
        
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import sgraph from './sgraph.vue'
import axios from 'axios'

export default {
  name: 'scoreboard',
  data () {
    return {
      graphloading: true,
      graphlabels: [],
      graphdata: [],
    }
  },
  beforeMount () {
    this.$store.dispatch('teams/loadTeams');
    this.$store.dispatch('connectScoreboard');


    let that = this;
    axios({
      method: 'post',
      url: 'http://localhost:8000/graphql/',
      withCredentials: true,
      data: {
          'query': 'mutation{ graph{ timeline, message } }'
      }
    })
    .then(r => r.data.data.graph)
    .then(graph => {
        console.log(graph.timeline);
        that.$store.commit('SET_GRAPH', {'data': JSON.parse(graph.message), 'labels': JSON.parse(graph.timeline)})
        console.log(JSON.parse(graph.message));
        // that.graphdata   = JSON.parse(graph.message);
        // that.graphlabels = JSON.parse(graph.timeline);
        that.graphloading = false;

        // console.log(JSON.parse(graph.message));
    });

  },
  components: {
    sgraph
  }
}
</script>

<style scoped>
.header {
  text-align: left;
  margin: 10px 0 20px 10px;
  font-family: "Marker Felt";
}
</style>