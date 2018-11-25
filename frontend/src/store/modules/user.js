import { api } from '@/utils/api'

const state = {
    user : "",
    auth : true,
}

const getters = {
    auth: state => {
        return state.auth
    },
    user: state => {
        return state.user
    },
    isAdmin: state => {
        return state.user.isSuperuser ? true : false
    },
    username: state => {
        return state.user.username
    },
    displayname: state => {
        return state.user.firstName + " " + state.user.lastName
    },
    userteam: state => {
        return state.user.profile ? state.user.profile[0].team.name : "None"
    },
}

const actions = {

    logout ({ commit }) {
        api('mutation { logout{ status } }').then(data => {
            console.log(data.logout)
            commit('DESTROY_USER')
        })
    },

    loadUser ({ commit }) {
        api('query { me{ id, username, firstName, lastName, profile{ team { id name } } } }').then(data => {
            console.log(data.me)
        })
    }
}

const mutations = {
    SET_USER (state, user){
        state.user = user
        state.auth = true
    },
    DESTROY_USER (state) {
        state.user = ""
        state.auth = false
    }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}