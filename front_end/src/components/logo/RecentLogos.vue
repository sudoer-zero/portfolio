<template>
  <div>
    <v-row align="center" justify="center">
      <v-chip class=""> Recent Logos </v-chip>
    </v-row>
    <Loading :isLoading="isLoading" />
    <v-row v-show="!isLoading" align="center" justify="center">
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
      height="200"
      src="../../assets/img/logo-design-banner-color.png"
    >
    </v-parallax>
  </div>
</template>

<script>
import axios from "axios";
import LogoBox from "./LogoBox.vue";
import Loading from "@/components/Loading.vue";
export default {
  name: "Recent-Logos",

  components: {
    LogoBox,
    Loading,
  },

  data() {
    return {
      logos: [],
      isLoading: true,
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
          this.isLoading = false;
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