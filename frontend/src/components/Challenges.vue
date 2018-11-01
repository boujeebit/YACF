<template>
  <div class="hello">
    <h3>Categories are shown below</h3>
    <div v-for="cat in this.$store.state.board" :key="cat.id">
      <h3>{{cat.name}}</h3>
      <div class="flex-container">
        <div class="flex-container-div" v-for="chal in cat.challenges" :key="chal.id">
          <h3>{{chal.name}}</h3>
          <p>{{chal.points}}</p>
        </div>
      </div>
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
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
  background-color: DodgerBlue;
  margin-bottom: 20px;
}

.flex-container-div {
  background-color: #f1f1f1;
  width: 300px;
  margin: 10px;
  text-align: center;
  /* line-height: 75px; */
  /* font-size: 30px; */
}
</style>
