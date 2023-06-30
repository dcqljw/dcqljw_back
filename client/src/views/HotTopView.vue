<template>
  <div class="HotTopMain">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>weibo</span>
        </div>
      </template>
      <div v-for="item in weibo_list" :key="item" class="text item">{{ item['idx'] + 1}}&nbsp;{{item['item']['note']}}</div>
    </el-card>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      weibo_list: []
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
}
</style>