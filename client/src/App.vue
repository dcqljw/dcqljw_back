<template>
  <h1>{{ title }}</h1>
  <!--    <router-view></router-view>-->
</template>

<script>

import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
      title: ""
    }
  },
  methods: {
    get_title() {
      axios.get("https://dcqljw.xyz:8000/home/")
          .then(message => {
            this.title = message.data
          }).catch(res => {
        console.log(res)
      })
    }
  },
  created() {
    this.get_title()
    setInterval(() => {
      this.get_title()
    }, 30000)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
