<template>
  <Navbar/>
  <router-view/>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: { 
    Navbar, 
  }
}
</script>
<style>
#app {
  background-color: #F6F5F5;
}
</style>