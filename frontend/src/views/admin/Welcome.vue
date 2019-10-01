<template>
  <div style="padding:20px">
    <!-- <h3>Configure Welcome</h3> -->

    <div>
      <b-card header="Welcome Page" header-tag="header">
        <b-tabs content-class="mt-3">
          <b-tab title="Configure" active>
            <MonacoEditor height="500" theme="vs" language="html" :options="options" @change="onChange" v-model="content"></MonacoEditor>
            <span>(html enabled)</span>
            <hr />
            <button class="btn btn-secondary" style="margin-top: 10px;" @click="addWelcome()">Submit</button>
          </b-tab>
          <b-tab title="Preview">
            <span v-html="content"></span>
          </b-tab>
        </b-tabs>
      </b-card>
    </div>
    <p>{{status}}</p>
  </div>
</template>

<script>
import MonacoEditor from "monaco-editor-vue";
import { api } from "@/utils/api.js";

export default {
  name: "",
  components: {
    MonacoEditor
  },
  data() {
    return {
      content: "",
      status: "",
      options: {
        //Monaco Editor Options
      }
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