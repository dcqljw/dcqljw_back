<template>
  <div class="main" v-loading="loading">
    <h1 class="title">算命（玉皇大帝认证）</h1>
    <el-input placeholder="输入姓名" class="item" v-model="name"></el-input>
    <el-input placeholder="输入生辰" class="item" v-model="bir"></el-input>
    <el-button class="item" style="width: 100%" @click="kaisuan">开算！！</el-button>
  </div>

  <el-dialog
      v-model="dialogVisible"
      title="Tips"
      width="30%"
      :before-close="handleClose"
  >
    <span><h1>封建迷信不可信！！！！！</h1></span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script>

export default {
  name: "FortuneTellerView",
  data() {
    return {
      loading: false,
      dialogVisible: false,
      name: "",
      bir: ""
    }
  },
  methods: {
    kaisuan() {
      if (this.name === "" || this.bir === ""){
        this.$message.error("请输入必填项")
        return
      }
      console.log(this.loading)
      this.loading = true
      setTimeout(() => {
        this.loading = false
        this.dialogVisible = true
      }, 3000)
      console.log(this.loading)
    },
    handleClose() {
      this.dialogVisible = false
    }
  }
}
</script>

<style scoped>
.title {
  text-align: center;
  padding-top: 30px;
}

.main {
  width: 400px;
  margin: 0 auto;
  padding-top: 100px;
}

.item {
  margin-top: 20px;
}
</style>