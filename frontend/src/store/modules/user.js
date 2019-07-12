import { api } from "@/utils/api";

const state = {
  user: "",
  auth: false
};

const getters = {
  auth: state => {
    return state.auth;
  },
  user: state => {
    return state.user;
  },
  isAdmin: state => {
    return state.user.isSuperuser ? true : false;
  },
  username: state => {
    return state.user.username;
  },
  displayname: state => {
    return state.user.firstName + " " + state.user.lastName;
  },
  initials: state => {
    if (state.user.firstName && state.user.lastName) {
      return state.user.firstName.charAt(0) + state.user.lastName.charAt(0);
    } else {
      return null;
    }
  },
  userteam: state => {
    if (state.user.profile) {
      return state.user.profile.team ? state.user.profile.team.name : null;
    } else {
      return null;
    }
  }
};

const actions = {
  logout({ commit }) {
    api("mutation { logout{ status } }").then(data => {
      console.log(data.logout);
      commit("DESTROY_USER");
    });
  },

  loadUser({ commit }) {
    api(
      "query { me{ id, username, firstName, lastName, profile{ team { id name } } } }"
    ).then(data => {
      console.log(data.me);
    });
  }
};

const mutations = {
  SET_USER(state, user) {
    state.user = user;
    state.auth = true;
  },
  DESTROY_USER(state) {
    state.user = "";
    state.auth = false;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
