<template>
  <div class="offset">
    <b-card-group deck>
      <b-card title="Teams">
        <h1>{{teams}}</h1>
      </b-card>
      <b-card title="Users">
        <h1>{{users}}</h1>
      </b-card>
      <b-card title="Challenges">
        <h1>{{challenges}}</h1>
      </b-card>
      <b-card title="Solves">
        <h1>{{solves}}</h1>
      </b-card>
    </b-card-group>

    <hr />
    <b-card header="Progress Graph">
      <Graph />
    </b-card>
    <hr />
    <b-card-group deck>
      <b-card header="Submissions"></b-card>
      <b-card header="Fails"></b-card>
    </b-card-group>
  </div>
</template>


<script>
import { api } from "@/utils/api";

export default {
  name: "MissionControl",
  components: {
    Graph: () => import("@/components/scoreboard/Graph")
  },
  data() {
    return {
      challenges: 0,
      teams: 0,
      users: 0,
      solves: 0
    };
  },
  created() {
    let self = this;
    api("query { challenges{ id } }").then(data => {
      self.challenges = data.challenges.length;
    });
    api("query { allTeams{ id } }").then(data => {
      self.teams = data.allTeams.length;
    });
    api("query { allUsers{ id } }").then(data => {
      self.users = data.allUsers.length;
    });
    api("query { allSolves{ id } }").then(data => {
      self.solves = data.allSolves.length;
    });
  },
  methods: {}
};
</script>

<style scoped>
</style>