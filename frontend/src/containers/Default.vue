<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="dark">
      <b-navbar-toggle target="main_nav_collapse"></b-navbar-toggle>

      <b-navbar-brand
        @click="$router.push({ name: 'Home'});"
        style="cursor: pointer;"
      >YACF {{this.$store.getters['user/brand']}}</b-navbar-brand>

      <b-collapse is-nav id="main_nav_collapse">
        <b-navbar-nav>
          <b-nav-item @click="$router.push({ name: 'Challenges'});">Challenges</b-nav-item>
          <b-nav-item @click="$router.push({ name: 'Scoreboard'});">Scoreboard</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item
            v-if="this.$store.getters['user/isAdmin']"
            @click="$router.push({ name: 'AdminMission'});"
          >Admin Dashboard</b-nav-item>
          <b-nav-item
            v-else
            @click="$router.push(`/team/${$store.getters['user/userteam']}`);"
          >{{this.$store.getters['user/userteam']}}</b-nav-item>

          <b-nav-item-dropdown right>
            <template slot="button-content">
              <span>{{$store.getters['user/initials']}}</span>
            </template>
            <b-dropdown-item @click="$router.push(`/profile`);">Profile</b-dropdown-item>
            <b-dropdown-item @click="logout">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "DefaultContainer",
  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      theme: "theme/GET_THEME"
    })
  },
  methods: {
    logout() {
      console.log("At logout");
      this.$store.dispatch("user/logout");
      this.$router.push("/login");
    }
  }
};
</script>

<style>
#app {
  height: 100vh;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
