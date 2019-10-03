import { api } from "@/utils/api";

/*

*/
const state = {
  challenge: ""
};

const getters = {
  GET_CHALLENGE: state => {
    return state.challenge;
  }
};

const actions = {
  LOAD_CHALLENGE({ commit }, id) {
    api(`query{ challenge(id:${id}){ id, description, points, flag, category { name } } }`).then(data => {
      console.log("[STORE] ", data.challenge);
      commit("SET_CHALLENGE", data.challenge);
    });
  },
  POST_FLAG({ commit }, id, flag) {
    api(`mutation{ submitflag(challenge:${id}, flag:"${flag}"){ code } }`).then(data => {
      console.log(data.submitflag);
    });
  }
};

const mutations = {
  SET_CHALLENGE(state, challenge) {
    state.challenge = challenge;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
