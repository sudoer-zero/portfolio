<template>
  <div class="mt-10">
    <v-divider></v-divider>
    <v-footer>
      <v-container>
        <v-row>
          <v-col cols="12" sm="6">
            <div class="d-flex align-center">
              <!-- Website Logo -->
              <router-link to="/">
                <v-img
                  alt="Logo"
                  class="shrink mr-2"
                  contain
                  src="../assets/logo.svg"
                  transition="scale-transition"
                  width="50"
                />
              </router-link>
              <h1 class="font-weight-light shrink dark">Sudoer Zero</h1>
            </div>
            <div>
              <v-btn
                href="https://github.com/sudoer-zero"
                target="_black"
                class="mr-1 my-2"
                dark
                small
                ><v-icon left> mdi-github </v-icon>Github</v-btn
              >
              <v-btn
                href="https://twitter.com/sudoerzero"
                target="_black"
                class="mr-1 my-2"
                color="primary"
                small
                ><v-icon left> mdi-twitter </v-icon>Twitter</v-btn
              >
            </div>
          </v-col>
          <v-col cols="12" sm="6">
            <v-row>
              <v-col>
                <h3 class="font-weight-light ml-2">Pages</h3>
                <!-- Links -->
                <div>
                  <v-btn small class="my-1" color="primary" text to="/"
                    >Home</v-btn
                  >
                </div>
                <div>
                  <v-btn small class="my-1" color="primary" text to="/work"
                    >Work</v-btn
                  >
                </div>
                <div>
                  <v-btn small class="my-1" color="primary" text to="/logo"
                    >Logo</v-btn
                  >
                </div>
                <div>
                  <v-btn small class="my-1" color="primary" text to="/blog"
                    >Blog</v-btn
                  >
                </div>
              </v-col>
              <v-col>
                <h3 class="font-weight-light ml-2">Links</h3>
                <!-- Links -->
                <div>
                  <v-btn small class="my-1" color="primary" text
                    href="https://github.com/sudoer-zero/portfolio"
                    target="_black"
                    >Website Repo</v-btn
                  >
                </div>
                <div>
                  <v-btn small class="my-1" color="primary" text
                    href="https://github.com/sudoer-zero/portfolio/issues"
                    target="_black"
                    >Found a bug?</v-btn
                  >
                </div>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12">
            <v-row align="center" justify="center">
              <v-col cols="12" sm="6">
                Copyright © {{ new Date().getFullYear() }} —
                <strong>Sudoer Zero</strong>
              </v-col>
              <v-col cols="12" sm="6">
                <About />
                <ContactForm />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </div>
</template>
<script>
import ContactForm from "./ContactForm.vue";
import About from "./About.vue";

export default {
  name: "Footer-Bar",

  components: {
    ContactForm,
    About,
  },
};
</script>