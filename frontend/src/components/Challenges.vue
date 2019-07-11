<template>
  <div>
    <transition name="fade">
      <div v-if="this.$store.state.board">
        <div v-for="cat in this.$store.state.board" :key="cat.id">
          <h3 style="text-align: center; margin-top: 15px;">{{cat.name}}</h3>
          <hr />
          <div class="flex-container">
            <div v-for="chal in cat.challenges" :key="chal.id">
              <div
                class="flex-container-div"
                v-b-modal="chal.id"
                style="cursor: pointer;"
                v-bind:style="[isSoved(chal.id) ? {'backgroundColor': '#448aff', 'color': 'white'} : {}]"
              >
                <h3>{{chal.name}}</h3>
                <p>{{chal.points}}</p>
                <!-- <p v-if="isSoved(chal.id)">Solved</p> -->
              </div>
              <Challenge :chal="chal" :enter="isSoved(chal.id) ? true : false"></Challenge>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <div v-if="!this.$store.state.board">
      <main>
        <div class="la-ball-clip-rotate-multiple la-dark la-3x">
          <div></div>
          <div></div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import Challenge from "@/components/Challenge.vue";

export default {
  name: "Challenges",
  components: {
    Challenge
  },
  mounted() {
    this.$store.dispatch("loadChallengeBoard");
  },
  methods: {
    isSoved(id) {
      return this.$store.state.solves.includes(id);
    }
  }
};
</script>

<style scoped>
</style>
