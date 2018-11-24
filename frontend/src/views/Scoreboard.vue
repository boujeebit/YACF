<template>
  <div style="padding: 15px;">
    <Scoreboard/>
  </div>
</template>

<script>
// @ is an alias to /src
import Scoreboard from '@/components/Scoreboard.vue'

export default {
  name: 'scoreboard',
  components: {
    Scoreboard
  }
}
</script>