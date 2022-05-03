<template>
  <div>
    <Hero />
    <LogoDesign /> 
  </div>
</template>

<script>
import Hero from "@/components/Hero.vue";
import LogoDesign from "@/components/LogoDesign.vue";

export default {
  name: "HomeView",

  components: {
    Hero,
    LogoDesign,
  },
};
</script>
