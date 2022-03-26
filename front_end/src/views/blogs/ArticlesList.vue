<template>
  <div class="w-11/12 md:w-5/6 mx-auto">
    <div class="grid grid-cols-4 gap-4 mx-4">
      <div class="col-span-4 md:col-span-3">
        <h1 class="mx-0 md:mx-2 text-6xl font-display font-semibold text-third">
          Articles
        </h1>
        <ArticleBox
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </div>
      <div class="col-span-4 md:col-span-1">
        <h1
          class="font-display font-semibold text-third border-b-2 border-first"
        >
          Recent Articles
        </h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ArticleBox from "@/components/ArticleBox.vue";

export default {
  name: "ArticleList",

  data() {
    return {
      articles: [],
      isLoading: true,
    };
  },

  components: {
    ArticleBox,
  },

  mounted() {
    this.getArticles();
    document.title = "Sudoer | Blogs";
  },

  methods: {
    async getArticles() {
      await axios
        .get("/blogs/")
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
