<template>
  <v-dialog v-model="dialog" width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="mr-3" dark v-bind="attrs" v-on="on"> About Me </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">About Me</span>
      </v-card-title>
      <v-card-text>
        I am an average developer. Plenty of spaghetti code, some of it works
        and some don’t. At the end of the day, I get the job done. So I have
        spent a lot of time learning (still learning) the ins and outs of
        Python, Django, JS, and Vue.js and despite imposter syndrome, I would
        call myself a developer.
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="red darken-1" text @click="dialog = false"> Close </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "About-Me",

  data() {
    return {
      dialog: false,
    };
  },
};
</script>