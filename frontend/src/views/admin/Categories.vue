<template>
  <div class="offset">
    <div v-if="loading">Yo, we loadin'. Hang tight</div>
    <div v-else>
      <div class="newOpt">
        <button class="btn btn-secondary" @click="showNew = !showNew">New Category</button>
      </div>
      <div v-if="showNew">
        <b-card header="New Category" header-tag="header">
          <AddCategory />
        </b-card>
        <hr />
      </div>
      <b-card header="Categories" header-tag="header">
        <table id="admincategories" class="table">
          <thead>
            <tr>
              <th>Category</th>
              <th>Description</th>
              <th>Number of Challenges</th>
              <th style="text-align: right;">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="category in categories" v-bind:key="category.id">
              <td>{{category.name}}</td>
              <td>{{category.description}}</td>
              <td>Blah</td>
              <td>
                <div>
                  <RemoveCategory :category="category" />
                  <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'adminEditCategory', params: { category: category } }">Edit</router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-card>
    </div>
  </div>
</template>


<script>
import { api } from "@/utils/api";
import AddCategory from "@/components/admin/add/category.vue";
import RemoveCategory from "@/components/admin/remove/category.vue";

export default {
  name: "AdminCategory",
  data() {
    return {
      loading: true,
      showNew: false,
      categories: []
    };
  },
  components: {
    AddCategory,
    RemoveCategory
  },
  beforeMount() {
    let that = this;
    api(
      "query { categories{ id, name, description, challenges { id } } }"
    ).then(data => {
      that.categories = data.categories;
      that.loading = false;
    });
  }
};
</script>

<style scoped>
</style>