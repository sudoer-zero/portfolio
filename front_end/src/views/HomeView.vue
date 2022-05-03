<template>
  <div>
    <Hero />
    <LogoDesign /> 
    <RecentLogos />
  </div>
</template>

<script>
import Hero from "@/components/Hero.vue";
import LogoDesign from "@/components/LogoDesign.vue";
import RecentLogos from "@/components/RecentLogos.vue";
export default {
  name: "HomeView",

  components: {
    Hero,
    LogoDesign,
    RecentLogos,
  },

  mounted() {
    document.title = "Sudoer | Home";
  },
};
</script>
