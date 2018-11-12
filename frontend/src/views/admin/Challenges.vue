<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="adminchallenge" class="table">
                <thead>
                    <tr>
                        <th>Challenge</th>
                        <th>Description</th>
                        <th>Points</th>
                        <th>Flag (Hover to show)</th>
                        <th>Edit/Remove (Not working)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="challenge in challenges" v-bind:key="challenge.id">
                        <td>{{challenge.name}}</td>
                        <td>{{challenge.description}}</td>
                        <td>{{challenge.points}}</td>
                        <td class="secret-flag">{{challenge.flag}}</td>
                        <td>Edit | Remove</td>
                    </tr>
                </tbody>
            </table>
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
                description
                points
                flag
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
.secret-flag {
    color: white;
}
.secret-flag:hover {
    color: black;
}
</style>