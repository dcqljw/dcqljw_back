<template>
  <div class="hot_top">
    <el-button type="primary" size="large" @click="this.$router.push('hot_top')">热榜</el-button>
  </div>
  <div id="barrage" v-show="false">
    <transition-group @after-enter="enter">
      <div class="item" v-for="item in barrage_list" v-bind:key="item.id" v-bind:data-line="item.line">
        <div class="barrage_item">
          <img :src="'https://api.multiavatar.com/'+item.id+'.png'">
          <div class="barrage_text">{{ item.text }}</div>
        </div>
      </div>
    </transition-group>
    <div class="send_barrage">
      <el-input v-model="send_text" placeholder="Please input" @keydown.enter="send_barrage"/>
    </div>
  </div>
</template>
<script>
import axios from "axios";

const getUUID = () => Math.random() + Math.random();
export default {
  name: 'App',
  data() {
    return {
      send_text: "",
      top: 0,
      barrage_list: [],
      waitBarrage: [],
      lines: 8,
      currentLine: 1
    }
  },
  methods: {
    showNextBarrage() {
      if (!this.waitBarrage.length) {
        return
      }
      this.currentLine = (this.currentLine % 5) + 1
      const currentBarrage = this.waitBarrage.shift()
      currentBarrage.line = this.currentLine
      this.barrage_list.push(currentBarrage)
    },
    send_barrage() {
      console.log(this.send_text)
      const new_barrage = {
        id: getUUID(),
        text: this.send_text,
        line: 0
      }
      this.waitBarrage.push(new_barrage)
      this.send_text = ""
    },
    removeBullet() {
      this.barrage_list.shift()
      console.log(this.barrage_list)
    },
    get_data() {
      axios.get("https://dcqljw.xyz:8000/home")
          .then(res => {
            console.log(res)
            for (let i = 0; i < res.data.length; i++) {
              console.log(res.data[i])
              const new_barrage = {
                id: getUUID(),
                text: res.data[i].title,
                line: 0
              }
              this.waitBarrage.push(new_barrage)
            }
          })
    },
    enter() {
      // this.barrage_list.shift()
      console.log("enter")
    }
  },
  created() {
    this.showNextBarrage()
    this.get_data()
    setInterval(this.showNextBarrage, 700)
  }
}
</script>
<style scoped>
.hot_top{
  width: 100px;
  margin: 0 auto;
  text-align: center;
}
#barrage {
  width: 100%;
  height: 100%;
  background-color: #a3a3a3;
  position: absolute;
  overflow: hidden;
}

.item {
  position: absolute;
}

.item img {
  width: 50px;
  border: 1px;
}

.barrage_item {
  display: flex;
  background-color: white;
  border-radius: 50px;
  padding-right: 20px;
  height: 50px;
}

.item[data-line='1'] {
  top: 50px;
}

.item[data-line='2'] {
  top: 150px;
}

.item[data-line='3'] {
  top: 250px;
}

.item[data-line='4'] {
  top: 350px;
}

.item[data-line='5'] {
  top: 450px;
}

.item[data-line='6'] {
  top: 550px;
}

.item[data-line='7'] {
  top: 650px;
}

.item[data-line='8'] {
  top: 750px;
}

.item {
  transform: translateX(-100%);
}

@keyframes rightToleft {
  from {
    transform: translateX(100vh);
  }
  to {
    transform: translateX(-100%);
  }
}

.v-enter-active {
  animation: rightToleft 8s linear;
}


.barrage_text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 20px;
  white-space: nowrap;
  padding-left: 13px;
}

.send_barrage {
  bottom: 20px;
  position: absolute;
  right: 50px;
}
</style>