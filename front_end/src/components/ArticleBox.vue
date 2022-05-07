<template>
  <v-card class="mx-auto my-3" max-width="344">
    <v-img :src="article.get_thumbnail" height="200px"></v-img>
    <v-card-title>
      {{ article.title }}
    </v-card-title>
    <v-card-subtitle>
      {{ article.description }}
    </v-card-subtitle>
    <v-card-actions>
      <v-chip small>{{ article.creation_date }}</v-chip>
      <v-spacer></v-spacer>
      <v-btn :to="article.get_absolute_url" small rounded color="primary">Read More</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
//import axios from "axios";
export default {
  name: "Article-Box",

  props: {
    article: Object,
  },

  data() {
    return {
      id: this.article.id,
    };
  },
};
</script>
