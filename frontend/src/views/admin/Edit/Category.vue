<template>
    <div style="padding:20px">
        <div v-if="category">
            <h3>Edit Category</h3>
            <label>Category Name</label>
            <input class="form-control" v-model="category.name">
            <label>Description</label>
            <textarea rows="5" class="form-control" v-model="category.description"/>

            <p>{{message}}</p>
            <button class="btn btn-secondary" @click="update()">Update Category</button>
        </div>
        <div v-else>
            Redirect.. You cannot access this page directly
        </div>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Category',
  props: ['category'],
  data () {
    return {
      message: ""
    }
  },
  methods: {
      update() {
        let that = this;
        api(`mutation { updateCategory(id:${this.category.id}, name:"${this.category.name}", description:"${this.category.description}"){ message } }`).then(data => {
            that.message = data.updateCategory.message;
        })
      }
  }
}
</script>

<style scoped>
.stats {
  color: black;
  text-align: center;
  cursor: pointer;
  margin-bottom: 0;
}
.stats:hover {
  text-decoration: underline;
}
label {
    margin-top: 10px; 
    margin-bottom: 0px;
}
</style>