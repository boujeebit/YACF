<template>
    <div>
        <div v-if="loading">
            Yo, we loadin'. Hang tight
        </div>
        <div v-else>
            <table id="adminteams" class="table">
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Firstname</th>
                        <th>Lastname</th>
                        <th>Email</th>
                        <th>Team</th>
                        <th>Privilege</th>
                        <th style="text-align: right;">Options</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users" v-bind:key="user.id">
                        <td>{{user.username}}</td>
                        <td>{{user.firstName}}</td>
                        <td>{{user.lastName}}</td>
                        <td>{{user.email}}</td>
                        <td v-if="user.profile[0]">{{user.profile[0].team.name}}</td>
                        <td v-else>No Team</td>
                        <td>
                          <b-badge v-if="user.isSuperuser" variant="danger">Superuser</b-badge>
                        </td>
                        <td>
                            <div>
                                <!-- <RemoveTeam :team="team"/> -->
                                <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditUser', params: { user: user } }">Edit</router-link>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: '',
  data () {
    return {
      loading: true,
      users: ""
    }
  },
  beforeMount () {
    let that = this;
    api('query { allUsers{ id username firstName lastName email isSuperuser profile { team { name } } } }').then(data => {
        that.users = data.allUsers;
        that.loading = false;
    })
  },
  methods: {
    
  }
}
</script>

<style scoped>
</style>