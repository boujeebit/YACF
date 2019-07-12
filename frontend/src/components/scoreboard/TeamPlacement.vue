<template>
  <div style="padding-top:20px;">
    <h3>Your Ranks</h3>
    <hr />
    <table id="socreboard" class="table table-hover">
      <thead>
        <tr>
          <th>ID</th>
          <th>Team name</th>
          <th>Correct Flags</th>
          <th>Wrong Flags</th>
          <th>Score</th>
          <th>Progress</th>
        </tr>
      </thead>
      <tbody>
        <tr style="cursor: pointer;" @click="$router.push(`/team/${team.name}`);">
          <td>{{team.id}}</td>
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
  name: "TeamPlacement",
  computed: {
    ...mapGetters({
      team: "teams/GET_TEAM_RANK",
      max: "teams/GET_MAX_POINTS"
    })
  },
  beforeMount() {
    this.$store.dispatch("teams/LoadTeamRank");
  }
};
</script>

<style>
</style>
