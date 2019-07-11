<template>
  <div style="padding: 15px;">
    <span v-html="content"></span>
  </div>
</template>

<script>
import { api } from "@/utils/api.js";
export default {
  name: "home",
  data() {
    return {
      loading: true,
      content: ""
    };
  },
  beforeMount() {
    let that = this;
    api("query{ welcomePage{ content } }").then(data => {
      // that.content = data.welcomePage.content;
      that.content = "boom";
      that.loading = false;
    });
  }
};
</script>
