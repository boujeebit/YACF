<template>
  <div>
    <span :key="$route.params.url" v-html="content"></span>
  </div>
</template>

<script>
import { api } from "@/utils/api";
export default {
  name: "Page",
  data() {
    return {
      content: ""
    };
  },
  watch: {
    "$route.params.url"() {
      this.get_page();
    }
  },
  created() {
    this.get_page();
  },
  methods: {
    get_page() {
      let self = this;
      api(`query{ page(url:"${this.$route.params.url}"){ id content } }`).then(
        data => {
          self.content = data.page.content;
        }
      );
    }
  }
};
</script>