<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <div v-for="challenge in challenges" v-bind:key="challenge.id">
                {{challenge.name}} 
                <p>Category: {{challenge.category}}</p>
                <hr>
            </div>
        </div>
    
    </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'AdminChallenge',
  data () {
    return {
        loading: true,
        challenges: []
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
            allChallenges{
                id
                name
                points
                category {
                    id
                    name
                }
            }
        }` 
    })
    .then(r => r.data.data.allChallenges)
    .then(allChallenges => {
        console.log(allChallenges);
        that.challenges = allChallenges;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>