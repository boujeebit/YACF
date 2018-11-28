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
                        <td class="secret">{{challenge.flag}}</td>
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
  name: 'AdminChallenge',
  data () {
    return {
        loading: true,
        challenges: []
    }
  },
  beforeMount () {
    let that = this;
    api('query { allChallenges{ id, name, description, points, flag, category { id, name } } }').then(data => {
        that.challenges = data.allChallenges;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
.secret {
    color: white;
}
.secret:hover {
    color: black;
}
</style>