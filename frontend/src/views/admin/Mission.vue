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
        <h1>{{solves.length}}</h1>
      </b-card>
    </b-card-group>

    <hr />
    <b-card header="Progress Graph">
      <Graph />
    </b-card>
    <hr />
    <b-card-group deck>
      <b-card header="Solves">
        <b-alert variant="success" v-for="solve in solves" :key="solve.id" show>({{solve.id}}) {{solve.team.name}} - {{solve.challenge.name}} - {{solve.timestamp}}</b-alert>
      </b-card>
      <b-card header="Failures">
        <b-alert variant="danger" v-for="failure in failures" :key="failure.id" show>({{failure.id}}) {{failure.team.name}} - {{failure.challenge.name}} - {{failure.timestamp}}</b-alert>
      </b-card>
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
      solves: 0,
      failures: []
    };
  },
  created() {
    let self = this;
    api("query { challenges{ id } }").then(data => {
      self.challenges = data.challenges.length;
    });
    api("query { teams{ id } }").then(data => {
      self.teams = data.teams.length;
    });
    api("query { users{ id } }").then(data => {
      self.users = data.users.length;
    });
    api(
      "query { solves { id team { name } challenge { name } timestamp } }"
    ).then(data => {
      self.solves = data.solves;
    });
    api(
      "query { failures { id team { name } challenge { name } timestamp } }"
    ).then(data => {
      self.failures = data.failures;
    });
  },
  methods: {}
};
</script>

<style scoped>
</style>