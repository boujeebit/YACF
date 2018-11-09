import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    board:      [],
    categories: [],
    challenges: [],
    teams: [],
    team: []
  },
  getters: {
    teamRanks: state => {
      return state.teams.sort(function(a, b){
        return b.points-a.points
      })
    },
    solved: state => {
      return state.team.solved
    }
  },
  actions: {
    loadChallengeBoard ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allCategories {id, challenges{ id, name, points }, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(board => {
          commit('SET_BOARD', board)
        })
    },
    loadCategories ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allCategories {id, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(categories => {
          commit('SET_CATEGORIES', categories)
        })
    },
    loadChallenges ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allChallenges {id, category{ id }, name, description, points} }'})
        .then(r => r.data.data.allChallenges)
        .then(challenges => {
          console.log(challenges)
          commit('SET_CHALLENGES', challenges)
        })
    },
    loadTeams ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allTeams {id, name, points, correctFlags, wrongFlags} }'})
        .then(r => r.data.data.allTeams)
        .then(teams => {
          console.log(teams)
          commit('SET_TEAMS', teams)
        })
    },
    loadStats ({ commit }, payload) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': `query{ team(name:"${payload}"){ id, points, solved{ id, timestamp, challenge { id, name, points, category{ name } } } } }` })
        .then(r => r.data.data.team)
        .then(team => {
          console.log(team)
          commit('SET_TEAM', team)
      })
    }
  },
  mutations: {
    SET_BOARD (state, board) {
      state.board = board
    },
    SET_CATEGORIES (state, categories) {
      state.categories = categories
    },
    SET_CHALLENGES (state, challenges) {
      state.challenges = challenges
    },
    SET_TEAMS (state, teams) {
      state.teams = teams
    },
    SET_TEAM (state, team) {
      state.team = team
    }
    
  }
})
