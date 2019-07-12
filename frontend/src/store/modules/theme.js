import { api } from "@/utils/api";

const state = {
  theme: null
};

const getters = {
  GET_THEME: state => {
    return state.theme;
  }
};

const actions = {
  GET_THEME({ commit }) {
    console.log("Gettin Server Setting!");
    api("query { theme { name primary secondary accent } }").then(data => {
      commit("SET_THEME", data.theme);
    });
  }
};

const mutations = {
  SET_THEME(state, payload) {
    console.log("Setting Theme!");
    state.theme = payload;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
