<template>
  <div>
    <v-row align="center" justify="center">
      <v-container>
        <v-row no-gutters>
          <LogoBox
            cols="12"
            sm="3"
            v-for="logo in logos"
            :key="logo.id"
            :logo="logo"
          />
        </v-row>
      </v-container>
    </v-row>
    <v-parallax
      class="px-0"
      height="300"
      src="../assets/img/logo-design-banner-color.png"
    >
    </v-parallax>
  </div>
</template>

<script>
import axios from "axios";
import LogoBox from "./LogoBox.vue";
export default {
  name: "Recent-Logos",

  components: {
    LogoBox,
  },

  data() {
    return {
      logos: [],
    };
  },

  mounted() {
    this.getLogos();
  },

  methods: {
    async getLogos() {
      await axios
        .get("/logos/latest-logos")
        .then((response) => {
          this.logos = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>