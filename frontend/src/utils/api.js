import axios from 'axios'

export function api(query) {
    console.log("[API UTIL]: ", query)
    return axios({
      method: 'post',
      url: 'http://localhost:8000/graphql/',
      withCredentials: true,
      data: {
          'query': query
      }
    })
    .then((result) => {
      return result.data.data;
  });
}