<template>
  <div class="w-5/6 mx-auto py-4 border-b-2 border-slate-300">
    <div class="grid grid-cols-2 mx-4">
      <div class="col-span-2 justify-self-center md:justify-self-start md:col-span-1">
        <router-link to="/">
          <img class="w-40" src="../assets/logo.svg" alt="logo">
        </router-link>
      </div>
      <div class="col-span-2 md:col-span-1 font-display justify-self-center md:justify-self-end pt-3">
        <span class="px-4">
          <router-link to="/apps">APPS</router-link>
        </span>
        <span class="px-4">
          <router-link to="/logos">LOGOS</router-link>
        </span>
        <span class="px-4">
          <router-link to="/blog">BLOG</router-link>
        </span>
        <span class="px-4">
          <router-link to="/about">ABOUT</router-link>
        </span>
      </div>
    </div>
  </div>
</template>
