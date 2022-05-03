<template>
  <v-parallax dark src="../assets/img/hero-banner.jpg">
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <h1 class="text-h4 text-md-h2 font-weight-light mb-4">DEVELOPER</h1>
        <h1 class="text-h4 text-md-h2 font-weight-light mb-4">LOGO DESIGNER</h1>
        <h1 class="text-h4 text-md-h2 font-weight-light mb-4">TECH ENTHUSIAST</h1>
        <div>
          <v-btn
            href="https://github.com/sudoer-zero"
            target="_black"
            class="mx-3"
            dark
            ><v-icon left> mdi-github </v-icon>Github</v-btn
          >
          <v-btn
            href="https://twitter.com/sudoerzero"
            target="_black"
            class="mx-3"
            color="primary"
            ><v-icon left> mdi-twitter </v-icon>Twitter</v-btn
          >
        </div>
      </v-col>
    </v-row>
  </v-parallax>
</template>

<script>
export default {
  name: "Hero-Banner",
};
</script>
