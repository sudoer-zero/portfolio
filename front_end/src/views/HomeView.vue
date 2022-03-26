<template>
  <RandomArtilce/>
  <Contact/>
</template>

<script>
// @ is an alias to /src
import Contact from "@/components/Contact.vue"
import RandomArtilce from "@/components/RandomArtilce.vue"
export default {
  name: 'HomeView',
  components: {
    Contact,
    RandomArtilce
  }
}
</script>
