<template>
    <div style="margin: 15px;">
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="adminteams" class="table">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Affiliation</th>
                        <th>Admin Email</th>
                        <th>Access Code (Hover)</th>
                        <th style="text-align: right;">Edit/Remove (Not working)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="team in teams" v-bind:key="team.id">
                        <td>{{team.name}}</td>
                        <td>{{team.affiliation}}</td>
                        <td>{{team.email}}</td>
                        <td class="secret">{{team.accesscode}}</td>
                        <td style="text-align: right;">
                            <button class="btn btn-sm btn-secondary">Edit</button> 
                            <button class="btn btn-sm btn-danger" style="margin-left: 5px;">Remove</button>
                        </td>
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
    api('query { allTeams{ id, name, affiliation, email, points, wrongFlags, correctFlags, accesscode } }').then(data => {
        that.teams = data.allTeams;
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