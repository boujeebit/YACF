import Vue from "vue";
import Vuex from "vuex";

import user from "./modules/user";
import teams from "./modules/teams";
import challenge from "./modules/challenge";
import theme from "./modules/theme";

import { WebSocketBridge } from "django-channels";

import { api } from "@/utils/api.js";

const socket = new WebSocketBridge();

// socket.connect('ws://team/stream/');

// socket.connect("ws://localhost:8000/team/stream/"); //DEV!

const createWebSocketPlugin = function(socket) {
  return store => {
    socket.listen(function(action, stream) {
      console.log(action);
      switch (action.type) {
        case 1:
          store.commit("addPoints", action);
          break;
        default:
          break;
      }
    });
  };
};

// const plugin = createWebSocketPlugin(socket);

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    teams,
    challenge,
    theme
  },
  state: {
    board: "",
    challenges: [],
    solves: "",
    // solved: "",

    graphdata: [],
    graphlabels: []
  },
  getters: {
    // solved: state => {
    //   return ""
    //   // return state.team.solved
    // },
    graphdata: state => {
      return state.graphdata;
    },
    graphlabels: state => {
      return state.graphlabels;
    }
  },
  actions: {
    loadChallengeBoard({ commit }) {
      api("query{ categories {id, challenges{ id, name, points }, name, description}, teamSovle{ challenge{ id } } }").then(data => {
        commit("SET_BOARD", data.categories);
        commit("SET_SOLVES", data.teamSovle);
      });
    },

    loadNewChallengeBoard({ commit }) {
      api("query{ challenges {id, name points category {name} } }").then(data => {
        commit("SET_NEW_BOARD", data.challenges);
        // commit("SET_SOLVES", data.teamSovle);
      });
    },

    connectScoreboard({ commit }) {
      socket.send({ command: "join", room: 1 });
    }
  },
  mutations: {
    SET_BOARD(state, board) {
      state.board = board;
    },
    SET_NEW_BOARD(state, challenges) {
      state.challenges = challenges;
    },
    SET_SOLVES(state, solves) {
      var ids = [];
      if (solves) {
        solves.forEach(function(solve) {
          ids.push(solve.challenge.id);
        });
      }
      state.solves = ids;
    },
    SET_USER_SOLVE(state, id) {
      state.solves.push(id);
    },
    SET_GRAPH(state, graph) {
      state.graphdata = graph.data;
      state.graphlabels = graph.labels;
    },
    addPoints(state, payload) {
      console.log("Adding points to team: ", payload.team);
      if (state.teams) {
        console.log(state.teams);
        // console.log(state.teams.find(team => team.name === payload.team))
        let team,
          newteam = state.teams.find(team => team.name === payload.team);
        console.log(team);
        newteam.points = payload.points;
        // TODO: There might be a bug here.
        state.teams.splice(team, 1, newteam);

        // Update graph
        for (let i = 0; i < state.graphdata.length; i++) {
          console.log(state.graphdata[i].label, payload.team);
          if (state.graphdata[i].label === payload.team) {
            console.log("TRUE!!!!");
            state.graphdata[i].data.push(payload.points);
          } else {
            state.graphdata[i].data.push(state.graphdata[i].data.slice(-1)[0]);
          }
        }
        // Do last. When this gets updated the graph on page does too.
        state.graphlabels.push(payload.time);
      }
    }
  }

  // plugins: [plugin]
});
