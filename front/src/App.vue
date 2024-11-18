<template>
  <div>
    <Navbar />

    <RouterView />
  </div>
</template>

<script setup>

import Navbar from "@/components/common/Navbar.vue";
import {RouterView} from "vue-router";
</script>

<style scoped>

</style>