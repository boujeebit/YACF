<template>
  <div class="home">
    <Challenges msg="Welcome to Your Vue.js App"/>
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
