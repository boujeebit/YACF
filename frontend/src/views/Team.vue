<template>
  <div>
    <h3 style="text-align:center; padding-top: 10px;">{{this.$route.params.name}}</h3>


        <table id="team" class="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Challenge</th>
              <th>Points</th>
              <th>Solved At</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(solve, index) in this.$store.getters.solved" :key="solve.id" style="cursor: pointer;">
                <td>{{index+1}}</td>
                <td>{{solve.challenge.name}}</td>
                <td>{{solve.challenge.points}}</td>
                <td>{{solve.timestamp}}</td>
            </tr>
          </tbody>
        </table>

  </div>
</template>

<script>
// @ is an alias to /src
// import Challenges from '@/components/Challenges.vue'

export default {
  name: 'team',
//   components: {
//     Challenges
//   }
  methods: {
      
  },
  beforeMount () {
    this.$store.dispatch('loadStats', this.$route.params.name);
  }
}
</script>