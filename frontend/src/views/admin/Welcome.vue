<template>
    <div style="padding:20px">
        <h3>Configure Welcome</h3>

        <p>{{status}}</p>
        <label>Welcome page (html enabled):</label>
        <textarea class="form-control" v-model="content" v-bind:rows="20"></textarea>

        <button class="btn btn-secondary" style="margin-top: 10px;" @click="addWelcome()">Submit</button>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: '',
  data () {
    return {
        content: "",
        status : ""
    }
  },
  beforeMount () {
    let that = this;
    api('query{ welcomePage{ content } }').then(data => {
      that.content = data.welcomePage.content;
    })
  },
  methods: {
    addWelcome () {
        console.log("Adding welcome")
        let that = this

        var re = new RegExp('\n', 'g');
        var str = this.content.replace(re, '\\n');
        console.log("One string: ", str)
        
        api(`mutation{ welcome(content:"${str}"){ status } }`).then(data => {
            that.status = data.welcome.status;
        })
    }
  }
}
</script>

<style scoped>
</style>