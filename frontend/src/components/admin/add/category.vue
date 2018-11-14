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
import axios from 'axios'

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
    console.log("Adding Category", this.name, this.description)

    let that = this;
    axios
    .post('http://localhost:8000/graphql/', {
        'query': 
        `mutation{
            addcategory(name:"${this.name}",description:"${this.description}") {
                message
            }
        }` 
    })
    .then(r => r.data.data.addcategory)
    .then(addcategory => {
        console.log(addcategory);
        if (addcategory.message == "success") {
            that.message = "Category added successfully"
        } else {
            that.message = "Failed to add category"
        }
    })




    },


  }
}
</script>

<style scoped>
</style>