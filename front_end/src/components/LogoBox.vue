<template>
  <v-card
    class="mx-auto my-3"
  >
    <v-img
      height="200px"
      width="200px"
      :src="logo.get_thumbnail"
    >
    </v-img>


  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "Logo-Box",

  props: {
    logo: Object,
  },

  data() {
    return {
      id: this.logo.id,
      star: this.logo.star,
    };
  },

  methods: {
    postStar() {
      axios
        .post(`/logos/${this.id}/star/`, this.star)
        .then(this.star++)
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>