<template>
  <Hero/>
  <RandomArtilce/>
  <LatestLogos/>
  <Contact/>
</template>

<script>
// @ is an alias to /src
import Contact from "@/components/Contact.vue"
import RandomArtilce from "@/components/RandomArtilce.vue"
import LatestLogos from "@/components/LatestLogos.vue"
import Hero from "@/components/Hero.vue"
export default {
  name: 'HomeView',
  components: {
    Contact,
    RandomArtilce,
    Hero,
    LatestLogos,
  },

  mounted() {
    document.title = "Sudoer | Home";
  }
}
</script>
