<template>
  <div class="offset">
    <v-jsoneditor v-model="yaml" :plus="false" height="600px" @error="onError" />
  </div>
</template>

<script>
import VJsoneditor from "v-jsoneditor";

export default {
  name: "Scripter",
  components: {
    VJsoneditor
  },
  data() {
    return {
      yaml: {
        org: "YACF",
        categories: [
          {
            name: "recon",
            challenges: [
              {
                name: "Recon 100",
                description: "This is recon 100",
                hint: "Google me",
                points: 100
              },
              {
                name: "Recon 200",
                description: "This is recon 200",
                hint: "Bing me",
                points: 200
              }
            ]
          },
          {
            name: "Reversing",
            challenges: [
              {
                name: "Reversing 100",
                description: "This is reversing 100",
                hint: "Look at the headers",
                points: 100
              }
            ]
          }
        ]
      }
    };
  },
  methods: {
    checker() {
      console.log(this.yaml);
    },
    onError() {
      console.log("error");
    }
  }
};
</script>