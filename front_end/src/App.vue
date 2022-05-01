<template>
  <v-app>
    <Navbar/>
    <h1 class="py-40">Testing Dark mode</h1>
    <v-toolbar-title>Collapsing Bar</v-toolbar-title>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
  name: 'App',

  components:{
    Navbar,
  },

  data: () => ({
    //
  }),
};
</script>
