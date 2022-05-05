<template>
  <div>
    <v-parallax dark src="../assets/img/work-main-banner.jpg">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 text-md-h2 font-weight-light mb-4">Projects</h1>
          <div class="mx-4">
          <p class="mb-0">
            These some of my projects I have created and some contributed to.
          </p>
          <p>
            If you have an idea for a project feel free to CONTACT ME NOW!
          </p>
        </div>
          <div>
          <v-btn
            href="https://github.com/sudoer-zero"
            target="_black"
            class="mx-3"
            dark
            ><v-icon left> mdi-github </v-icon>Github</v-btn
          >
         <ContactForm /> 
        </div>
        </v-col>
      </v-row>
    </v-parallax>
  </div>
</template>

<script>
import ContactForm from "@/components/ContactForm.vue"
export default {
  name: 'ProjectsList',

  components: {
    ContactForm,
  },

  mounted() {
    document.title = "Sudoer | Work"
  }

}
</script>

<style>

</style>