<template>
  <div>
    <v-row align="center" justify="center">
      <v-chip class=""> Recent Articles </v-chip>
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
import ArticleBox from "./ArticleBox.vue";
import Loading from "@/components/Loading.vue";
export default {
  name: "Recent-Articles",

  components: {
    ArticleBox,
    Loading,
  },

  data() {
    return {
      articles: [],
      isLoading: true,
    };
  },

  mounted() {
    this.getArticles();
  },

  methods: {
    async getArticles() {
      await axios
        .get("/blogs/latest-articles")
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