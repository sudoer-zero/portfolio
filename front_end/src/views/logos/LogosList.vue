<template>
  <Loading :isLoading="isLoading" />
  <div v-show="!isLoading">
    <div class="w-11/12 md:w-5/6 mx-auto">
      <div class="grid grid-cols-4 gap-1 lg:gap-4">
        <LogoBox
          class="col-span-2 md:col-span-1"
          v-for="logo in logos"
          :key="logo.id"
          :logo="logo"
        >
        </LogoBox>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import LogoBox from "@/components/LogoBox.vue";
import Loading from "@/components/Loading.vue"
export default {
  name: "LogosList",

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
    document.title = "Sudoer | Logos";
  },

  methods: {
    async getLogos() {
      await axios
        .get("/logos/")
        .then((response) => {
          this.logos = response.data;
          this.isLoading = false
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
