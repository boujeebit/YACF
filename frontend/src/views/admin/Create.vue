<template>
  <div>
    <AddCategory/>
    <hr>
    <AddChallenge/>
    <hr>
    <AddTeam/>
    <hr>
  </div>
</template>

<script>
import AddCategory from '@/components/admin/add/category.vue'
import AddChallenge from '@/components/admin/add/challenge.vue'
import AddTeam from '@/components/admin/add/team.vue'

export default {
  name: 'home',
  components: {
    AddCategory,
    AddChallenge,
    AddTeam
  }
}
</script>
