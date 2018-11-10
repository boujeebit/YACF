<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <div v-for="category in categories" v-bind:key="category.id">
                {{category.name}} 
                <p>Challenges: {{category.challenges}}</p>
                <hr>
            </div>
        </div>
    
    </div>
</template>


<script>
import axios from 'axios'

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
    axios
    .post('http://127.0.0.1:8000/graphql/', {
        'query': 
        `query {
            allCategories{
                id
                name
                description
                challenges {
                    id
                }
            }
        }` 
    })
    .then(r => r.data.data.allCategories)
    .then(allCategories => {
        console.log(allCategories);
        that.categories = allCategories;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>