import { api } from "@/utils/api";

/*
    Teams: Used for all teams for name, points, flag stats
    Team : Used for deeper analytics for the statistic page.
*/
const state = {
  teams: [],
  team: [],
  rank: [],
  max: 0
};

const getters = {
  ranks: state => {
    return state.teams.sort(function(a, b) {
      return b.points - a.points;
    });
  },
  GET_TEAM_RANK: state => {
    return state.rank;
  },
  GET_TEAM_SOLVE: state => {
    return state.team.solved;
  },
  GET_MAX_POINTS: state => {
    return state.max;
  }
};

const actions = {
  LoadTeamRank({ commit }) {
    api("query{ team {id, name, points, correctFlags, wrongFlags } totalPoints }").then(data => {
      commit("SET_TEAM_RANK", data.team);
      commit("SET_MAX_POINTS", data.totalPoints);
    });
  },
  loadTeams({ commit }) {
    api("query{ teams {id, name, points, correctFlags, wrongFlags} totalPoints }").then(data => {
      commit("SET_TEAMS", data.teams);
      commit("SET_MAX_POINTS", data.totalPoints);
    });
  },
  loadStats({ commit }, payload) {
    api(`query{ teamName(name:"${payload}"){ id, name, points, players { user { username } }, solved{ id, timestamp, challenge { id, name, points, category{ name } } } } }`).then(data => {
      commit("SET_TEAM", data.teamName);
    });
  }
};

const mutations = {
  SET_TEAMS(state, teams) {
    state.teams = teams;
  },
  SET_TEAM(state, team) {
    state.team = team;
  },
  SET_TEAM_RANK(state, team) {
    state.rank = team;
  },
  SET_MAX_POINTS(state, points) {
    state.max = points;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
