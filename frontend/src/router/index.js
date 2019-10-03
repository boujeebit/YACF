import Vue from "vue";
import Router from "vue-router";

import { base, graud, superusergraud } from "@/router/guards";

Vue.use(Router);

export default new Router({
  mode: "history",
  linkActiveClass: "open active",
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: "/",
      component: () => import("@/containers/Default"),
      redirect: { name: "Home" },
      name: "Root",
      beforeEnter: graud,
      children: [
        {
          path: "/_",
          name: "Home",
          component: () => import("@/views/Home")
        },
        {
          path: "/challenges",
          name: "Challenges",
          component: () => import("@/views/Challenges")
        },
        {
          path: "/challenge/:category/:points",
          name: "Statistics",
          component: () => import("@/views/Statistics")
        },
        {
          path: "/scoreboard",
          name: "Scoreboard",
          component: () => import("@/views/Scoreboard")
        },
        {
          path: "/page/:url",
          name: "Page",
          component: () => import("@/views/Page")
        },
        {
          path: "/team/:name",
          name: "Team",
          component: () => import("@/views/Team")
        },
        {
          path: "/admin",
          name: "Admin",
          component: () => import("@/views/Admin"),
          children: [
            {
              path: "/admin/mission",
              name: "AdminMission",
              component: () => import("@/views/admin/Mission")
            },
            {
              path: "/admin/welcome",
              name: "AdminWelcome",
              component: () => import("@/views/admin/Welcome")
            },
            {
              path: "/admin/pages",
              name: "AdminPages",
              component: () => import("@/views/admin/Pages")
            },
            {
              path: "/admin/pages/create",
              name: "AdminCreatePages",
              component: () => import("@/views/admin/Create/Page")
            },
            {
              path: "/admin/categories",
              name: "AdminCategories",
              component: () => import("@/views/admin/Categories")
            },
            {
              path: "/admin/category/edit",
              name: "AdminCategoryEdit",
              component: () => import("@/views/admin/Edit/Category"),
              props: true
            },
            {
              path: "/admin/challenges",
              name: "AdminChallenges",
              component: () => import("@/views/admin/Challenges")
            },
            {
              path: "/admin/challenge/edit",
              name: "AdminChallengeEdit",
              component: () => import("@/views/admin/Edit/Challenge"),
              props: true
            },
            {
              path: "/admin/teams",
              name: "AdminTeams",
              component: () => import("@/views/admin/Teams")
            },
            {
              path: "/admin/team/edit",
              name: "AdminTeamEdit",
              component: () => import("@/views/admin/Edit/Team"),
              props: true
            },
            {
              path: "/admin/users",
              name: "AdminUsers",
              component: () => import("@/views/admin/Users")
            },
            {
              path: "/admin/user/edit",
              name: "AdminUserEdit",
              component: () => import("@/views/admin/Edit/User"),
              props: true
            },
            {
              path: "/admin/solves",
              name: "AdminSolves",
              component: () => import("@/views/admin/Solves")
            },
            {
              path: "/admin/surveys",
              name: "AdminSurveys",
              component: () => import("@/views/admin/Surveys")
            },
            {
              path: "/admin/settings",
              name: "AdminSettings",
              component: () => import("@/views/admin/Settings")
            },
            {
              path: "/admin/scripter",
              name: "AdminScripter",
              component: () => import("@/views/admin/Scripter")
            }
          ],
          beforeEnter: superusergraud
        }
      ]
    },
    {
      path: "/login",
      name: "Login",
      beforeEnter: base,
      component: () => import("@/views/Login")
    },
    {
      path: "/register/user",
      name: "RegisterUser",
      beforeEnter: base,
      component: () => import("@/views/Register/User")
    },
    {
      path: "/register/team",
      name: "RegisterTeam",
      beforeEnter: base,
      component: () => import("@/views/Register/Team")
    },
    {
      path: "*",
      beforeEnter: base,
      component: () => import("@/views/errors/404")
    }
  ]
});
