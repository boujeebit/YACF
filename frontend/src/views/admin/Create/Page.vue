<template>
  <div class="offset">
    <b-card header="New Page" header-tag="header">
      <AddPage />
    </b-card>
  </div>
</template>

<script>
import AddPage from "@/components/admin/add/Page.vue";

export default {
  name: "AdminCreatePage",
  components: { AddPage },
  data() {
    return {};
  }
};
</script>