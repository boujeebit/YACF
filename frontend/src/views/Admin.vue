<template>
  <div>
    <AdminNav/>

    <router-view></router-view>
    <!-- <AddCategory/>
    <hr>
    <AddChallenge/>
    <hr>
    <AddTeam/>
    <hr> -->
  </div>
</template>

<script>
import AdminNav from '@/components/admin/adminnav.vue'

import AddCategory from '@/components/admin/add/category.vue'
import AddChallenge from '@/components/admin/add/challenge.vue'
import AddTeam from '@/components/admin/add/team.vue'

export default {
  name: 'home',
  components: {
    AdminNav,
    AddCategory,
    AddChallenge,
    AddTeam
  }
}
</script>
