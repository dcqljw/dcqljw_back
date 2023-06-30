<template>
  <!--  <h1>{{ title }}</h1>-->
  <router-view></router-view>
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
    // this.get_title()
    // setInterval(() => {
    //   this.get_title()
    // }, 30000)
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
}

::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
 border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background-color: #0003;
  border-radius: 10px;
}
</style>
