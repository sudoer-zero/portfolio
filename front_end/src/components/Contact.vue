<template>
  <div class="font-display px-2 md:px-5 text-first bg-third">
    <div class="w-5/6 mx-auto font-semibold">
      <form v-on:submit.prevent="onSubmit" class="py-5 px-2 md:px-10">
        <div class="grid grid-cols-2 gap-2">
          <div class="col-span-2 md:col-span-1">
            <label class="uppercase text-sm opacity-90 px-2">Name</label>
            <input
              v-model="name"
              type="text"
              class="
                text-third
                font-semibold
                p-3
                mt-2
                mb-4
                w-full
                bg-slate-200
                border-2 border-first
                focus:border-third focus:outline-none
                rounded
              "
            />
          </div>
          <div class="col-span-2 md:col-span-1">
            <label class="uppercase text-sm opacity-90 px-2">Email</label>
            <input
              v-model="email"
              type="email"
              class="
                text-third
                font-semibold
                p-3
                mt-2
                mb-4
                w-full
                bg-slate-200
                border-2 border-first
                focus:border-third focus:outline-none
                rounded
              "
            />
          </div>
        </div>
        <div>
          <label class="uppercase text-sm opacity-90 px-2">Message</label>
          <textarea
            v-model="message"
            name="message"
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
            mb-4
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
