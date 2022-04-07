<template>
  <div id="nav" class="w-11/12 md:w-5/6 mx-auto py-2 md:py-5">
    <div class="grid grid-cols-2 mx-0 md:mx-4 p-2 md:p-4 rounded shadow-lg border-2 border-fourth">
      <div class="col-span-2 justify-self-center md:justify-self-start md:col-span-1">
        <router-link to="/">
          <img class="w-40" src="../assets/logo.svg" alt="logo">
        </router-link>
      </div>
      <div class="col-span-2 md:col-span-1 font-display justify-self-center md:justify-self-end pt-3 text-third font-semibold">
        <span class="px-4">
          <router-link to="/work">WORK</router-link>
        </span>
        <span class="px-4">
          <router-link to="/logos">LOGOS</router-link>
        </span>
        <span class="px-4">
          <router-link to="/blogs">BLOGS</router-link>
        </span>
        <span class="px-4">
          <router-link to="/about">ABOUT</router-link>
        </span>
      </div>
    </div>
  </div>
</template>
<style>
#nav a {
  color: #00334E;
}
#nav a.router-link-exact-active {
  color: #EE6F57;
}
</style>
