<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="admincategories" class="table table-hover">
                <thead>
                    <tr>
                    <th>Category</th>
                    <th>Description</th>
                    <th>Number of Challenges</th>
                    <th>Edit/Remove (Not working)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="category in categories" v-bind:key="category.id">
                        <td>{{category.name}}</td>
                        <td>{{category.description}}</td>
                        <td>Blah</td>
                        <td>Edit | Remove</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>


<script>
import { api } from '@/utils/api'

export default {
  name: 'AdminCategory',
  data () {
    return {
        loading: true,
        categories: []
    }
  },
  methods: {
      
  },
  beforeMount () {
    let that = this;
    api('query { allCategories{ id, name, description, challenges { id } } }').then(data => {
        that.categories = data.allCategories;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>