<template>
  <el-affix>
    <el-row justify="space-between" class="header">
      <el-col :span="8" :xs="12" style="height: 100%">
        <div class="header-left">
          <div class="header-logo" @click="this.$router.push('/')">
            <el-avatar style="background: none" :src="require('@/assets/learn.png')"></el-avatar>
            Learn-Duck
          </div>
          <div class="header-menu hidden-md-and-down">
            <div :class="{ active:isActive('/') }" @click="this.$router.push('/')">首页</div>
            <div :class="{ active:isActive('/learn_group') }" @click="this.$router.push('/learn_group')">学习组</div>
            <div :class="{ active:isActive('/my_learn') }" @click="this.$router.push('/my_learn')">我的组</div>
            <div :class="{ active:isActive('/moyu') }" @click="this.$router.push('/moyu')">摸鱼</div>
          </div>
        </div>
      </el-col>
      <el-col :span="8" class="hidden-sm-and-down">
        <div class="header-center">
          <div class="header-search">
            <el-input
                v-model="search"
                size="large"
                class="w-50 m-2 search-input"
                placeholder="请输入需要搜索的内容"
                :suffix-icon="Search"
            />
          </div>
        </div>
      </el-col>
      <el-col :span="8" :xs="12">
        <div class="header-right">
          <div class="header-other hidden-md-and-down">
            <div>
              <el-switch
                  v-model="switchDarkValue"
                  :active-action-icon="View"
                  :inactive-action-icon="Hide"
                  @click="switchDark"
              />
            </div>
            <div>
              <el-icon>
                <Message/>
              </el-icon>
            </div>
            <div>
              <el-icon>
                <Calendar/>
              </el-icon>
            </div>
          </div>
          <div class="header-create hidden-md-and-down" v-if="isLogin">
            <el-button class="create_group_button" type="primary" :icon="Plus"
                       @click="this.$router.push('/create_group')">创建组
            </el-button>
          </div>
          <div class="header-user">
            <el-popover :width="100" v-if="isLogin">
              <template #reference>
                <el-avatar v-if="isLogin & userInfo.avatar !== null" :size="50"
                           :src="userInfo.avatar">{{ userInfo.username }}
                </el-avatar>
                <el-avatar v-else-if="isLogin & userInfo.avatar == null">
                  {{ userInfo.username }}
                </el-avatar>
              </template>
              <template #default>
                <div class="user-menu">
                  <div>
                    <el-link :underline="false" @click="this.$router.push('/account')">个人中心</el-link>
                  </div>
                  <div>
                    <el-link :underline="false" @click="outLogin">退出登录</el-link>
                  </div>
                </div>
              </template>
            </el-popover>
            <el-avatar v-else class="login-button" @click="showLogin">登录</el-avatar>
          </div>
        </div>
      </el-col>
    </el-row>
  </el-affix>
  <router-view></router-view>
  <div class="bottom-menu hidden-lg-and-up">
    <el-menu
        :default-active="this.$route.path"
        mode="horizontal" class="bottom-menu-m">
      <el-menu-item index="/" @click="this.$router.push('/')">
        <span class="item-menu">
          <el-icon size="25">
            <House/>
          </el-icon>
          <span>首页</span>
        </span>
      </el-menu-item>
      <el-menu-item index="/learn_group" @click="this.$router.push('/learn_group')"><span class="item-menu">
          <el-icon size="25"><ChatLineSquare/></el-icon>
          <span>组别</span>
        </span></el-menu-item>
      <el-menu-item index="/my_learn" @click="this.$router.push('/my_learn')"><span class="item-menu">
          <el-icon size="25">
            <User/>
          </el-icon>
          <span>我的</span>
        </span></el-menu-item>
      <el-menu-item index="/moyu" @click="this.$router.push('/moyu')"><span class="item-menu">
          <el-icon size="25">
            <Coffee/>
          </el-icon>
          <span>摸鱼</span>
        </span></el-menu-item>
    </el-menu>
  </div>
  <LoginDialog ref="ShowLogin"></LoginDialog>
  <el-backtop class="hidden-sm-and-down" :right="100" :bottom="150"/>
</template>

<script>

import {
  Calendar,
  ChatLineSquare,
  Coffee,
  Hide,
  House,
  Message,
  Plus,
  Search,
  User,
  View
} from "@element-plus/icons-vue";
import LoginDialog from "@/components/LoginDialog.vue";

export default {
  name: 'App',
  components: {Coffee, User, ChatLineSquare, House, Calendar, Message, LoginDialog},
  computed: {
    Hide() {
      return Hide
    },
    View() {
      return View
    },
    Plus() {
      return Plus
    },
    Search() {
      return Search
    }
  },
  data() {
    return {
      title: "",
      search: "",
      switchDarkValue: false,
      LoginShow: false,
      isLogin: false,
      userInfo: {}
    }
  },
  methods: {
    isActive(a) {
      return a === this.$route.path
    },
    showLogin() {
      this.$refs.ShowLogin.update(true)
    },
    switchDark() {
      if (this.switchDarkValue) {
        document.querySelector("html").classList.add("dark")
      } else {
        document.querySelector("html").classList.remove("dark")
      }
    },
    outLogin() {
      localStorage.clear()
      this.$router.push("/")
      location.reload()
    }
  },
  created() {
    document.cookie = "key=asdf;path=/;domain=baidu.com;max-age=session"
    console.log("未登录")
  },
  mounted() {
    if (localStorage.getItem("userInfo")) {
      this.isLogin = true
      this.userInfo = JSON.parse(localStorage.getItem("userInfo"))
    } else {
      console.log("未登录")
    }
  }
}
</script>

<style>
html {
  height: 100%;
  margin: 0;
}

body {
  margin: 0;
  background-color: var(--el-bg-color);
}

.scrollbar {
  overflow-y: scroll;
  scrollbar-width: none;
}

.scrollbar::-webkit-scrollbar {
  display: none;
}

.scrollbar::-webkit-scrollbar-thumb {
  background-color: #aaa;
}

.header {
  border-bottom: 1px solid var(--el-border-color);
  background: var(--el-bg-color);
  height: 60px;
  align-items: center;
}

.header-user:hover {
  cursor: pointer;
}

.header-search {
  max-width: 500px;
  width: 100%;
}

.header-contains, .header-left, .header-center, .header-right, .header-menu, .header-other {
  display: flex;
  align-items: center;
}

.header-contains {
  justify-content: space-between;
  height: 100%;
}

.header-right {
  justify-content: flex-end;
}

.header-menu {
  height: 100%;
}

.header-menu > div {
  height: 100%;
  display: flex;
  align-items: center;
}

.header-menu > div:hover {
  cursor: pointer;
  color: var(--el-color-primary);
  border-bottom: 3px solid var(--el-color-primary);
}

.header-left div {
  padding: 0 20px;
}

.header-left {
  height: 100%;
}

.header-right > div {
  margin: 0 10px;
}

.header-other > div {
  margin: 0 10px;
}

.active {
  color: var(--el-color-primary);
  border-bottom: 3px solid var(--el-color-primary);
}

.login-button {
  color: var(--el-color-primary) !important;
}

.user-menu {
  text-align: center;
}

.user-menu div {
  margin-bottom: 5px;
}

.header-logo {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.bottom-menu {
  position: fixed;
  bottom: 0;
  width: 100%;
  border-top: 1px solid var(--el-border-color)
}

.bottom-menu-m {
  justify-content: space-evenly;
}

.bottom-menu-m li {
  line-height: 35px;
}

.item-menu {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 10px;
  text-align: center;
}

.item-menu i {
  margin: 0 auto !important;
}
</style>
