<template>
  <div class="HotTopMain">
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header">
          <span>微博</span>
        </div>
      </template>
      <div class="item_body">
        <div v-for="item in weibo_list" :key="item" class="item">
          <div class="item_idx">
            {{ item['idx'] + 1 }}
          </div>
          <el-link :href="'https://s.weibo.com/weibo?q=%23'+item['item']['note'] + '%23'" target="_blank"
                   class="item_link">
            {{ item['item']['note'] }}
          </el-link>
        </div>
      </div>
    </el-card>
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header">
          <span>百度</span>
        </div>
      </template>
      <div class="item_body">
        <div v-for="item in baidu_list" :key="item" class="item">
          <div class="item_idx">
            {{ item['idx'] + 1 }}
          </div>
          <el-link :href="'https://s.weibo.com/weibo?q=%23'+item['item']['note'] + '%23'" target="_blank"
                   class="item_link">
            {{ item['item']['note'] }}
          </el-link>
        </div>
      </div>
    </el-card>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      weibo_list: [],
      baidu_list: []
    }
  },
  methods: {
    get_data() {
      axios.get("http://localhost:8000/home/hot_top?spider_type=weibo").then(res => {
        for (let i = 0; i < res.data.data.length; i++) {
          this.weibo_list.push({idx: i, item: res.data.data[i]})
        }
        console.log(this.weibo_list)
      }).catch(res => {
        console.log(res.message)
      })
      axios.get("http://localhost:8000/home/hot_top?spider_type=baidu").then(res => {
        for (let i = 0; i < res.data.data.length; i++) {
          this.baidu_list.push({idx: i, item: res.data.data[i]})
        }
      })

    }
  },
  created() {
    this.get_data()
  }
}
</script>
<style scoped>
.HotTopMain {
  width: 1000px;
  margin: 0 auto;
  padding-top: 30px;
  display: flex;
}

.hot-top-card {
  width: 300px;
  margin: 0 10px;
}

.hot-top-card .item {
  display: flex;
}

.item_link {
  justify-content: flex-start;
  overflow: hidden;
}

.item {
  text-wrap: normal;
}

.item_idx {
  width: 30px;
  color: #9195A3;
  text-align: center;
}
</style>