import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
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

import store from './store.js'

import { isAuthenicated } from './utils/auth'

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
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: (to, from, next) => {
        let that = this;
        isAuthenicated().then((result) => {
            // console.log(result.data.data.me);
            if(result.data.data.me !== null) {
                console.log(result.data.data.me);
                store.state.user = result.data.data.me
                store.state.auth = true
                console.log('User: ', store.state.user);
                next();
            } else {
                console.log("[ROUTE]: Authenication failed, going to login")
                next('/login');
            }
        });
      }
    },
    {
      path: '/challenges',
      name: 'Challenges',
      component: Challenges,
      beforeEnter: (to, from, next) => {
        let that = this;
        isAuthenicated().then((result) => {
            // console.log(result.data.data.me);
            if(result.data.data.me !== null) {
                console.log(result.data.data.me);
                store.state.user = result.data.data.me
                store.state.auth = true
                console.log('User: ', store.state.user);
                next();
            } else {
                console.log("[ROUTE]: Authenication failed, going to login")
                next('/login');
            }
        });
      }
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
        { path: '/admin/welcome', component: AdminWelcome },
        { path: '/admin/create', component: AdminCreate },
        { path: '/admin/categories', component: AdminCategory },
        { path: '/admin/challenges', component: AdminChallenge },
        { path: '/admin/teams', component: AdminTeams },
      ],
      beforeEnter: (to, from, next) => {
        let that = this;
        isAuthenicated().then((result) => {
            // console.log(result.data.data.me);
            if(result.data.data.me !== null) {
                console.log(result.data.data.me);
                store.state.user = result.data.data.me
                store.state.auth = true
                console.log('User: ', store.state.user);
                result.data.data.me.isSuperuser ? next() : next('/')
            } else {
                console.log("[ROUTE]: Authenication failed, going to login")
                next('/login');
            }
        });
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    { path: '*', redirect: '/' }
  ]
})
