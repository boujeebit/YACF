import axios from 'axios'

export function api(query) {
    console.log("[API UTIL]: ", query)
    return axios({
      method: 'post',
      url: '/graphql/',
      withCredentials: true,
      data: {
          'query': query
      }
    })
    .then((result) => {
      return result.data.data;
  });
}