<script>
import {Document, List, Calendar, ChatRound, Notebook} from "@element-plus/icons-vue";


export default {
  name: "GroupDetailView",
  components: {List, Document, Calendar, ChatRound, Notebook},
  data() {
    return {
      groupInfo: {},
      currentView: "1",
      currentActive: "index"
    }
  },
  mounted() {
    this.currentActive = this.$route.name
    console.log(this.currentActive)
  },
  methods: {
    handleOpen() {

    },
    handleClose() {

    },
    select(key) {
      this.currentView = key
      console.log(this.currentView)
    }
  }
}
</script>

<template>
  <div class="group-detail">
    <el-container>
      <el-aside width="100px">
        <el-affix :offset="65">
          <div class="nav">
            <el-menu
                :default-active="currentActive"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                @select="select"
                :router="true"
            >
              <el-menu-item index="groupIndex" style="justify-content: center">
                <el-avatar :shape="'square'">Learn</el-avatar>
              </el-menu-item>
              <el-menu-item index="document">
                <el-icon>
                  <Document/>
                </el-icon>
                <template #title>文章</template>
              </el-menu-item>
              <el-menu-item index="todo">
                <el-icon>
                  <List/>
                </el-icon>
                <template #title>计划</template>
              </el-menu-item>
              <el-menu-item index="calendar">
                <el-icon>
                  <Calendar/>
                </el-icon>
                <template #title>日历</template>
              </el-menu-item>
              <el-menu-item index="chat">
                <el-icon>
                  <ChatRound/>
                </el-icon>
                <template #title>聊天</template>
              </el-menu-item>
              <el-menu-item index="note">
                <el-icon>
                  <Notebook/>
                </el-icon>
                <template #title>笔记</template>
              </el-menu-item>
            </el-menu>
          </div>
        </el-affix>
      </el-aside>
      <el-container>
        <el-main>
          <div class="view-page">
            <router-view></router-view>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.group-detail {
  display: flex;
}

.view-page {
  width: 100%;
}

.is-active {
  background: #dcdfe6;
}
</style>