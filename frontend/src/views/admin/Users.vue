<template>
  <div class="offset">
    <div v-if="loading">Yo, we loadin'. Hang tight</div>
    <div v-else>
      <b-card header="Users" header-tag="header">
        <table id="adminteams" class="table">
          <thead>
            <tr>
              <th>Username</th>
              <th>Firstname</th>
              <th>Lastname</th>
              <th>Email</th>
              <th>Team</th>
              <th>Privilege</th>
              <th style="text-align: right;">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" v-bind:key="user.id">
              <td>{{user.username}}</td>
              <td>{{user.firstName}}</td>
              <td>{{user.lastName}}</td>
              <td>{{user.email}}</td>
              <td v-if="user.profile.team">{{user.profile.team.name}}</td>
              <td v-else>
                <b-badge variant="warning">No Team</b-badge>
              </td>
              <td>
                <b-badge v-if="user.isSuperuser" variant="danger">Superuser</b-badge>
              </td>
              <td>
                <div>
                  <!-- <RemoveTeam :team="team"/> -->
                  <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{}">Edit</router-link>
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
import { api } from "@/utils/api.js";

export default {
  name: "",
  data() {
    return {
      loading: true,
      users: []
    };
  },
  beforeMount() {
    let self = this;
    api(
      "query { users{ id username firstName lastName email isSuperuser profile { team { name } } } }"
    ).then(data => {
      self.users = data.users;
      self.loading = false;
    });
  },
  methods: {}
};
</script>

<style scoped>
</style>