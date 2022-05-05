<template>
  <div>
    <v-parallax dark src="../assets/img/logo-main-banner.jpg">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 text-md-h2 font-weight-light mb-4">Logo Design</h1>
          <div class="mx-4">
          <p class="mb-0">
            Explore a beautiful logo design. Where The Designer mix design with
            beauty.
          </p>
          <p>
            You have the ability to boost your brand identity, HIRE ME NOW!
          </p>
        </div>
          <v-btn
            href="https://www.fiverr.com/share/ylZj2A"
            target="_black"
            class="mx-3"
            dark
            >Hire Me</v-btn
          >
         <ContactForm /> 
        </v-col>
      </v-row>
    </v-parallax>
    <v-row align="center" justify="center" class="pb-4">
      <v-chip class=""> All Logos </v-chip>
    </v-row>
    <v-row align="center" justify="center">
      <v-container>
        <v-row no-gutters>
          <Loading :isLoading="isLoading" />
          <LogoBox
            v-show="!isLoading"
            cols="12"
            sm="3"
            v-for="logo in logos"
            :key="logo.id"
            :logo="logo"
          />
        </v-row>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import LogoBox from "@/components/LogoBox.vue";
import Loading from "@/components/Loading.vue";
import ContactForm from "@/components/ContactForm.vue";

export default {
  name: "LogosList",

  components: {
    LogoBox,
    Loading,
    ContactForm
  },

  data() {
    return {
      logos: [],
      isLoading: true,
    };
  },

  mounted() {
    this.getLogos();
    document.title = "Sudoer | Logos";
  },

  methods: {
    async getLogos() {
      await axios
        .get("/logos/")
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
