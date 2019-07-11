<template>
  <!-- <div style="padding: 15px;">
    <Challenges/>
  </div>-->

  <div v-if="this.$store.getters['user/userteam']">
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
  <div v-else>You are not apart of a team</div>
</template>

<script>
// import Challenges from "@/components/Challenges.vue";
import Challenge from "@/components/Challenge.vue";

export default {
  name: "home",
  components: {
    Challenge
  },
  mounted() {
    //TODO: Load this back into a component
    this.$store.dispatch("loadChallengeBoard");
  },
  methods: {
    isSoved(id) {
      return this.$store.state.solves.includes(id);
    }
  }
};
</script>


<style>
.header {
  text-align: left;
  margin: 10px 0 20px 10px;
  font-family: "Marker Felt";
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
  background-color: white;
  margin-bottom: 20px;
  justify-content: center;
}

.flex-container-div {
  background-color: #f5f5f5;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
  border-radius: 2px;
  width: 300px;
  margin: 10px;
  text-align: center;
  padding: 15px 0 15px 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

main {
  height: 100vh;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: auto;
}

main div {
  padding: 20px;
  overflow: auto;
}

/*!
 * Load Awesome v1.1.0 (http://github.danielcardoso.net/load-awesome/)
 * Copyright 2015 Daniel Cardoso <@DanielCardoso>
 * Licensed under MIT
 */
.la-ball-clip-rotate-multiple,
.la-ball-clip-rotate-multiple > div {
  position: relative;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
.la-ball-clip-rotate-multiple {
  display: block;
  font-size: 0;
  color: #fff;
}
.la-ball-clip-rotate-multiple.la-dark {
  color: #333;
}
.la-ball-clip-rotate-multiple > div {
  display: inline-block;
  float: none;
  background-color: currentColor;
  border: 0 solid currentColor;
}
.la-ball-clip-rotate-multiple {
  width: 32px;
  height: 32px;
}
.la-ball-clip-rotate-multiple > div {
  position: absolute;
  top: 50%;
  left: 50%;
  background: transparent;
  border-style: solid;
  border-width: 2px;
  border-radius: 100%;
  -webkit-animation: ball-clip-rotate-multiple-rotate 1s ease-in-out infinite;
  -moz-animation: ball-clip-rotate-multiple-rotate 1s ease-in-out infinite;
  -o-animation: ball-clip-rotate-multiple-rotate 1s ease-in-out infinite;
  animation: ball-clip-rotate-multiple-rotate 1s ease-in-out infinite;
}
.la-ball-clip-rotate-multiple > div:first-child {
  position: absolute;
  width: 32px;
  height: 32px;
  border-right-color: transparent;
  border-left-color: transparent;
}
.la-ball-clip-rotate-multiple > div:last-child {
  width: 16px;
  height: 16px;
  border-top-color: transparent;
  border-bottom-color: transparent;
  -webkit-animation-duration: 0.5s;
  -moz-animation-duration: 0.5s;
  -o-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-direction: reverse;
  -moz-animation-direction: reverse;
  -o-animation-direction: reverse;
  animation-direction: reverse;
}
.la-ball-clip-rotate-multiple.la-sm {
  width: 16px;
  height: 16px;
}
.la-ball-clip-rotate-multiple.la-sm > div {
  border-width: 1px;
}
.la-ball-clip-rotate-multiple.la-sm > div:first-child {
  width: 16px;
  height: 16px;
}
.la-ball-clip-rotate-multiple.la-sm > div:last-child {
  width: 8px;
  height: 8px;
}
.la-ball-clip-rotate-multiple.la-2x {
  width: 64px;
  height: 64px;
}
.la-ball-clip-rotate-multiple.la-2x > div {
  border-width: 4px;
}
.la-ball-clip-rotate-multiple.la-2x > div:first-child {
  width: 64px;
  height: 64px;
}
.la-ball-clip-rotate-multiple.la-2x > div:last-child {
  width: 32px;
  height: 32px;
}
.la-ball-clip-rotate-multiple.la-3x {
  width: 96px;
  height: 96px;
}
.la-ball-clip-rotate-multiple.la-3x > div {
  border-width: 6px;
}
.la-ball-clip-rotate-multiple.la-3x > div:first-child {
  width: 96px;
  height: 96px;
}
.la-ball-clip-rotate-multiple.la-3x > div:last-child {
  width: 48px;
  height: 48px;
}
/*
 * Animation
 */
@-webkit-keyframes ball-clip-rotate-multiple-rotate {
  0% {
    -webkit-transform: translate(-50%, -50%) rotate(0deg);
    transform: translate(-50%, -50%) rotate(0deg);
  }
  50% {
    -webkit-transform: translate(-50%, -50%) rotate(180deg);
    transform: translate(-50%, -50%) rotate(180deg);
  }
  100% {
    -webkit-transform: translate(-50%, -50%) rotate(360deg);
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
@-moz-keyframes ball-clip-rotate-multiple-rotate {
  0% {
    -moz-transform: translate(-50%, -50%) rotate(0deg);
    transform: translate(-50%, -50%) rotate(0deg);
  }
  50% {
    -moz-transform: translate(-50%, -50%) rotate(180deg);
    transform: translate(-50%, -50%) rotate(180deg);
  }
  100% {
    -moz-transform: translate(-50%, -50%) rotate(360deg);
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
@-o-keyframes ball-clip-rotate-multiple-rotate {
  0% {
    -o-transform: translate(-50%, -50%) rotate(0deg);
    transform: translate(-50%, -50%) rotate(0deg);
  }
  50% {
    -o-transform: translate(-50%, -50%) rotate(180deg);
    transform: translate(-50%, -50%) rotate(180deg);
  }
  100% {
    -o-transform: translate(-50%, -50%) rotate(360deg);
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
@keyframes ball-clip-rotate-multiple-rotate {
  0% {
    -webkit-transform: translate(-50%, -50%) rotate(0deg);
    -moz-transform: translate(-50%, -50%) rotate(0deg);
    -o-transform: translate(-50%, -50%) rotate(0deg);
    transform: translate(-50%, -50%) rotate(0deg);
  }
  50% {
    -webkit-transform: translate(-50%, -50%) rotate(180deg);
    -moz-transform: translate(-50%, -50%) rotate(180deg);
    -o-transform: translate(-50%, -50%) rotate(180deg);
    transform: translate(-50%, -50%) rotate(180deg);
  }
  100% {
    -webkit-transform: translate(-50%, -50%) rotate(360deg);
    -moz-transform: translate(-50%, -50%) rotate(360deg);
    -o-transform: translate(-50%, -50%) rotate(360deg);
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
