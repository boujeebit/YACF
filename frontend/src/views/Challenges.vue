<template>
  <div class="home">
    <Challenges/>
  </div>
</template>

<script>
// @ is an alias to /src
import Challenges from '@/components/Challenges.vue'

export default {
  name: 'home',
  components: {
    Challenges
  }
}
</script>
