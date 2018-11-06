<template>
  <div>
      <div style="padding:20px">
        <h3>Add Category</h3>
        <label>Category name:</label>
        <input class="form-control">
        <label>Category Description:</label>
        <input class="form-control">
      </div>
      <hr>
      <div style="padding:20px">
        <h3>Add Challenge</h3>
        <label>Challenge name:</label>
        <input class="form-control">
        <label>Challenge Description:</label>
        <input class="form-control">
        <label>Challenge Points:</label>
        <input class="form-control">
        <label>Challenge Category:</label>
        <input class="form-control">
      </div>
      <hr>
      <div style="padding:20px">
        <h3>Add Team</h3>
        <label>Team name:</label>
        <input class="form-control">
      </div>
      <hr>
  </div>
</template>

<script>
// @ is an alias to /src
// import Challenges from '@/components/Challenges.vue'

export default {
  name: 'home',
//   components: {
//     Challenges
//   }
}
</script>
