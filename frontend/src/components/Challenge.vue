<template>
  <div>
    <!-- Modal Component -->
    <b-modal v-bind:id="chal.id" v-bind:title="chal.name" ok-title="Submit Flag" ok-variant="secondary" @shown="loaddata" @ok="handleOk">
      <div v-if="loading">Challenge details are loading, please hold!</div>
      <div v-else>
        <span v-html="challenge.description"></span>

        <div v-if="enter">
          <p>Congrats, you solved the challenge! On to the next one!</p>
        </div>
        <div v-else>
          <b-form-group id="flaggroup" label-for="chad.id" description="Flags are not case sensitive">
            <b-form-input id="chad.id" type="text" required placeholder="Enter Flag" v-model="flag"></b-form-input>
          </b-form-group>
          <p>{{message}}</p>
        </div>
      </div>
      <p class="stats" @click="$router.push(`/challenge/${categoryInLowerCase}/${challenge.points}`);">View Stats</p>
    </b-modal>
  </div>
</template>

<script>
import { api } from "@/utils/api.js";

export default {
  name: "Challenges",
  props: ["chal", "enter"],
  data() {
    return {
      loading: true,
      challenge: "",

      solved: false,
      message: ""
    };
  },
  computed: {
    categoryInLowerCase() {
      return this.challenge.category.name.toLowerCase().trim();
    }
  },
  methods: {
    handleOk(evt) {
      console.log("Here is the flag enter: ", this.flag);
      evt.preventDefault();

      let that = this;
      api(
        `mutation{ submitflag(challenge:${this.chal.id}, flag:"${this.flag}"){ code } }`
      ).then(data => {
        console.log("FLAG:", data.submitflag);
        if (data.submitflag.code === 1) {
          that.message = "You solved it!"; //Should get this from the backend
          that.$store.commit("SET_USER_SOLVE", that.chal.id);
        } else {
          that.message = "That's not it! Try again.";
        }
      });
    },
    loaddata() {
      let that = this;
      api(
        `query{ challenge(id:${this.chal.id}){ id, description, points, category { name } } }`
      ).then(data => {
        that.challenge = data.challenge;
        that.loading = false;
      });
    }
  }
};
</script>

<style scoped>
.stats {
  color: black;
  text-align: center;
  cursor: pointer;
  margin-bottom: 0;
}
.stats:hover {
  text-decoration: underline;
}
</style>