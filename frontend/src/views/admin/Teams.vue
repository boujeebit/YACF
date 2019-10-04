<template>
  <div class="offset">
    <div v-if="loading">Yo, we loadin'. Hang tight</div>
    <div v-else>
      <div class="newOpt">
        <button class="btn btn-secondary" @click="showNew = !showNew">New Team</button>
      </div>
      <div v-if="showNew">
        <b-card header="New Challenge" header-tag="header">
          <AddTeam />
        </b-card>
        <hr />
      </div>
      <b-card header="Teams" header-tag="header">
        <table id="adminteams" class="table">
          <thead>
            <tr>
              <th>Team</th>
              <th>Affiliation</th>
              <th>Website</th>
              <th>Admin Email</th>
              <th>Number of Members</th>
              <th style="text-align: right;">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="team in teams" v-bind:key="team.id">
              <td>{{team.name}}</td>
              <td>{{team.affiliation}}</td>
              <td>{{team.website}}</td>
              <td>{{team.email}}</td>
              <td>{{team.members}}</td>
              <td>
                <div>
                  <RemoveTeam :team="team" />
                  <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditTeam', params: { team: team } }">Edit</router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-card>
    </div>
  </div>
</template>


<script>
import { api } from "@/utils/api";
import AddTeam from "@/components/admin/add/team.vue";
import RemoveTeam from "@/components/admin/remove/team.vue";

export default {
  name: "AdminTeam",
  components: {
    AddTeam,
    RemoveTeam
  },
  data() {
    return {
      loading: true,
      showNew: false,
      teams: []
    };
  },
  methods: {
    _child_Remove(value) {
      console.log("here", value);
    }
  },
  beforeMount() {
    let that = this;
    api(
      "query { teams{ id, name, affiliation, website, email, points, members, wrongFlags, correctFlags } }"
    ).then(data => {
      that.teams = data.teams;
      that.loading = false;
    });
  }
};
</script>

<style scoped>
.secret {
  color: white;
}
.secret:hover {
  color: black;
}
</style>