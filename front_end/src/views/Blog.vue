<template>
  <div>
    <v-parallax dark src="../assets/img/blog-main-banner.jpg">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 text-md-h2 font-weight-light mb-4">Articles</h1>
          <div class="mx-4">
            <p class="mb-0">
              Read  some of my improvised articles.
            </p>
            <p>Maybe you will get something useful from it.</p>
          </div>
          <About />
          <ContactForm />
        </v-col>
      </v-row>
    </v-parallax>
    <v-row align="center" justify="center">
      <v-chip class=""> All Articles </v-chip>
    </v-row>
    <Loading :isLoading="isLoading" />
    <v-row v-show="!isLoading" align="center" justify="center">
      <v-container>
        <v-row no-gutters>
          <ArticleBox
            cols="12"
            sm="3"
            v-for="article in articles"
            :key="article.id"
            :article="article"
          >
          </ArticleBox>
        </v-row>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import ArticleBox from "@/components/blog/ArticleBox.vue";
import Loading from "@/components/Loading.vue";
import ContactForm from "@/components/ContactForm.vue";
import About from "@/components/About.vue";

export default {
  name: "BlogList",

  components: {
    ArticleBox,
    Loading,
    ContactForm,
    About,
  },

  data() {
    return {
      articles: [],
      isLoading: true,
    };
  },

  mounted() {
    this.getArticles();
    document.title = "Sudoer | Blog";
  },

  methods: {
    async getArticles() {
      await axios
        .get("/blogs")
        .then((response) => {
          this.articles = response.data;
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