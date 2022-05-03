<template>
  <div>
    <v-row align="center" justify="center" class="pb-4">
      <v-chip class=""> Logo Design </v-chip>
      <v-col class="text-center px-0" cols="12">
        <h1 class="text-h2 font-weight-light mb-4">Design Meet Beauty</h1>
        <div class="grey--text mx-4">
          <p class="mb-0">
            Explore a beautiful logo design. Where The Designer mix design with
            beauty.
          </p>
          <p>
            You have the ability to boost your brand identity, HIRE ME NOW!
          </p>
        </div>
        <div>
          <v-btn to="/logo" class="mx-3" color="primary">Check it out</v-btn>
          <v-btn
            href="https://www.fiverr.com/share/ylZj2A"
            target="_black"
            class="mx-3"
            >Hire Me</v-btn
          >
        </div>
      </v-col>
    </v-row>
    <v-parallax class="px-0" height="300" src="../assets/img/logo-design-banner.png">
    </v-parallax>
  </div>
</template>

<script>
export default {
  name: "Logo-Design",
};
</script>

<style>
</style>