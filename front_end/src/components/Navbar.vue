<template>
  <v-app-bar app>
    <div class="d-flex align-center">
      <!-- Website Logo -->
      <router-link to="/">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="../assets/logo.svg"
          transition="scale-transition"
          width="50"
        />
      </router-link>
      <h1 class="font-weight-light shrink hidden-sm-and-down dark">
        Sudoer Zero
      </h1>
    </div>

    <v-spacer></v-spacer>

    <div>
      <!-- Links -->
      <v-btn small depressed class="mx-1" to="/work">Work</v-btn>
      <v-btn small depressed class="mx-1" to="/logo">Logo</v-btn>
      <v-btn small depressed class="mx-1" to="/blog">Blog</v-btn>

      <!-- Dark mode toggle button -->
      <v-btn icon v-if="!$vuetify.theme.dark" @click="toggleTheme()">
        <v-icon class="mr-1" color="blue-grey darken-4"
          >mdi-moon-waxing-crescent</v-icon
        >
      </v-btn>
      <v-btn icon v-if="$vuetify.theme.dark" @click="toggleTheme()">
        <v-icon color="yellow darken-3">mdi-white-balance-sunny</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: "Nav-bar",

  methods: {
    toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
};
</script>
