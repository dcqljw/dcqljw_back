<script>
export default {
  name: "AccountView",
  data() {
    return {
      userInfo: {},
      showUpdatePassword: false,
      showDelete: false,
      newPassword: ""
    }
  },
  methods: {
    updatePassword() {
      this.$message.success("修改成功")
      this.showUpdatePassword = false
    },
    deleteAccount() {
      this.$message.success("删除成功")
      this.showDelete = false
      localStorage.clear()
      // location.reload()
      this.$router.push("/")
    }
  },
  mounted() {
    let userInfo = localStorage.getItem("userInfo")
    if (userInfo !== null) {
      userInfo = JSON.parse(userInfo)
      this.userInfo = userInfo
    } else {
      this.$router.push("/")
    }
  }
}
</script>

<template>
  <div class="account">
    <div class="title"><h2>个人中心</h2></div>
    <el-tabs :tab-position="'left'" class="demo-tabs">
      <el-tab-pane label="个人资料">
        <div class="user-info">
          <div>
            <div class="user-info-left">
              <el-avatar v-if="userInfo.avatar === null" :size="80">{{ userInfo.username }}</el-avatar>
              <el-avatar v-else :size="80"></el-avatar>
            </div>
            <el-button type="success" size="small">更改头像</el-button>
          </div>
          <el-divider/>
          <div>
            <div class="user-info-left">
              <el-text>昵称</el-text>
            </div>
            <el-input v-model="userInfo.username"></el-input>
          </div>
          <el-divider/>
          <div>
            <div class="user-info-left">
              <el-text>邮箱</el-text>
            </div>
            <el-input v-model="userInfo.email"></el-input>
          </div>
          <el-divider/>
          <div>
            <div class="user-info-left">
              <el-text>修改密码</el-text>
            </div>
            <el-button type="danger" size="small" @click="showUpdatePassword = true">
              修改密码
            </el-button>
          </div>
          <el-divider/>
        </div>
      </el-tab-pane>
      <el-tab-pane label="账号管理">
        <el-text>
          删除账号，将清空账号所有数据信息，不可恢复！！
        </el-text>
        <el-button type="danger" @click="showDelete = true">删除账号</el-button>
      </el-tab-pane>
    </el-tabs>
    <el-dialog
        v-model="showUpdatePassword"
        title="修改密码"
        width="30%"
    >
      <el-input v-model="newPassword" placeholder="密码" type="password"></el-input>
      <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="updatePassword">
          确认
        </el-button>
      </span>
      </template>
    </el-dialog>
    <el-dialog
        v-model="showDelete"
        title="删除账号"
        width="30%"
    >
      <el-text>请输入密码</el-text>
      <el-input v-model="newPassword" placeholder="密码" type="password"></el-input>
      <template #footer>
      <span class="dialog-footer">
        <el-button type="danger" @click="deleteAccount">
          确认删除
        </el-button>
      </span>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
.account {
  width: 500px;
  margin: 0 auto;
}

.title {
  text-align: center;
}

.user-info > div {
  display: flex;
  align-items: center;
}

.user-info-left {
  width: 100px;
}
</style>