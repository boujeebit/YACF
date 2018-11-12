import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Statistics from './views/Statistics.vue'
import Scoreboard from './views/Scoreboard.vue'
import Team from './views/Team.vue'
import Admin from './views/Admin.vue'
import MissionControl from './views/admin/Mission.vue'
import AdminCreate from './views/admin/Create.vue'
import AdminCategory from './views/admin/Categories.vue'
import AdminChallenge from './views/admin/Challenges.vue'
import AdminTeams from './views/admin/Teams.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/challenge/:category/:points',
      name: 'Statistics',
      component: Statistics
    },
    {
      path: '/scoreboard',
      name: 'scoreboard',
      component: Scoreboard
    },
    {
      path: '/team/:name',
      name: 'team',
      component: Team
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      children: [
        { path: '/admin/mission', component: MissionControl },
        { path: '/admin/create', component: AdminCreate },
        { path: '/admin/categories', component: AdminCategory },
        { path: '/admin/challenges', component: AdminChallenge },
        { path: '/admin/teams', component: AdminTeams },
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
