<template>
    <div style="padding:20px">
        <h3>Add Category</h3>
        <label>Category name:</label>
        <input class="form-control" v-model="name">
        <label>Category Description:</label>
        <input class="form-control" v-model="description">
        <p>{{message}}</p>
        <button class="btn btn-secondary" @click="addCategory()">Add Category</button>
    </div>
</template>

<script>
import { api } from '@/utils/api'

export default {
  name: 'AddChallenge',
  data () {
    return {
        name: "",
        description: "",
        message: ""
    }
  },
  methods: {
    addCategory (){
        let that = this;
        api(`mutation{ addcategory(name:"${this.name}",description:"${this.description}") { message } }`).then(data => {
            data.addcategory.message ? that.message = "Category added successfully" : that.message = "Failed to add category"
        })
    },
  }
}
</script>

<style scoped>
</style>