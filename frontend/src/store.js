import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    testval: "Test is a test",
    categories: []
  },
  actions: {
    loadCategories ({ commit }) {
      axios
        .post('http://127.0.0.1:8000/graphql/', {'query': 'query{ allCategories {id, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(categories => {
          commit('SET_CATEGORIES', categories)
        })
    }
  },
  mutations: {
    SET_CATEGORIES (state, categories) {
      state.categories = categories
    }
  }
})
