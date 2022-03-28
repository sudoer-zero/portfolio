<template>
  <Loading :isLoading="isLoading" />
  <div v-show="!isLoading" class="w-11/12 md:w-5/6 mx-auto">
    <div class="grid grid-cols-4 gap-4 mx-4">
      <div class="col-span-4 lg:col-span-3">
        <h1 class="mx-0 md:mx-2 text-6xl font-display font-semibold text-third">
          Articles
        </h1>
        <ArticleBox
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </div>
      <div class="col-span-4 lg:col-span-1">
        <h1 class="font-display font-semibold text-third text-2xl lg:text-lg">
          Recent Logos
        </h1>
        <div class="grid md:grid-cols-3 lg:grid-cols-1">
          <LogoBox
            class="w-11/12 md:w-3/4 mx-auto"
            v-for="logo in logos"
            :key="logo.id"
            :logo="logo"
          >
          </LogoBox>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ArticleBox from "@/components/ArticleBox.vue";
import LogoBox from "@/components/LogoBox.vue";
import Loading from "@/components/Loading.vue";
export default {
  name: "ArticleList",

  data() {
    return {
      articles: [],
      logos: [],
      isLoading: true,
    };
  },

  components: {
    ArticleBox,
    LogoBox,
    Loading,
  },

  mounted() {
    this.getArticles();
    this.getLogos();
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
    async getLogos() {
      await axios
        .get("/logos/latest-logos/")
        .then((response) => {
          this.logos = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
