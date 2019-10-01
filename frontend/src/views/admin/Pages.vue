<template>
  <div class="offset">
    <div v-if="loading">Yo, we loadin'. Hang tight</div>
    <div v-else>
      <div class="newOpt">
        <button class="btn btn-secondary" @click="$router.push({ name: 'AdminCreatePages'});">New Page</button>
      </div>
      <b-card header="Pages" header-tag="header">
        <table id="adminpages" class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>URL</th>
              <th style="text-align: right;">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="page in pages" v-bind:key="page.id">
              <td>{{page.id}}</td>
              <td>{{page.name}}</td>
              <td>{{page.url}}</td>
              <td>
                <div>
                  <!-- <RemoveChallenge :challenge="challenge" />
                  <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditChallenge', params: { challenge: challenge } }">Edit</router-link>-->
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
import AddPage from "@/components/admin/add/Page.vue";

export default {
  name: "Pages",
  components: { AddPage },
  data() {
    return {
      loading: true,
      pages: []
    };
  },
  created() {
    let self = this;
    api("query { pages{ id name url } }").then(data => {
      self.pages = data.pages;
      self.loading = false;
    });
  }
};
</script>