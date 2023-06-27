<template>
  <div id="barrage">
    <div class="item" v-for="item in barrage_list" v-bind:key="item.id" v-bind:data-line="item.line"
         @transitionend="removeBullet">
      <div class="barrage_item">
        <img :src="'https://api.multiavatar.com/'+item.id+'.png'">
        <div class="barrage_text">{{ item.text }}</div>
      </div>
    </div>
    <div class="send_barrage">
      <el-input v-model="send_text" placeholder="Please input" @keydown.enter="send_barrage"/>
    </div>
  </div>
</template>
<script>
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
    }
  },
  created() {
    this.showNextBarrage()
    setInterval(this.showNextBarrage, 700)
  }
}
</script>
<style scoped>
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

.item {
  transform: translateX(-100%);
}

.item {
  transform: translateX(100vw);
}

.item {
  animation: rightToleft 10s linear both infinite;
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

@keyframes rightToleft {
  0% {
    transform: translate(100vw);
  }
  100% {
    transform: translate(-100%);
  }
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
//height: 100px; //width: 100px; //border: 1px solid; bottom: 20px; position: absolute; right: 50px;
}
</style>