<script>


import {Hide} from "@element-plus/icons-vue";
import axios from "axios";

export default {
  name: "LoginDialog",
  computed: {
    Hide() {
      return Hide
    }
  },
  data() {
    return {
      isShow: false,
      activeName: "login",
      username: "",
      password: "",
      loading: false,
    }
  },
  methods: {
    update(Show) {
      this.isShow = Show
    },
    login() {
      this.loading = true
      axios.post("/user/login", {
        username: this.username,
        password: this.password
      }).then(res => {
        if (res.data.code === "2000") {
          this.$message.success("登录成功")
          this.isShow = false
          localStorage.setItem('userInfo', JSON.stringify(res.data.userInfo))
          localStorage.setItem('token', res.data.token)
          location.reload()
        } else {
          this.$message.error(res.data.msg)
        }
      })
      this.loading = false
    },
    register() {
      this.$message.success("注册成功")
    }
  }
}
</script>

<template>
  <div class="login-dialog">
    <el-dialog v-model="isShow" title="登录" center width="30%">
      <div>
        <el-tabs v-model="activeName" class="demo-tabs">
          <el-tab-pane label="登录" name="login" class="login">
            <el-input v-model="username" placeholder="输入用户名" size="large"/>
            <el-input v-model="password" placeholder="输入密码" size="large" show-password/>
            <el-button type="primary" @click="login" v-loading="loading">登录</el-button>
          </el-tab-pane>
          <el-tab-pane label="注册" name="register" class="register">
            <span>
              内测中暂不支持注册！！！
            </span>
            <div v-show="false">
              <el-input v-model="username" placeholder="输入用户名" size="large"/>
              <el-input v-model="password" placeholder="输入密码" size="large" show-password/>
              <el-button type="primary" @click="register">注册</el-button>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-dialog>
  </div>
</template>

<style scoped>
.login > div, .register > div {
  padding-bottom: 20px;
}

@media screen and (max-width: 900px) {
  .login-dialog :deep(.el-dialog) {
    --el-dialog-width: 100% !important;
  }
}

.login-dialog button {
  width: 100%;
}
</style>