<template>
  <div>
    <Hero />
    <LogoDesign /> 
    <RecentLogos />
    <RecentArticles />
  </div>
</template>

<script>
import Hero from "@/components/Hero.vue";
import LogoDesign from "@/components/logo/LogoDesign.vue";
import RecentLogos from "@/components/logo/RecentLogos.vue";
import RecentArticles from "@/components/blog/RecentArticles.vue";
export default {
  name: "HomeView",

  components: {
    Hero,
    LogoDesign,
    RecentLogos,
    RecentArticles,
  },

  mounted() {
    document.title = "Sudoer | Home";
  },
};
</script>
