import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

import { WebSocketBridge } from 'django-channels'

const socket = new WebSocketBridge();

socket.connect('ws://localhost:8000/team/stream/');


// const webSocketBridge = new WebSocketBridge();
// webSocketBridge.connect('ws://localhost:8000/team/stream/');
// webSocketBridge.listen(function(action, stream) {
//   console.log(action, stream);
// });

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

// export default function createWebSocketPlugin (socket) {
//   return store => {
//     socket.connect('data', data => {
//       console.log(data);
//       // store.commit('receiveData', data)
//     })
//     // store.subscribe(mutation => {
//     //   if (mutation.type === 'UPDATE_DATA') {
//     //     socket.emit('update', mutation.payload)
//     //   }
//     // })
//   }
// }

// const plugin = createWebSocketPlugin(webSocketBridge)

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    user : "",
    board:      [],
    categories: [],
    challenges: [],
    teams: [],
    team: [],
    graphdata: [],
    graphlabels: []
  },
  getters: {
    teamRanks: state => {
      return state.teams.sort(function(a, b){
        return b.points-a.points
      })
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
    loginUser ({ commit }, credentials) {
      console.log(credentials)
      axios
        .post('http://localhost:8000/graphql/', {'query': `mutation { login(username:"${credentials.username}", password:"${credentials.password}") { id } }`})
        .then(r => r.data.data)
        .then(login => {
          // commit('SET_BOARD', board)
          console.log(login);
      })
    },
    loadChallengeBoard ({ commit }) {
      axios
        .post('http://localhost:8000/graphql/', {'query': 'query{ allCategories {id, challenges{ id, name, points }, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(board => {
          commit('SET_BOARD', board)
        })
    },
    loadCategories ({ commit }) {
      axios
        .post('http://localhost:8000/graphql/', {'query': 'query{ allCategories {id, name, description} }'})
        .then(r => r.data.data.allCategories)
        .then(categories => {
          commit('SET_CATEGORIES', categories)
        })
    },
    loadChallenges ({ commit }) {
      axios
        .post('http://localhost:8000/graphql/', {'query': 'query{ allChallenges {id, category{ id }, name, description, points} }'})
        .then(r => r.data.data.allChallenges)
        .then(challenges => {
          console.log(challenges)
          commit('SET_CHALLENGES', challenges)
        })
    },
    loadTeams ({ commit }) {
      axios
        .post('http://localhost:8000/graphql/', {'query': 'query{ allTeams {id, name, points, correctFlags, wrongFlags} }'})
        .then(r => r.data.data.allTeams)
        .then(teams => {
          console.log(teams)
          commit('SET_TEAMS', teams)
        })
    },
    loadStats ({ commit }, payload) {
      axios
        .post('http://localhost:8000/graphql/', {'query': `query{ team(name:"${payload}"){ id, name, points, solved{ id, timestamp, challenge { id, name, points, category{ name } } } } }` })
        .then(r => r.data.data.team)
        .then(team => {
          console.log(team)
          commit('SET_TEAM', team)
      })
    },
    connectScoreboard ({ commit }) {
      socket.send({"command": "join", "room": 1});
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
    },
    SET_USER (state, user){
      state.user = user
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
