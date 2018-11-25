import { api } from '@/utils/api'

/*
    Teams: Used for all teams for name, points, flag stats
    Team : Used for deeper analytics for the statistic page.
*/
const state = {
    teams: [],
    team : []
}

const getters = {
    ranks: state => {
        return state.teams.sort(function(a, b){
          return b.points-a.points
        })
    },
    GET_TEAM_SOLVE: state => {
        return state.team.solved
    },
}

const actions = {
    loadTeams ({ commit }) {
        api('query{ allTeams {id, name, points, correctFlags, wrongFlags} }').then(data => {
          commit('SET_TEAMS', data.allTeams)
        })
    },
    loadStats ({ commit }, payload) {
        api(`query{ team(name:"${payload}"){ id, name, points, solved{ id, timestamp, challenge { id, name, points, category{ name } } } } }`).then(data => {
          commit('SET_TEAM', data.team)
        })
    }
}

const mutations = {
    SET_TEAMS (state, teams) {
        state.teams = teams
    },
    SET_TEAM (state, team) {
        state.team = team
    }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}