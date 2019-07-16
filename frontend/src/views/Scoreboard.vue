<template>
  <div style="padding:15px;">
    <Graph />
    <div v-if="!this.$store.getters['user/isAdmin']">
      <TeamPlacement />
    </div>
    <Scoreboard />
  </div>
</template>

<script>
export default {
  name: "scoreboard",
  components: {
    Graph: () => import("@/components/scoreboard/Graph"),
    TeamPlacement: () => import("@/components/scoreboard/TeamPlacement"),
    Scoreboard: () => import("@/components/scoreboard/Scoreboard")
  }
};
</script>