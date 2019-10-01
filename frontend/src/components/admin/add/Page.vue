<template>
  <div>
    <h3>Add Page</h3>
    <label>Page Name:</label>
    <input class="form-control" v-model="name" />
    <label>Page URL:</label>
    <input class="form-control" v-model="url" />
    <label>Page Content:</label>
    <MonacoEditor height="500" theme="vs" language="html" v-model="content" :options="options"></MonacoEditor>
    <p>{{message}}</p>
    <button class="btn btn-secondary" @click="addPage()">Add Page</button>
  </div>
</template>

<script>
import { api } from "@/utils/api";
import MonacoEditor from "monaco-editor-vue";

export default {
  name: "AddPage",
  components: { MonacoEditor },
  data() {
    return {
      name: "",
      url: "",
      content: "",
      message: "",
      options: {
        //Monaco Editor Options
      }
    };
  },
  methods: {
    addPage() {
      let that = this;
      api(
        `mutation { createpage(name:"${this.name}", url:"${this.url}", content:"${this.content}") { message } }`
      ).then(data => {
        data.createpage.message
          ? (that.message = "Page added successfully")
          : (that.message = "Failed to add page");
      });
    }
  }
};
</script>

<style scoped>
</style>