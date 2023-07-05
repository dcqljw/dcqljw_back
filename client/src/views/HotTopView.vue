<template>
  <div>
    <h1 class="page_title">全网热搜</h1>
  </div>
  <div class="HotTopMain">
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>微博</span>
          <span class="time_show">{{ weibo_time }}</span>
          <span class="source_link"><a href="https://weibo.com" target="_blank">数据来源:https://weibo.com</a></span>
        </div>
      </template>
      <el-skeleton :loading="skeleton" animated>
        <template #default>
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
        </template>
        <template #template>
          <el-skeleton-item variant="text" style="width: 100%;height: 30px;margin: 10px 0"
                            v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i"/>
        </template>
      </el-skeleton>

    </el-card>
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>百度</span>
          <span class="time_show">{{ baidu_time }}</span>
          <span class="source_link"><a href="https://baidu.com" target="_blank">数据来源:https://baidu.com</a></span>
        </div>
      </template>
      <el-skeleton :loading="skeleton" animated>
        <template #default>
          <div class="item_body">
            <div v-for="item in baidu_list" :key="item" class="item">
              <div class="item_idx">
                {{ item['idx'] + 1 }}
              </div>
              <el-link :href="'https://www.baidu.com/s?wd='+item['item']['note'] + '%23'" target="_blank"
                       class="item_link">
                {{ item['item']['note'] }}
              </el-link>
            </div>
          </div>
        </template>
        <template #template>
          <el-skeleton-item variant="text" style="width: 100%;height: 30px;margin: 10px 0"
                            v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i"/>
        </template>
      </el-skeleton>
    </el-card>
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>抖音</span>
          <span class="time_show">{{ douyin_time }}</span>
          <span class="source_link"><a href="https://douyin.com" target="_blank">数据来源:https://douyin.com</a></span>
        </div>
      </template>
      <el-skeleton :loading="skeleton" animated>
        <template #default>
          <div class="item_body">
            <div v-for="item in douyin_list" :key="item" class="item">
              <div class="item_idx">
                {{ item['idx'] + 1 }}
              </div>
              <el-link :href="'https://www.douyin.com/search/'+item['item']['note']" target="_blank"
                       class="item_link">
                {{ item['item']['note'] }}
              </el-link>
            </div>
          </div>
        </template>
        <template #template>
          <el-skeleton-item variant="text" style="width: 100%;height: 30px;margin: 10px 0"
                            v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i"/>
        </template>
      </el-skeleton>
    </el-card>
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>哔哩哔哩</span>
          <span class="time_show">{{ bilibili_time }}</span>
          <span class="source_link"><a href="https://bilibili.com"
                                       target="_blank">数据来源:https://bilibili.com</a></span>
        </div>
      </template>
      <el-skeleton :loading="skeleton" animated>
        <template #default>
          <div class="item_body">
            <div v-for="item in bilibili_list" :key="item" class="item">
              <div class="item_idx">
                {{ item['idx'] + 1 }}
              </div>
              <el-link :href="'https://search.bilibili.com/all?keyword='+item['item']['note']" target="_blank"
                       class="item_link">
                {{ item['item']['note'] }}
              </el-link>
            </div>
          </div>
        </template>
        <template #template>
          <el-skeleton-item variant="text" style="width: 100%;height: 30px;margin: 10px 0"
                            v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i"/>
        </template>
      </el-skeleton>
    </el-card>
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>今日头条</span>
          <span class="time_show">{{ toutiao_time }}</span>
          <span class="source_link"><a href="https://toutiao.com"
                                       target="_blank">数据来源:https://toutiao.com</a></span>
        </div>
      </template>
      <el-skeleton :loading="skeleton" animated>
        <template #default>
          <div class="item_body">
            <div v-for="item in toutiao_list" :key="item" class="item">
              <div class="item_idx">
                {{ item['idx'] + 1 }}
              </div>
              <el-link :href="'https://so.toutiao.com/search?keyword='+item['item']['note']" target="_blank"
                       class="item_link">
                {{ item['item']['note'] }}
              </el-link>
            </div>
          </div>
        </template>
        <template #template>
          <el-skeleton-item variant="text" style="width: 100%;height: 30px;margin: 10px 0"
                            v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i"/>
        </template>
      </el-skeleton>
    </el-card>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      weibo_list: [],
      weibo_time: "",
      baidu_list: [],
      baidu_time: "",
      douyin_list: [],
      douyin_time: "",
      bilibili_list: [],
      bilibili_time: "",
      toutiao_list: [],
      toutiao_time: "",
      skeleton: true
    }
  },
  methods: {

    send_data(spider_type) {
      return axios.get("home/hot_top?spider_type=" + spider_type).catch(() => {
      })
    },
    get_datas() {
      const _this = this
      axios.all([
        _this.send_data("weibo"),
        _this.send_data("douyin"),
        _this.send_data("baidu"),
        _this.send_data("bilibili"),
        _this.send_data("toutiao")])
          .then(axios.spread(function (res1, res2, res3, res4, res5) {
                for (let i = 0; i < res1.data.data.length; i++) {
                  _this.weibo_list.push({idx: i, item: res1.data.data[i]})
                  _this.weibo_time = res1.data.data[i]['crawl_time'].replace("T", " ")
                }
                for (let i = 0; i < res2.data.data.length; i++) {
                  _this.douyin_list.push({idx: i, item: res2.data.data[i]})
                  _this.douyin_time = res2.data.data[i]['crawl_time'].replace("T", " ")
                }
                for (let i = 0; i < res3.data.data.length; i++) {
                  _this.baidu_list.push({idx: i, item: res3.data.data[i]})
                  _this.baidu_time = res3.data.data[i]['crawl_time'].replace("T", " ")
                }
                for (let i = 0; i < res4.data.data.length; i++) {
                  _this.bilibili_list.push({idx: i, item: res4.data.data[i]})
                  _this.bilibili_time = res4.data.data[i]['crawl_time'].replace("T", " ")
                }
                for (let i = 0; i < res5.data.data.length; i++) {
                  _this.toutiao_list.push({idx: i, item: res5.data.data[i]})
                  _this.toutiao_time = res5.data.data[i]['crawl_time'].replace("T", " ")
                }
                _this.skeleton = false
              })
          ).catch(error => {
        return error
      })
    },
  },
  created() {
    this.get_datas()
  }
}
</script>
<style scoped>
.no1 {
  color: red;
}

.no2 {

}

.no3 {

}

.page_title {
  text-align: center;
}

.source_link {
  position: absolute;
  top: 17px;
  right: -12px;

}

.time_show {
  font-size: 10px;
  position: absolute;
  top: -10px;
  right: -14px;
}

.source_link a {
  color: #919191;
  font-style: oblique;
}

.HotTopMain {
  margin: 0 auto;
  padding-top: 30px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.hot-top-card {
  width: 300px;
  margin: 10px 10px;
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