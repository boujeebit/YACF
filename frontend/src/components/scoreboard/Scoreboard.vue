<template>
  <div style="padding-top:20px;">
    <h3>Teams</h3>
    <table id="socreboard" class="table table-hover table-sm">
      <thead>
        <tr>
          <th>Rank</th>
          <th>Team name</th>
          <th>Correct Flags</th>
          <th>Wrong Flags</th>
          <th>Score</th>
          <th>Progress</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(team, index) in teams" :key="team.id" style="cursor: pointer;" @click="$router.push(`/team/${team.name}`);">
          <td>{{index+1}}</td>
          <td>{{team.name}}</td>
          <td>{{team.correctFlags}}</td>
          <td>{{team.wrongFlags}}</td>
          <td>{{team.points}}</td>
          <td>
            <b-progress class="mt-2" :max="max" height="4px">
              <b-progress-bar :value="team.points" variant="success"></b-progress-bar>
            </b-progress>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Scoreboard",
  computed: {
    ...mapGetters({
      teams: "teams/ranks",
      max: "teams/GET_MAX_POINTS"
    })
  },
  beforeMount() {
    this.$store.dispatch("teams/loadTeams");
  }
};
</script>

<style scoped>
</style>