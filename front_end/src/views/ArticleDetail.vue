<template>
  <div class="mt-5">
    <Loading :isLoading="isLoading" />
    <v-container v-show="!isLoading">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="6">
          <div>
            <h1>{{ title }}</h1>
            <v-row class="my-3 mx-2 grey--text" align="center">
              <v-chip small><v-icon small>mdi-account</v-icon></v-chip>
              <v-text class="mx-1">Sudoer Zero</v-text>
              <span>•</span>
              <v-text class="mx-1">{{ creation_date }}</v-text>
            </v-row>
            <v-divider></v-divider>
            <v-card class="mx-auto my-3">
              <v-img :src="image" class="overflow-x-auto"></v-img>
            </v-card>
            <VueShowdown :markdown="content" class="overflow-x-hidden" />
            <v-divider></v-divider>
            <div class="mx-auto mt-2">
              <v-row align="center" justify="center">
                <v-col cols="12" sm="6">
                  <div class="d-flex justify-center">
                    <v-chip v-for="tag in tags" :key="tag" class="mx-1">
                      <v-icon small>mdi-tag</v-icon>
                      {{ tag }}</v-chip
                    >
                  </div>
                </v-col>
                <v-col cols="12" sm="6">
                  <div class="d-flex justify-center">
                    <v-btn
                      class="mx-2"
                      color="amber lighten-3"
                      light
                      @click="postHappy()"
                      >{{ happy }}
                      <v-icon small class="mx-2"
                        >mdi-emoticon-happy-outline</v-icon
                      ></v-btn
                    >
                    <v-btn
                      class="mx-2"
                      color="pink lighten-3"
                      light
                      @click="postHeart()"
                      >{{ heart }}
                      <v-icon small class="mx-2">
                        mdi-heart-outline</v-icon
                      ></v-btn
                    >
                    <v-btn
                      class="mx-2"
                      color="blue lighten-3"
                      light
                      @click="postLike()"
                      >{{ like }}
                      <v-icon small class="mx-2">
                        mdi-thumb-up-outline</v-icon
                      ></v-btn
                    >
                  </div>
                </v-col>
              </v-row>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Loading from "@/components/Loading.vue";
import { VueShowdown } from "vue-showdown";

import axios from "axios";
export default {
  name: "ArticleDetail",

  data() {
    return {
      id: "",
      title: "",
      content: "",
      image: "",
      tags: [],
      like: "",
      heart: "",
      happy: "",
      creation_date: "",
      isLoading: true,
    };
  },

  components: {
    Loading,
    VueShowdown,
  },

  mounted() {
    this.getArticleDetail();
  },

  methods: {
    async getArticleDetail() {
      const article_slug = this.$route.params.article_slug;
      await axios
        .get(`blogs/${article_slug}/`)
        .then((response) => {
          document.title = "Blogs | " + response.data.title;
          this.id = response.data.id;
          this.title = response.data.title;
          this.content = response.data.content;
          this.image = response.data.get_image;
          this.tags = response.data.tags;
          this.like = response.data.like;
          this.heart = response.data.heart;
          this.happy = response.data.happy;
          this.creation_date = response.data.creation_date;
          this.isLoading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    postHeart() {
      axios
        .post(`/blogs/${this.id}/heart/`, this.heart)
        .then(this.heart++)
        .catch((err) => {
          console.log(err);
        });
    },

    postLike() {
      axios
        .post(`/blogs/${this.id}/like/`, this.like)
        .then(this.like++)
        .catch((err) => {
          console.log(err);
        });
    },

    postHappy() {
      axios
        .post(`/blogs/${this.id}/happy/`, this.happy)
        .then(this.happy++)
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>