<template>
  <div>
    <div class="w-11/12 md:w-5/6 mx-auto">
      <div class="grid grid-cols-4 lg:gap-4">
        <LogoBox
          class="col-span-4 md:col-span-1"
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

export default {
  name: "LogosList",

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
    document.title = "Sudoer | Logos";
  },

  methods: {
    async getLogos() {
      await axios
        .get("/logos/")
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
