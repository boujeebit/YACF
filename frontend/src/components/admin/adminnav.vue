<template>
  <b-navbar toggleable="md" type="light" variant="light">
    <b-navbar-toggle target="admin_nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="admin_nav_collapse">
      <b-navbar-nav>
        <b-nav-item @click="$router.push('/admin/mission');">Mission Control</b-nav-item>
        <b-nav-item @click="$router.push('/admin/welcome');">Welcome</b-nav-item>
        <b-nav-item @click="$router.push('/admin/pages');">Pages</b-nav-item>
        <b-nav-item @click="$router.push('/admin/categories');">Categories</b-nav-item>
        <b-nav-item @click="$router.push('/admin/challenges');">Challenges</b-nav-item>
        <b-nav-item @click="$router.push('/admin/teams');">Teams</b-nav-item>
        <b-nav-item @click="$router.push('/admin/users');">Users</b-nav-item>
        <b-nav-item @click="$router.push('/admin/solves');">Solves</b-nav-item>
        <b-nav-item @click="$router.push('/admin/surveys');">Surveys</b-nav-item>
        <b-nav-item @click="$router.push('/admin/settings');">Settings</b-nav-item>
        <!-- <b-nav-item @click="$router.push('/admin/scripter');">Scripter</b-nav-item> -->
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "adminNav"
};
</script>