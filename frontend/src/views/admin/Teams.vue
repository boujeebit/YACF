<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="adminteams" class="table">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Affiliation</th>
                        <th>Website</th>
                        <th>Admin Email</th>
                        <th>Number of Members (Not working)</th>
                        <th>Access Code (Hover)</th>
                        <th style="text-align: right;">Options</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="team in teams" v-bind:key="team.id">
                        <td>{{team.name}}</td>
                        <td>{{team.affiliation}}</td>
                        <td>{{team.website}}</td>
                        <td>{{team.email}}</td>
                        <td>{{team.members}}</td>
                        <td class="secret">{{team.accesscode}}</td>
                        <td>
                            <div>
                                <RemoveTeam :team="team"/>
                                <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditTeam', params: { team: team } }">Edit</router-link>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    
    </div>
</template>


<script>
import { api } from '@/utils/api'
import RemoveTeam from '@/components/admin/remove/team.vue'

export default {
  name: 'AdminTeam',
  components: {
    RemoveTeam
  },
  data () {
    return {
        loading: true,
        teams: []
    }
  },
  methods: {
      _child_Remove (value) {
        console.log("here", value)
    }
  },
  beforeMount () {
    let that = this;
    api('query { allTeams{ id, name, affiliation, website, email, points, members, wrongFlags, correctFlags, accesscode } }').then(data => {
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