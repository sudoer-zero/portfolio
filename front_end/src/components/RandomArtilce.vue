<template>
  <div class="w-11/12 lg:w-5/6 mx-auto my-2 md:my-5 text-third">
    <div class="mx-0 md:mx-4">
      <div
        class="grid grid-cols-4 gap-2"
        v-for="article in articles"
        :key="article.id"
        :article="article"
      >
        <div class="col-span-4 md:col-span-1">
          <div>
            <img class="rounded h-fit w-fit" :src="article.get_image" alt="" />
          </div>
        </div>
        <div class="col-span-4 md:col-span-3 py-2 md:py-5">
          <div>
            <h1
              class="
                mx-2
                text-2xl
                md:text-4xl
                lg:text-7xl
                font-display font-semibold
              "
            >
              {{ article.title }}
            </h1>
          </div>
          <div class="my-2 md:my-5 mx-2">
            <p class="text-xl font-paragraph">{{ article.description }}</p>
          </div>
          <div class="flex justify-center md:justify-start">
            <div
              class="flex bg-white px-3 py-2 mx-2 rounded"
              v-for="tag in article.tags"
              :key="tag"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mt-1"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z"
                  clip-rule="evenodd"
                />
              </svg>
              <span class="font-display font-semibold mx-1 capitalize">{{
                tag
              }}</span>
            </div>
          </div>
          <div class="flex justify-center md:justify-end">
            <span
              class="
                font-display
                px-8
                md:px-4
                py-2
                font-semibold
                rounded
                bg-fourth
                hover:bg-third hover:text-fourth
                mt-2
                md:mt-0
              "
            >
              <router-link to="/blogs">Read More</router-link>
            </span>
          </div>
        </div>
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
  },

  methods: {
    async getArticles() {
      await axios
        .get("/blogs/random-article")
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
