<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="adminteams" class="table table-hover">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Access Code</th>
                        <th>Edit/Remove (Not working)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="team in teams" v-bind:key="team.id">
                        <td>{{team.name}}</td>
                        <td>{{team.accesscode}}</td>
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
  name: 'AdminTeam',
  data () {
    return {
        loading: true,
        teams: []
    }
  },
  methods: {
      
  },
  beforeMount () {
    let that = this;
    api('query { allTeams{ id, name, points, wrongFlags, correctFlags, accesscode } }').then(data => {
        that.teams = data.allTeams;
        that.loading = false;
    })
  }
}
</script>

<style scoped>
</style>