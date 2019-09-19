<template>
  <div>
    <AdminNav />
    <router-view></router-view>
  </div>
</template>

<script>
import AdminNav from "@/components/admin/adminnav.vue";

export default {
  name: "home",
  components: {
    AdminNav
  }
};
</script>
