<template>
  <div style="padding:20px">
    <h3>Configure Welcome</h3>

    <p>{{status}}</p>
    <label>Welcome page (html enabled):</label>
    <textarea class="form-control" v-model="content" v-bind:rows="20"></textarea>

    <button class="btn btn-secondary" style="margin-top: 10px;" @click="addWelcome()">Submit</button>
  </div>
</template>

<script>
import { api } from "@/utils/api.js";

export default {
  name: "",
  data() {
    return {
      content: "",
      status: ""
    };
  },
  beforeMount() {
    let that = this;
    api("query{ welcomePage{ content } }").then(data => {
      that.content = decodeURIComponent(escape(atob(data.welcomePage.content)));
    });
  },
  methods: {
    addWelcome() {
      console.log("Adding welcome");
      let self = this;

      api(
        `mutation{ welcome(content:"${btoa(
          unescape(encodeURIComponent(this.content))
        )}"){ status } }`
      ).then(data => {
        self.status = data.welcome.status;
      });
    }
  }
};
</script>

<style scoped>
</style>