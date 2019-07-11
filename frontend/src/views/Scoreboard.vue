<template>
  <div>
    <Graph />
    <TeamPlacement />
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