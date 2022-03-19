<template>
  <div class="font-display">
    <div class="w-5/6 mx-auto">
      <form v-on:submit.prevent="onSubmit">
        <div class="grid grid-cols-2 gap-2">
          <div class="col-span-2 md:col-span-1 ">
            <label class="uppercase text-sm opacity-70 px-2">Name</label>
					  <input v-model="name" type="text" class="p-3 mt-2 mb-4 w-full bg-slate-200 border-2 border-slate-200 focus:border-slate-400 focus:outline-none">
          </div>
          <div class="col-span-2 md:col-span-1">
            <label class="uppercase text-sm opacity-70 px-2">Email</label>
					  <input v-model="email" type="email" class="p-3 mt-2 mb-4 w-full bg-slate-200 border-2 border-slate-200 focus:border-slate-400 focus:outline-none">
          </div>
        </div>
        <div>
          <label class="uppercase text-sm opacity-70 px-2">Message</label>
          <textarea v-model="message" name="message" class="p-3 mt-2 mb-4 h-40 md:h-60 w-full bg-slate-200 border-2 border-slate-200 focus:border-slate-400 focus:outline-none"></textarea>
        </div>
        <button type="submit" class="p-3 mt-2 mb-4 w-full bg-slate-200 border-2 border-slate-200 focus:border-slate-400 focus:outline-none">Send</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'Contact', 

  data() {
    return {
      name: "", 
      email: "",
      message: "",
    }
  },

  methods: {
    onSubmit() {
      const formData = {
      name: this.name,
      email: this.email,
      message: this.message      
      }
      axios({
        method: "POST",
        url: "/contact/",
        headers: {"Content-Type": "application/json"},
        data: formData
      })
      .then(() => { 
        this.$router.push("/thanks")
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
