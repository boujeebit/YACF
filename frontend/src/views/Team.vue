<template>
  <div style="padding: 15px;">
    <h3 style="padding-top: 10px;">{{this.$store.state.teams.team.name}}</h3>
    <hr />
    <graph :name="this.$route.params.name" />
    <div>--{{this.$store.state.teams.team.players}}</div>
    <div style="margin: 20px;">
      <table id="team" class="table table-hover">
        <thead>
          <tr>
            <th>Order</th>
            <th>Challenge</th>
            <th>Points</th>
            <th>Solved At</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(solve, index) in this.$store.getters['teams/GET_TEAM_SOLVE']"
            :key="solve.id"
            style="cursor: pointer;"
            @click="$router.push(`/challenge/${solve.challenge.category.name}/${solve.challenge.points}`);"
          >
            <td>{{index+1}}</td>
            <td>{{solve.challenge.name}}</td>
            <td>{{solve.challenge.points}}</td>
            <td>{{solve.timestamp | moment("dd, MM Do YYYY, h:mm:ss a") }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "team",
  beforeMount() {
    this.$store.dispatch("teams/loadStats", this.$route.params.name);
  },
  components: {
    Graph: () => import("@/components/team/Graph")
  }
};
</script>