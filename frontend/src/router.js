import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
import RegisterUser from './views/Register/User.vue'
import RegisterTeam from './views/Register/Team.vue'
import Profile from './views/Profile.vue'
import Home from './views/Home.vue'
import Challenges from './views/Challenges.vue'
import Statistics from './views/Statistics.vue'
import Scoreboard from './views/Scoreboard.vue'
import Team from './views/Team.vue'
import Admin from './views/Admin.vue'
import MissionControl from './views/admin/Mission.vue'
import AdminWelcome from './views/admin/Welcome.vue'
import AdminCreate from './views/admin/Create.vue'
import AdminCategory from './views/admin/Categories.vue'
import AdminChallenge from './views/admin/Challenges.vue'
import AdminTeams from './views/admin/Teams.vue'
import AdminEditChallenge from './views/admin/Edit/Challenge.vue'

import { graud, superusergraud } from '@/utils/guards'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/resigster/user',
      name: 'resigster-user',
      component: RegisterUser
    },
    {
      path: '/resigster/team',
      name: 'resigster-team',
      component: RegisterTeam
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      beforeEnter: graud
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: graud
    },
    {
      path: '/challenges',
      name: 'Challenges',
      component: Challenges,
      beforeEnter: graud
    },
    {
      path: '/challenge/:category/:points',
      name: 'Statistics',
      component: Statistics,
      beforeEnter: graud
    },
    {
      path: '/scoreboard',
      name: 'scoreboard',
      component: Scoreboard,
      beforeEnter: graud
    },
    {
      path: '/team/:name',
      name: 'team',
      component: Team,
      beforeEnter: graud
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      children: [
        { path: '/admin/mission', component: MissionControl },
        { path: '/admin/welcome', component: AdminWelcome },
        { path: '/admin/create', component: AdminCreate },
        { path: '/admin/categories', component: AdminCategory },
        { path: '/admin/challenges', component: AdminChallenge },
        { path: '/admin/challenge/edit', name: 'adminEditChallenge', component: AdminEditChallenge, props: true },
        { path: '/admin/teams', component: AdminTeams },
      ],
      beforeEnter: superusergraud
    },
    { path: '*', redirect: '/' }
  ]
})
