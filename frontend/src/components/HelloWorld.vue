<template>
  <div class="hello">
    Categories...
    <div v-for="cat in this.$store.state.categories">
      {{cat.name}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },  
  data () {
    return {
      categories: []
    }
  },
  mounted () {
    this.$store.dispatch('loadCategories')
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
