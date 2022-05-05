<template>
  <v-card class="mx-auto my-3">
    <v-img
      height="200px"
      width="200px"
      :src="logo.get_thumbnail"
      class="align-end"
    >
      <v-card-title>
        <v-row justify="space-around" class="pb-1">
          <v-dialog v-model="dialog" persistent max-width="500">
            <template v-slot:activator="{ on, attrs }">
              <v-btn small v-bind="attrs" v-on="on">Show</v-btn>
              <v-btn @click="postStar()" small color="primary">
                {{ star }} Stars
              </v-btn>
            </template>
            <v-card>
              <v-img
                height="500px"
                width="500px"
                :src="logo.get_image"
                class="align-end m-4"
              ></v-img>
              <v-card-actions>
                <v-text-card>Client: {{ logo.client }}</v-text-card>
                <v-spacer></v-spacer>
                <v-btn color="red darken-1" small text @click="dialog = false">
                  Close
                </v-btn>
                <v-btn @click="postStar()" small color="primary">
                  {{ star }} Stars
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </v-card-title>
    </v-img>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "Logo-Box",

  props: {
    logo: Object,
  },

  data() {
    return {
      id: this.logo.id,
      star: this.logo.star,
      dialog: false,
    };
  },

  methods: {
    postStar() {
      axios
        .post(`/logos/${this.id}/star/`, this.star)
        .then(this.star++)
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
