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
                  lastName,
                  profile{
                    team{
                        name
                    }
                  }
                }
            }
            `
        },
    }).then((result) => {
        return result;
    });
}