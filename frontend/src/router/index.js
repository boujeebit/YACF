import Vue from "vue";
import Router from "vue-router";

import { graud, superusergraud } from "@/router/guards";

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
              path: "/admin/create",
              name: "AdminCreate",
              component: () => import("@/views/admin/Create")
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
            }
          ],
          beforeEnter: superusergraud
        }
      ]
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("@/views/Login")
    },
    {
      path: "/register/user",
      name: "RegisterUser",
      component: () => import("@/views/Register/User")
    },
    {
      path: "/register/team",
      name: "RegisterTeam",
      component: () => import("@/views/Register/Team")
    },
    {
      path: "*",
      component: () => import("@/views/errors/404")
    }
  ]
});