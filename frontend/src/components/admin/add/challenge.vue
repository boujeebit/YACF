<template>
  <div>
    <h3>Add Challenge</h3>
    <label>Challenge name:</label>
    <input class="form-control" v-model="name" />
    <label>Challenge Description (html enabled):</label>
    <textarea class="form-control" v-model="description"></textarea>
    <label>Challenge Points:</label>
    <input class="form-control" v-model="points" />
    <label>Challenge Flag:</label>
    <input class="form-control" v-model="flag" />
    <label>Challenge Category:</label>
    <select class="form-control" v-model="category">
      <option value="None" v-bind:default="true">None</option>
      <option v-for="category in categories" v-bind:value="category.name" v-bind:key="category.id">{{category.name}}</option>
    </select>
    <p>{{message}}</p>
    <button class="btn btn-secondary" @click="addChallenge()">Add Challenge</button>
  </div>
</template>

<script>
import { api } from "@/utils/api";

export default {
  name: "AddCategory",
  data() {
    return {
      categories: [],
      name: "",
      description: "",
      points: "",
      flag: "",
      category: "",
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
    addChallenge() {
      var query = "";
      if (this.category == "None" || this.category == "") {
        query = `mutation{ addChallenge(name:"${this.name}", description:"${this.description}", points:${this.points}, flag:"${this.flag}", show:true) { message } }`;
      } else {
        query = `mutation{ addChallenge(name:"${this.name}", description:"${this.description}", points:${this.points}, flag:"${this.flag}", show:true, category:"${this.category}") { message } }`;
      }

      let that = this;
      api(query).then(data => {
        that.message = data.addChallenge.message;
      });
    }
  }
};
</script>

<style scoped>
</style>