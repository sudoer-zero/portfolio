<template>
  <v-app-bar
      app
      color="primary"
      
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down dark"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

       <v-btn icon v-if="!$vuetify.theme.dark" @click="toggleTheme()">
        <v-icon class="mr-1" color="blue-grey darken-4">mdi-moon-waxing-crescent</v-icon>
      </v-btn>
      <v-btn icon v-if="$vuetify.theme.dark" @click="toggleTheme()">
        <v-icon color="yellow darken-3">mdi-white-balance-sunny</v-icon>
      </v-btn>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
</template>

<script>
export default {
  name: 'Nav-bar',

  methods: {
     toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }

}
</script>

<style>

</style>