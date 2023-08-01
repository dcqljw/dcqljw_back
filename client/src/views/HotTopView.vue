<template>
  <div>
    <h1 class="page_title">全网热搜</h1>
  </div>
  <div class="HotTopMain">
    <el-card class="hot-top-card" body-style="height:500px;overflow: auto;padding: 10px 2px;"
             v-for="(hot,key) in hot_top"
             :key="key.id">
      <template #header>
        <div class="card-header" style="position: relative">
          <span>
            <el-image style="width: 30px;" :src="hot_config[key]['icon']"/>
          </span>
          <span class="time_show">{{ hot[0]['crawl_time'].substr(11) }}</span>
          <span class="source_link"><a :href="hot_config[key]['source_href']"
                                       target="_blank">数据来源{{ hot_config[key]['source_href'] }}</a></span>
        </div>
      </template>
      <!--      <el-skeleton :loading="skeleton" animated>-->
      <el-skeleton :loading="false" animated>
        <template #default>
          <div class="item_body">
            <div v-for="(item,index) in hot" :key="item" class="item">
              <div :class="'item_idx no'+(index + 1)">
                {{ index + 1 }}
              </div>
              <el-link :href="hot_config[key]['hot_link'].replace('{note}',item['note'])" target="_blank"
                       class="item_link">
                {{ item['note'] }}
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
      hot_top: {},
      hot_config: {
        baidu: {
          icon: "https://baidu.com/favicon.ico",
          hot_link: "https://www.baidu.com/s?wd={note}",
          source_href: "https://baidu.com/"
        },
        weibo: {
          icon: "https://weibo.com/favicon.ico",
          hot_link: "https://s.weibo.com/weibo?q=%23{note}%23",
          source_href: "https://weibo.com/"
        },
        douyin: {
          icon: "https://douyin.com/favicon.ico",
          hot_link: "https://www.douyin.com/search/{note}",
          source_href: "https://douyin.com/"
        },
        bilibili: {
          icon: "https://bilibili.com/favicon.ico",
          hot_link: "https://search.bilibili.com/all?keyword={note}",
          source_href: "https://bilibili.com/"
        },
        toutiao: {
          icon: "https://toutiao.com/favicon.ico",
          hot_link: "https://so.toutiao.com/search?keyword={note}",
          source_href: "https://toutiao.com/"
        }
      },
      skeleton: false
    }
  },
  methods: {
    get_datas() {
      axios.get(
          'home/hot_top?spider_type_list=baidu_weibo_douyin_bilibili_toutiao'
      ).then(res => {
        console.log(res)
        const data = res.data.data
        for (const key in data) {
          console.log(data[key])
          this.hot_top[key] = data[key]
        }
        console.log(this.hot_top)
      }).catch(() => {
        this.$message.error("加载失败")
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
  color: #FE2D46 !important;
}

.no2 {
  color: #F60 !important;
}

.no3 {
  color: #FAA90E !important;
}

.page_title {
  text-align: center;
}

.source_link {
  position: absolute;
  top: 17px;
  right: -12px;
  font-size: 10px;

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