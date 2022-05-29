<template>
  <div>
    <v-parallax dark src="../assets/img/work-main-banner.jpg">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 text-md-h2 font-weight-light mb-4">Projects</h1>
          <div class="mx-4">
            <p class="mb-0">These some of my projects I have created and some contributed to.</p>
            <p>If you have an idea for a project feel free to CONTACT ME NOW!</p>
          </div>
          <div>
            <v-btn href="https://github.com/sudoer-zero" target="_black" class="mx-3" dark>
              <v-icon left>mdi-github</v-icon>Github
            </v-btn>
            <ContactForm />
          </div>
        </v-col>
      </v-row>
    </v-parallax>
    <v-row align="center" justify="center" class="pb-4">
      <v-chip class>All Projects</v-chip>
    </v-row>

    <Loading :isLoading="isLoading" />
    <div v-show="!isLoading" class="my-5">
      <v-container>
        <v-row justify="center">
          <v-expansion-panels popout>
            <v-expansion-panel v-for="project in projects" :key="project.id" :project="project">
              <v-expansion-panel-header>
                <v-row align="center" justify="space-between">
                  <div class="font-weight-light text-h6 my-1">{{ project.name }}</div>

                  <div class="mr-4">
                    <v-chip small class="ml-2">
                      <v-icon small>mdi-account</v-icon>
                    </v-chip>
                    <v-text class="mx-1 text-caption">
                      {{
                        project.status
                      }}
                    </v-text>
                    <v-divider class="mx-2" vertical></v-divider>
                    <v-btn
                      small
                      dark
                      class="hidden-sm-and-down"
                      :href="project.gh_url"
                      target="_black"
                    >
                      <v-icon small>mdi-github</v-icon>Github Repo
                    </v-btn>
                  </div>
                </v-row>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <div>
                  <v-container>
                    <v-row>
                      <v-col>
                        <p class="text--secondary">{{ project.description }}</p>
                        <v-expansion-panels accordion>
                          <v-expansion-panel>
                            <v-expansion-panel-header class="font-weight-light">Read Me</v-expansion-panel-header>
                            <v-expansion-panel-content>
                              <VueShowdown
                                :markdown="project.get_readme"
                                class="overflow-x-hidden text--secondary"
                              />
                            </v-expansion-panel-content>
                          </v-expansion-panel>
                        </v-expansion-panels>
                      </v-col>
                    </v-row>
                  </v-container>
                  <v-row class="py-4" align="center" justify="space-between">
                    <div class="mr-4">
                      <v-chip small class="mr-1" v-for="pl in project.prog_lang" :key="pl">{{ pl }}</v-chip>
                    </div>
                    <div class="hidden-md-and-up">
                      <v-btn small dark :href="project.gh_url" target="_black">
                        <v-icon small>mdi-github</v-icon>Repo
                      </v-btn>
                    </div>
                  </v-row>
                </div>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import ContactForm from "@/components/ContactForm.vue";
import Loading from "@/components/Loading.vue";
import { VueShowdown } from "vue-showdown";
import axios from "axios";
export default {
  name: "ProjectsList",

  components: {
    ContactForm,
    Loading,
    VueShowdown,
  },
  data() {
    return {
      projects: [],
      isLoading: true,
    };
  },
  mounted() {
    this.getProjects();
    document.title = "Sudoer | Work";
  },

  methods: {
    async getProjects() {
      await axios
        .get("/projects/")
        .then((response) => {
          this.projects = response.data;
          this.readme_url = response.data.readme_url
          this.isLoading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

  },
};
</script>

<style>
</style>