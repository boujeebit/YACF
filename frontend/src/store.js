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
    challenges: []
  },
  actions: {
    loadChallengeBoard ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allCategories {id, challenges{ id, name, points }, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(board => {
          // console.log(board)
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
    }
  }
})
