<template>
  <div style="padding:20px">
    <div v-if="challenge">
      <h3>Edit Challenge</h3>
      <label>Challenge name:</label>
      <input class="form-control" v-model="challenge.name" />
      <label>Challenge Description (html enabled):</label>
      <textarea class="form-control" rows="10" v-model="challenge.description"></textarea>
      <label>Challenge Points:</label>
      <input class="form-control" v-model="challenge.points" />
      <label>Challenge Flag:</label>
      <input class="form-control" v-model="challenge.flag" />
      <label>Challenge Category:</label>
      <select class="form-control" v-model="challenge.category.name">
        <option v-bind:default="challenge.category.name">{{challenge.category.name}}</option>
        <option value="None">None</option>
        <option v-for="category in categories" v-bind:value="category.name" v-bind:key="category.id">{{category.name}}</option>
      </select>
      <p>{{message}}</p>
      <button class="btn btn-secondary" @click="update()">Update Challenge</button>
    </div>
    <div v-else>Redirect.. You cannot access this page directly</div>
  </div>
</template>


<script>
import { api } from "@/utils/api";
import RemoveChallenge from "@/components/admin/remove/challenge.vue";

export default {
  name: "AdminChallenge",
  props: ["challenge"],
  components: {
    RemoveChallenge
  },
  data() {
    return {
      loading: true,
      categories: [],
      message: ""
    };
  },
  beforeMount() {
    let that = this;
    api("query { categories{ name } }").then(data => {
      that.categories = data.categories;
    });
  },
  methods: {
    update() {
      var re = new RegExp("\n", "g");
      var str = this.challenge.description.replace(re, "\\n");
      let that = this;
      api(
        `mutation { updateChallenge(id:${this.challenge.id}, name:"${this.challenge.name}", description:"${str}", points:${this.challenge.points}, flag:"${this.challenge.flag}", show:false, category:"${this.challenge.category.name}"){ message} }`
      ).then(data => {
        that.message = data.updateChallenge.message;
      });
    }
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