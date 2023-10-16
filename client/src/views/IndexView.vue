<template>
  <div class="content">
    <el-row>
      <el-col :lg="16" style="padding: 0 10px">
        <div class="article" v-for="item in article" :key="item.id">
          <el-card>
            <div class="card-header">
              <div class="user-avatar">
                <el-avatar :size="50" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"/>
              </div>
              <div class="username">{{ item.username }}</div>
              <div class="user-group">
                <el-tag>
                  {{ item.group }}
                </el-tag>
              </div>
            </div>
            <div class="card-body">
              <div class="article-title">
                <h3>
                  <el-link :underline="false"><strong>{{ item.title }}</strong></el-link>
                </h3>
              </div>
              <div class="article-content">
                <el-text>{{ item.article }}</el-text>
              </div>
            </div>
            <div class="card-bottom">
              <div class="create_date">
                <el-text class="mx-1" type="info">{{ item.create_date }}</el-text>
              </div>
              <el-divider direction="vertical"/>
              <div class="like">
                {{ item.like }}
              </div>
              <el-divider direction="vertical"/>
              <div class="start">
                <el-icon :size="15">
                  <Star/>
                </el-icon>
                {{ item.star }}
              </div>
              <el-divider direction="vertical"/>
              <div class="comment">
                <el-icon>
                  <ChatLineSquare/>
                </el-icon>
                {{ item.comment }}
              </div>
            </div>
          </el-card>
        </div>
      </el-col>
      <el-col :lg="8" class="hidden-sm-and-down">
        <el-affix :offset="80">
          <div class="right-content">
            <div class="group-top">
              <el-card>
                <template #header>
                  <div class="top-header">
                    <span>🔥 活跃组</span>
                    <el-link type="primary">更多</el-link>
                  </div>
                </template>
                <div class="group-content">
                  <el-avatar shape="square" style="background: none" :src="require('@/assets/learn-duck.png')"/>
                  <div class="group-title">
                    <el-link :underline="false">Learn-Duck建设组</el-link>
                  </div>
                </div>
                <el-divider/>
                <div class="group-content">
                  <el-avatar shape="square" style="background: none" src="https://www.python.org/static/favicon.ico"/>
                  <div class="group-title">
                    <el-link :underline="false">Python学习组</el-link>
                  </div>
                </div>
              </el-card>
            </div>
            <div class="recommend-top">
              <el-card>
                <template #header>
                  <div class="top-header">
                    <span>推荐组</span>
                    <el-link type="primary">更多</el-link>
                  </div>
                </template>
                <div class="group-content">
                  <el-avatar shape="square" style="background: none" :src="require('@/assets/learn-duck.png')"/>
                  <div class="group-title">
                    <el-link :underline="false">Learn-Duck建设组</el-link>
                  </div>
                </div>
                <el-divider/>
                <div class="group-content">
                  <el-avatar style="background: none" shape="square" src="https://www.python.org/static/favicon.ico"/>
                  <div class="group-title">
                    <el-link :underline="false">Python学习组</el-link>
                  </div>
                </div>
              </el-card>
            </div>
          </div>
        </el-affix>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import {ChatLineSquare, Star} from "@element-plus/icons-vue";

export default {
  name: 'App',
  components: {ChatLineSquare, Star},
  data() {
    return {
      article: [
        {
          id: 1,
          avatar: "https://api.multiavatar.com/Python",
          username: "Learn-Duck",
          group: "Learn-Duck建设组",
          title: "Python学习路线",
          article: "python学习路线\n1.ahsdiufsa",
          create_date: "2023-09-04 23:04",
          like: "1000",
          star: "30",
          comment: "40"
        },
        {
          id: 2,
          avatar: "https://api.multiavatar.com/afasf",
          username: "dcq",
          group: "Python学习组",
          article: "demo",
          title: "Demo",
          create_date: "2023-09-04 23:04",
          like: "1000",
          star: "30",
          comment: "40"
        }, {
          id: 3,
          avatar: "https://api.multiavatar.com/sasdf",
          username: "ljw",
          group: "learn-duck建设组",
          title: "Vue.js",
          article: "demo",
          create_date: "2023-09-04 23:04",
          like: "1000",
          star: "30",
          comment: "40"
        },
        {
          id: 4,
          avatar: "https://api.multiavatar.com/sasdf",
          username: "ljw",
          group: "learn-duck建设组",
          title: "Vue.js",
          article: "demo",
          create_date: "2023-09-04 23:04",
          like: "1000",
          star: "30",
          comment: "40"
        },
      ]
    }
  },
  methods: {},
  created() {
  },
  mounted() {
  }
}
</script>
<style scoped>

.content {
  width: 1200px;
  margin: 20px auto 0;
  padding-bottom: 60px;
}

.article {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  align-items: center;
}

.card-body {
  margin: 20px 0;
}

.article-title {
  font-weight: bold;
}

.card-bottom {
  display: flex;
  font-size: 14px;
}

.username {
  margin-left: 10px;
  margin-right: 10px;
}

.right-content > div {
  margin-bottom: 20px;
}

.group-content {
  display: flex;
  align-items: center;
}

.group-title {
  font-size: 15px;
  margin-left: 10px;
}

.top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media screen and (max-width: 1200px) {
  .content {
    width: auto;
  }
}

</style>