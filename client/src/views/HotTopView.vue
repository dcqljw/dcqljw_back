<template>
  <div class="hot-top-main">
    <h1 class="title">热搜</h1>
    <el-tabs v-model="activeName" class="demo-tabs">
      <el-tab-pane label="我的关注" name="我的关注"></el-tab-pane>
      <el-tab-pane label="全部" name="all">
        <div class="hot-top-content">
          <div class="select-menu">
            <el-menu
                default-active="baidu"
                class="el-menu-vertical-demo"
                :collapse="isCollapse"
            >
              <el-menu-item :index="key" :name="key" v-for="(hot,key) in hot_top" :key="key.id" @click="show">
                <el-icon>
                  <el-image style="width: 20px" :src="hot_config[key]['icon']"/>
                </el-icon>
                <!--                <div>{{hot_config[key]['label']}}</div>-->
                <template #title>
                  <div style="width: 56px">{{ hot_config[key]['label'] }}</div>
                </template>
              </el-menu-item>
            </el-menu>
          </div>
          <div class="content-show">
            <div class="hot-top-title">
              <el-image style="width: 30px;" :src="hot_config[show_index]['icon']"/>
              &nbsp;{{ hot_config[show_index]['label'] }}
            </div>
            <div class="hot-top-rank">
              <div v-for="(item,index) in hot_top[show_index]" :key="item" class="item">
                <div :class="'item_idx no'+(index + 1)">
                  {{ index + 1 }}
                </div>
                <el-link :href="hot_config['baidu']['hot_link'].replace('{note}',item['note'])" target="_blank"
                         class="item_link">
                  {{ item['note'] }}
                </el-link>
              </div>
            </div>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="综合" name="综合">
        <div class="hot-top-content">
          <div class="select-menu">
            <el-menu
                default-active="baidu"
                class="el-menu-vertical-demo"
                :collapse="isCollapse"
            >
              <el-menu-item :index="key" :name="key" v-for="(hot,key) in hot_top" :key="key.id" @click="show">
                <el-icon>
                  <el-image style="width: 20px" :src="hot_config[key]['icon']"/>
                </el-icon>
                <!--                <div>{{hot_config[key]['label']}}</div>-->
                <template #title>
                  <div style="width: 56px">{{ hot_config[key]['label'] }}</div>
                </template>
              </el-menu-item>
            </el-menu>
          </div>
          <div class="content-show">
            <div class="hot-top-title">
              <el-image style="width: 30px;" :src="hot_config[show_index]['icon']"/>
              &nbsp;{{ hot_config[show_index]['label'] }}
            </div>
            <div class="hot-top-rank">
              <div v-for="(item,index) in hot_top[show_index]" :key="item" class="item">
                <div :class="'item_idx no'+(index + 1)">
                  {{ index + 1 }}
                </div>
                <el-link :href="hot_config['baidu']['hot_link'].replace('{note}',item['note'])" target="_blank"
                         class="item_link">
                  {{ item['note'] }}
                </el-link>
              </div>
            </div>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      activeName: "all",
      childActive: "baidu",
      hot_top: {},
      isCollapse: false,
      show_index: "baidu",
      hot_config: {
        baidu: {
          icon: "https://baidu.com/favicon.ico",
          hot_link: "https://www.baidu.com/s?wd={note}",
          source_href: "https://baidu.com/",
          label: "百度"
        },
        weibo: {
          icon: "https://weibo.com/favicon.ico",
          hot_link: "https://s.weibo.com/weibo?q=%23{note}%23",
          source_href: "https://weibo.com/",
          label: "微博"
        },
        douyin: {
          icon: "https://douyin.com/favicon.ico",
          hot_link: "https://www.douyin.com/search/{note}",
          source_href: "https://douyin.com/",
          label: "抖音"
        },
        bilibili: {
          icon: "https://bilibili.com/favicon.ico",
          hot_link: "https://search.bilibili.com/all?keyword={note}",
          source_href: "https://bilibili.com/",
          label: "哔哩哔哩"
        },
        toutiao: {
          icon: "https://toutiao.com/favicon.ico",
          hot_link: "https://so.toutiao.com/search?keyword={note}",
          source_href: "https://toutiao.com/",
          label: "今日头条"
        }
      },
      skeleton: false
    }
  },
  methods: {
    tab_click(tab) {
      console.log(tab.paneName)
    },
    show(e) {
      console.log(e.index)
      this.show_index = e.index
    },
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
    var userAgentInfo = navigator.userAgent; // 包含有关浏览器的信息
    // 非手机端
    var Agents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
    for (var v = 0; v < Agents.length; v++) {
      if (userAgentInfo.indexOf(Agents[v]) > 0) {
        this.isCollapse = true
        break
      }
    }
  }
}
</script>
<style scoped>
.hot-top-main {
  margin: 0 auto;
  width: 90%;
}

.title {
  text-align: center;
}

:deep(.child_item .el-tabs__item) {
  justify-content: flex-start !important;
}

.hot-top-content {
//overflow: scroll; height: 500px; display: flex;
}

.hot-top-rank {
  height: 500px;
  overflow: scroll;
}

.content-show {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.hot-top-title {
  margin-left: 20px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.select-menu {
//min-width: 56px;
}

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
  display: flex;
  text-wrap: normal;
}

.item_idx {
  width: 30px;
  color: #9195A3;
  text-align: center;
}
</style>