<template>
  <div>
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
        <tr
          v-for="(team, index) in this.$store.getters['teams/ranks']"
          :key="team.id"
          style="cursor: pointer;"
          @click="$router.push(`/team/${team.name}`);"
        >
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
export default {
  name: "Scoreboard",
  beforeMount() {
    this.$store.dispatch("teams/loadTeams");
  }
};
</script>

<style scoped>
</style>