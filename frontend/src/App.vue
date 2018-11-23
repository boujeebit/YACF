<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="dark" v-if="this.$store.getters.auth">

      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand @click="$router.push('/');">YACF</b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item @click="$router.push('/challenges');">Challenges</b-nav-item>
          <b-nav-item @click="$router.push('/scoreboard');">Scoreboard</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>{{this.$store.getters.displayname}}</em>
            </template>
            <b-dropdown-item @click="$router.push(`/user/${$store.getters.displayname}`);">Profile (NW)</b-dropdown-item>
            <b-dropdown-item @click="logout">Signout</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item v-if="this.$store.getters.isAdmin" @click="$router.push('/admin/mission');">Admin Dashboard</b-nav-item>
          <b-nav-item v-else @click="$router.push(`/team/${$store.getters.userteam}`);">{{this.$store.getters.userteam}}</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {

    }
  },
  methods: {
    logout () {
      console.log("At logout");
      this.$store.dispatch('logout');
      this.$router.push('/login');
    }
  }
}
</script>


<style>
#app {
  height: 100vh;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
