<template>
  <div class="shadow rounded p-2 my-4 bg-first">
    <div class="flex justify-between font-display mx-0 md:mx-2 text-third">
      <div>
        <h1 class="text-3xl md:text-4xl hover:text-fourth">
          <router-link :to="article.get_absolute_url">
            {{ article.title }}
          </router-link>
        </h1>
        <p class="text-third my-1">{{ article.description }}</p>
        <p class="flex">
          <span
            class="flex font-semibold mx-1 md:mx-2 px-1 md:px-2"
            v-for="tag in article.tags"
            :key="tag"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4 m-1"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z"
                clip-rule="evenodd"
              />
            </svg>
            {{ tag }}
          </span>
        </p>
      </div>
      <div>
        <button
          @click="postLike"
          class="flex hover:bg-fourth bg-first rounded-md px-1 mx-1"
        >
          <span class="p-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"
              />
            </svg>
          </span>
          <span class="p-1 font-semibold">
            {{ like }}
          </span>
        </button>
        <button
          @click="postHeart"
          class="flex hover:bg-fourth bg-first rounded-md px-1 mx-1"
        >
          <span class="p-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
              />
            </svg>
          </span>
          <span class="p-1 font-semibold">
            {{ heart }}
          </span>
        </button>
        <button
          @click="postHappy"
          class="flex hover:bg-fourth bg-first rounded-md px-1 mx-1"
        >
          <span class="p-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </span>
          <span class="p-1 font-semibold">
            {{ happy }}
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ArticleBox",

  props: {
    article: Object,
  },

  data() {
    return {
      like: this.article.like,
      heart: this.article.heart,
      happy: this.article.happy,
      id: this.article.id,
    };
  },

  methods: {
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
