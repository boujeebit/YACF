import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

import { WebSocketBridge } from 'django-channels'

import { api } from './utils/api.js'

const socket = new WebSocketBridge();

socket.connect('ws://localhost:8000/team/stream/');

const createWebSocketPlugin = function(socket) {
	return store => {
		socket.listen(function(action, stream) {
		console.log(action);
		switch(action.type) {
			// case 0:
			// 	console.log("Adding subscription");
			// 	store.commit('addSubscription', action)
			// 	break;
			case 1:
				store.commit('addPoints', action)
				break;
			// case 2:
			// 	console.log("Recieved Port");
			// 	console.log(action);
			// 	store.commit('addPort', action)
			// 	break;
			// case 3:
			// 	break;
			default:
				break;
		}

		// store.commit('addMessage', action)
		})
	//   store.subscribe(mutation => {
	// 	if (mutation.type === 'UPDATE_DATA') {
	// 	  socket.emit('update', mutation.payload)
	// 	}
	//   })
	}
}


const plugin = createWebSocketPlugin(socket)



Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    user : "none",
    auth : false,
    board :     "",
    solves:   "",
    categories: [],
    challenges: [],
    teams: [],
    team : [],
    graphdata :  [],
    graphlabels: []
  },
  getters: {
    auth: state => {
      return state.auth
    },
    user: state => {
      return state.user
    },
    isAdmin: state => {
      return state.user.isSuperuser ? true : false
    },
    teamRanks: state => {
      return state.teams.sort(function(a, b){
        return b.points-a.points
      })
    },
    userteam: state => {
      return state.user.profile ? state.user.profile[0].team.name : "None"
    },
    // userplace: state => {
    //   console.log("Get place", state.teams.find(team => team.name === state.user.profile[0].team.name))
    //   return state.teams.find(team => team.name === state.user.profile[0].team.name);
    // },
    username: state => {
      return state.user.username
    },
    displayname: state => {
      return state.user.firstName + " " + state.user.lastName
    },
    solved: state => {
      return state.team.solved
    },
    graphdata: state => {
      return state.graphdata
    },
    graphlabels: state => {
      return state.graphlabels
    }
  },
  actions: {
    logout ({ commit }) {
      api('mutation { logout{ status } }').then(data => {
        console.log(data.logout)
        commit('DESTROY_USER')
      })
    },
    loadUser ({ commit }) {
      axios
        .post('http://localhost:8000/graphql/', {'query': 'query { me{ id, username, firstName, lastName, profile{ team { id name } } } }'})
        .then(r => r.data.data)
        .then(me => {
          // commit('SET_BOARD', board)

          console.log("In load user:", me);
      })
    },
    loadChallengeBoard ({ commit }) {
      api('query{ allCategories {id, challenges{ id, name, points }, name, description}, teamSovle{ challenge{ id } } }').then(data => {
        commit('SET_BOARD', data.allCategories)
        commit('SET_SOLVES', data.teamSovle)
      })
    },
    loadChallenges ({ commit }) {
      api('query{ allChallenges {id, category{ id }, name, description, points} }').then(data => {
        commit('SET_CHALLENGES', data.allChallenges)
      })
    },
    loadTeams ({ commit }) {
      api('query{ allTeams {id, name, points, correctFlags, wrongFlags} }').then(data => {
        commit('SET_TEAMS', data.allTeams)
      })
    },
    loadStats ({ commit }, payload) {
      api(`query{ team(name:"${payload}"){ id, name, points, solved{ id, timestamp, challenge { id, name, points, category{ name } } } } }`).then(data => {
        commit('SET_TEAM', data.team)
      })
    },
    connectScoreboard ({ commit }) {
      socket.send({"command": "join", "room": 1});
    }
  },
  mutations: {
    DESTROY_USER (state) {
      state.user = ""
      state.auth = false
      state.board = ""
    },
    SET_BOARD (state, board) {
      state.board = board
    },
    SET_SOLVES (state, solves) {
      state.solves = solves
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
    },
    SET_USER (state, user){
      state.user = user
      state.auth = true
    },
    SET_GRAPH (state, graph) {
      state.graphdata = graph.data;
      state.graphlabels = graph.labels;
    },
    addPoints (state, payload) {
      console.log("Adding points to team: ", payload.team);
      if (state.teams) {
        console.log(state.teams);
        // console.log(state.teams.find(team => team.name === payload.team))
        let team, newteam = state.teams.find(team => team.name === payload.team);
        console.log(team)
        newteam.points = payload.points;
        // TODO: There might be a bug here.
        state.teams.splice(team, 1, newteam);
        
        // Update graph
        for (let i = 0; i < state.graphdata.length; i++) { 
          console.log(state.graphdata[i].label , payload.team)
          if (state.graphdata[i].label === payload.team) {
            console.log("TRUE!!!!")
            state.graphdata[i].data.push(payload.points)
          } else {
            state.graphdata[i].data.push(state.graphdata[i].data.slice(-1)[0])
          }
        }
        // Do last. When this gets updated the graph on page does too.
        state.graphlabels.push(payload.time);
      }
      
    },
    
  },
  plugins: [plugin]
})