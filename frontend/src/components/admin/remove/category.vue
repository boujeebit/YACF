<template>
    <div style="float: right;">
        <!-- Modal Component -->
        <button class="btn btn-sm btn-danger" v-b-modal="category.id" style="margin-left: 5px;">Remove</button>
        <b-modal v-bind:id="category.id" v-bind:title="title" ok-title='Confirm Remove' ok-variant='danger' @ok="handleOk">
          <p>Are you sure you want to <strong>delete {{category.name}}</strong>? This action cannot be undone. Type in the category name below to confirm the deletion.</p>
          <label>category Name</label>
          <input class="form-control" v-model="confirm">
          {{message}}
        </b-modal>
    </div>
</template>

<script>
import { api } from '@/utils/api.js'

export default {
  name: 'Category',
  props: ['category'],
  data () {
    return {
      loading: true,
      challenge: "",
      confirm: "",

      message: ""
    }
  },
  computed: {
    title() {
      return "Deleting " + this.category.name;
    }
  },
  methods: {
      handleOk ( evt ) {
        console.log("Delete");
        evt.preventDefault()

        // TODO: Delete out of list
        let that = this;
        if (this.confirm === this.category.name){
            api(`mutation { removeCategory(id:${this.category.id}){ message } }`).then(data => {
                if (data.removeCategory.message === "success") {
                    that.message = "Category deleted."
                } else {
                    that.message = "Category was not delete. API error"
                }
            })
        } else {
            that.message = "Categoryeam was not delete. Confirmation incorrect"
        }

      }
  }
}
</script>

<style scoped>
.stats {
  color: black;
  text-align: center;
  cursor: pointer;
  margin-bottom: 0;
}
.stats:hover {
  text-decoration: underline;
}
label {
    margin-top: 10px; 
    margin-bottom: 0px;
}
</style>