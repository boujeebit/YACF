import axios from 'axios'

export function isAuthenicated() {
    console.log("[AUTH]: Validating User");

    return axios({
        url: 'http://localhost:8000/graphql/',
        withCredentials: true,
        method: 'post',
        data: {
            query: `
            {
                me {
                  id,
                  isSuperuser,
                  username,
                  firstName,
                  lastName
                }
            }
            `
        },
    }).then((result) => {
        // For refreash. Add to store if auth is false.
        // if(!store.auth && result.data.data.me !== null){
        //     store.commit('addUser', result.data.data.me);
        // }

        return result;
    });
}