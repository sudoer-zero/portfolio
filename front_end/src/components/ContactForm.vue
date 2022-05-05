<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on">
        <v-icon class="pr-1" small>mdi-message</v-icon> Contact
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Contact Form</span>
      </v-card-title>
      <v-card-text>
        <v-form v-model="valid" v-on:submit.prevent="onSubmit">
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="name"
                  label="Name*"
                  :rules="nameRules"
                  :counter="20"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Email*"
                  type="email"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  v-model="message"
                  :rules="messageRules"
                  :counter="200"
                  label="Message*"
                  type="textarea"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <v-card-actions>
            <small>*indicates required field</small>
        <v-spacer></v-spacer>
        <v-btn color="red darken-1" text @click="dialog = false"> Close </v-btn>
        <v-btn color="primary" type="submit" > Send </v-btn>
      </v-card-actions>
        </v-form>

        
      </v-card-text>
      
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  name: "Contact-Form",

  data: () => ({

    valid: false,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => v.length <= 20 || 'Name must be less than 20 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
    message: '',
    messageRules: [
      v => !!v || 'Message is required',
      v => v.length <= 200 || 'Message must be less than 200 characters',
    ],
    dialog: false,
  }),

  methods: {
    onSubmit() {
      const formData = {
        name: this.name,
        email: this.email,
        message: this.message,
      };
      axios({
        method: "POST",
        url: "/contact/",
        headers: { "Content-Type": "application/json" },
        data: formData,
      })
        .then(() => {
          this.dialog = !this.dialog;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>