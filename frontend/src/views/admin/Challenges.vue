<template>
  <div class="offset">
    <div v-if="loading">Yo, we loadin'. Hang tight</div>
    <div v-else>
      <div class="newOpt">
        <button class="btn btn-secondary" @click="showNew = !showNew">New Challenge</button>
      </div>
      <div v-if="showNew">
        <b-card header="New Challenge" header-tag="header">
          <AddChallenge />
        </b-card>
        <hr />
      </div>
      <b-card header="Challenge" header-tag="header">
        <table id="adminchallenge" class="table">
          <thead>
            <tr>
              <th>Challenge</th>
              <th>Description</th>
              <th>Points</th>
              <th style="text-align: right;">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="challenge in challenges" v-bind:key="challenge.id">
              <td>{{challenge.name}}</td>
              <td>{{challenge.description}}</td>
              <td>{{challenge.points}}</td>
              <td>
                <div>
                  <RemoveChallenge :challenge="challenge" />
                  <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditChallenge', params: { challenge: challenge } }">Edit</router-link>
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
import AddChallenge from "@/components/admin/add/challenge.vue";
import RemoveChallenge from "@/components/admin/remove/challenge.vue";

export default {
  name: "AdminChallenge",
  components: { AddChallenge, RemoveChallenge },
  data() {
    return {
      loading: true,
      showNew: false,
      challenges: []
    };
  },
  beforeMount() {
    let that = this;
    api(
      "query { challenges{ id, name, description, points, category { id, name } } }"
    ).then(data => {
      that.challenges = data.challenges;
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