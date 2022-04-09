<template>
  <Loading :isLoading="isLoading" />
  <div v-show="!isLoading" class="">
    <div v-for="article in articles"
          :key="article.id"
          :article="article">
          <router-link :to="article.get_absolute_url">
          {{ article.title}}

          </router-link>

    </div>
  </div>
</template>

<script>
import axios from "axios";
import Loading from "@/components/Loading.vue";
export default {
  name: "LatestArticles",

  data() {
    return {
      articles: [],
      logos: [],
      isLoading: true,
    };
  },

  components: {
    Loading,
  },

  mounted() {
    this.getArticles();
  },

  methods: {
    async getArticles() {
      await axios
        .get("/blogs/latest-articles/")
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
