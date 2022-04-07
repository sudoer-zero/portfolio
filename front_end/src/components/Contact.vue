<template>
  <div id="bg" class="font-display px-2 md:px-5 text-first bg-third my-5 md:my-10">
    <div class="w-11/12 md:w-5/6 mx-auto font-semibold">
      <form v-on:submit.prevent="onSubmit" class="py-5 px-2 md:px-10 text-fourth">
        <div class="grid grid-cols-2 gap-2">
          <div class="col-span-2 md:col-span-1">
            <input
              v-model="name"
              type="text"
              placeholder="NAME"
              class="
                text-third
                font-semibold
                p-3
                mt-2
                mb-4
                w-full
                bg-first
                border-2 border-first
                focus:border-third focus:outline-none
                rounded
              "
            />
          </div>
          <div class="col-span-2 md:col-span-1">
            <input
              v-model="email"
              type="email"
              placeholder="E-MAIL"
              class="
                text-third
                font-semibold
                p-3
                mt-2
                mb-4
                w-full
                bg-first
                border-2 border-first
                focus:border-third focus:outline-none
                rounded
              "
            />
          </div>
        </div>
        <div>
          <textarea
            v-model="message"
            name="message"
            placeholder="MESSAGE"
            class="
              text-third
              font-semibold
              p-3
              mt-2
              mb-4
              h-40
              md:h-60
              w-full
              bg-first
              border-2 border-first
              focus:border-third focus:outline-none
              rounded
            "
          ></textarea>
        </div>
        <button
          type="submit"
          class="
            text-third
            font-semibold
            p-3
            mt-2
            w-full
            bg-fourth
            border-2 border-first
            focus:border-third focus:outline-none
            rounded
          "
        >
          Send
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Contact",

  data() {
    return {
      name: "",
      email: "",
      message: "",
    };
  },

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
          this.$router.push("/thanks");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
#bg {
  background-image: url("../../public/bg.svg");
}
</style>