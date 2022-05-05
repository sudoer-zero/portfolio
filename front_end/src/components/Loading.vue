<template>
  <v-row v-show="isLoading" align="center" justify="center">
    <v-progress-circular indeterminate color="primary"></v-progress-circular>
  </v-row>
</template>

<script>
export default {
  name: "Loading-Circle",

  props: {
    isLoading: Boolean,
  },
};
</script>
<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>