<template>
    <div style="padding:20px">
        <h3>Add Challenge</h3>
        <label>Challenge name:</label>
        <input class="form-control" v-model="name">
        <label>Challenge Description:</label>
        <textarea class="form-control" v-model="description"></textarea>
        <label>Challenge Points:</label>
        <input class="form-control" v-model="points">
        <label>Challenge Flag:</label>
        <input class="form-control" v-model="flag">
        <label>Challenge Category:</label>
        <select class="form-control" v-model="category">
            <option value="None" v-bind:default="true">None</option>
            <option v-for="category in categories" v-bind:value="category.name" v-bind:key="category.id">{{category.name}}</option>
        </select>
        <p>{{message}}</p>
        <button class="btn btn-secondary" @click="addChallenge()">Add Challenge</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AddCategory',
  data () {
    return {
        categories: [],
        name: "",
        description: "",
        points: "",
        flag: "",
        category: "",
        message: ""
    }
  },
  beforeMount () {
        let that = this;
        axios
        .post('http://127.0.0.1:8000/graphql/', {
            'query': 
            `query {
                allCategories{
                    name
                }
            }` 
        })
        .then(r => r.data.data.allCategories)
        .then(allCategories => {
            console.log(allCategories);
            that.categories = allCategories;
        })
  },
  methods: {

    addChallenge (){
        let query = "";
        console.log("Adding Challenge", this.name, this.description, this.points, this.category)

        if (this.category == "None" || this.category == ""){
            console.log("No category selected", this.category);
            query = 
            `mutation{
                addChallenge(name:"${this.name}", description:"${this.description}", points:${this.points}, flag:"${this.flag}", show:true) {
                    message
                }
            }` 
        } else {
            console.log("Category selected")
            query = 
            `mutation{
                addChallenge(name:"${this.name}", description:"${this.description}", points:${this.points}, flag:"${this.flag}", show:true, category:"${this.category}") {
                    message
                }
            }` 
        }

        let that = this;
        axios
        .post('http://127.0.0.1:8000/graphql/', {
            'query': 
            query
        })
        .then(r => r.data.data.addChallenge)
        .then(addChallenge => {
            console.log(addChallenge);
            if (addChallenge.message == "success") {
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