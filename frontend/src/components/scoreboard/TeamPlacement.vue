<template>
  <div>
    <h3>Your Ranks</h3>
    <hr />
    <table id="socreboard" class="table table-hover">
      <thead>
        <tr>
          <th>ID (Needs Rank)</th>
          <th>Team name</th>
          <th>Correct Flags</th>
          <th>Wrong Flags</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        <tr style="cursor: pointer;" @click="$router.push(`/team/${team.name}`);">
          <td>{{team.id}}</td>
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
import { mapGetters } from "vuex";

export default {
  name: "TeamPlacement",
  computed: {
    ...mapGetters({
      team: "teams/GET_TEAM_RANK"
    })
  },
  beforeMount() {
    this.$store.dispatch("teams/LoadTeamRank");
  }
};
</script>

<style>
</style>
