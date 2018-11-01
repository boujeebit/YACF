<template>
  <div class="hello">
    <h2 class="header">Challenge Board</h2>
    <div v-for="cat in this.$store.state.board" :key="cat.id">
      <h3>{{cat.name}}</h3>
      <div class="flex-container">
        <div class="flex-container-div" v-for="chal in cat.challenges" :key="chal.id">
          <h3>{{chal.name}}</h3>
          <p>{{chal.points}}</p>
        </div>
      </div>
      <hr>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Challenges',
  mounted () {
    // this.$store.dispatch('loadCategories');
    // this.$store.dispatch('loadChallenges');
    this.$store.dispatch('loadChallengeBoard');
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
}

.flex-container-div {
  background-color: #f5f5f5;
  box-shadow: 4px 3px #eaeaea;
  width: 300px;
  margin: 10px;
  text-align: center;
  padding: 15px 0 15px 0;
  /* line-height: 75px; */
  /* font-size: 30px; */
}

</style>
