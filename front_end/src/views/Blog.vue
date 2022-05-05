<template>
  <div>
    <v-parallax dark src="../assets/img/blog-main-banner.jpg">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 text-md-h2 font-weight-light mb-4">Articles</h1>
          <div class="mx-4">
          <p class="mb-0">
            Explore a beautiful logo design. Where The Designer mix design with
            beauty.
          </p>
          <p>
            You have the ability to boost your brand identity, HIRE ME NOW!
          </p>
        </div>
          <About />
          <ContactForm />
        </v-col>
      </v-row>
    </v-parallax>
  </div>
</template>

<script>
import ContactForm from "@/components/ContactForm.vue"
import About from "@/components/About.vue"

export default {
  name: 'BlogList',

  components: {
    ContactForm,
    About,
  },

  mounted() {
    document.title = "Sudoer | Blog"
  }

}
</script>

<style>

</style>