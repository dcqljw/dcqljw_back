<script>
export default {
  name: "LearnGroupView",
  data() {
    return {
      learnGroupList: [
        {
          id: "9358c5d100f85c1c5ef161571eaec056",
          title: "Learn-Duck建设组",
          description: "Learn-Duck建设小组",
          personNumber: 1,
          avatar: require('@/assets/learn-duck.png'),
          tag: ["Learn-Duck", "主站"]
        },
        {
          id: "2",
          title: "Python学习组",
          description: "Python学习",
          personNumber: 2,
          avatar: "https://www.python.org/static/favicon.ico",
          tag: ["Python"]
        },
        {
          id: "3",
          title: "Vue学习组",
          description: "Vue学习",
          personNumber: 0,
          avatar: "https://vuejs.org/logo.svg",
          tag: ["Vue"]
        }
      ]
    }
  },
  methods: {
    joinGroup(id) {
      if (localStorage.getItem("userInfo") === null) {
        this.$message.error("请先登录")
      } else {
        this.$message.success(`${id}加入成功`)
      }
    }
  }
}
</script>

<template>
  <div class="learn-group">
    <el-row>
      <el-col :span="16" :xs="24">
        <div class="learn-group-left">
          <el-card v-for="item in learnGroupList" :key="item.title">
            <div class="group-item">
              <div class="group-start">
                <div class="group-avatar">
                  <el-avatar :size="70" v-if="item.avatar === ''" shape="square">{{ item.title }}</el-avatar>
                  <el-avatar :size="70" v-else shape="square" :src="item.avatar" fit="scale-down"
                             style="background: none"></el-avatar>
                </div>
                <div class="group-item-content">
                  <div class="group-item-title">
                    <el-link :underline="false" @click="this.$router.push('/group_detail/'+item.id+'/groupIndex')">
                      {{ item.title }}
                    </el-link>
                    <el-tag v-for="tag in item.tag" :key="tag" size="small">{{ tag }}</el-tag>
                  </div>
                  <div>
                    <el-text>{{ item.description }}</el-text>
                  </div>
                </div>
              </div>
              <div class="group-item-right">
                <div class="group-item-person">
                  <el-tag type="success" size="small">{{ item.personNumber }}人</el-tag>
                </div>
                <el-button @click="joinGroup(item.id)">申请加入</el-button>
              </div>
            </div>
          </el-card>
        </div>
      </el-col>
      <el-col :span="8" class="hidden-sm-and-down">
        <div class="learn-group-right">
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
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.learn-group {
  width: 1200px;
  margin: 0 auto;
}

.group-item {
  display: flex;
  justify-content: space-between;
}

.group-start {
  display: flex;
}

.group-item-content {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.group-item-right {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.learn-group-left > div {
  margin-bottom: 10px;
  margin-right: 10px;
  margin-left: 10px;
}

.learn-group {
  margin-top: 20px;
}

.group-item-person {
  display: flex;
  justify-content: flex-end;
}

.group-item-title > span {
  margin-left: 5px;
}

.group-content {
  display: flex;
}

.top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.learn-group-right > div {
  margin-bottom: 10px;
}

.group-item-title > a {
  font-size: 18px;
}

.group-title {
  margin-left: 10px;
}

@media screen and (max-width: 1200px) {
  .learn-group {
    width: auto;
  }
}
</style>