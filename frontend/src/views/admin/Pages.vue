<template>
  <div class="offset">{{pages}}</div>
</template>

<script>
import { api } from "@/utils/api";

export default {
  name: "Pages",
  data() {
    return {
      pages: []
    };
  },
  created() {
    let self = this;
    api("query { pages{ id name content } }").then(data => {
      self.pages = data.pages;
    });
  }
};
</script>