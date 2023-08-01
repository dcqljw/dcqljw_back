<template>
  <div class="index">
    <div class="title">
      <div class="text">Welcome to moyu</div>
    </div>
    <div class="hot_top">
      <el-button @click="this.$router.push('hot_top')" size="large">吃瓜🍉</el-button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {}
  },
  methods: {},
  created() {
  }
}
</script>
<style scoped>
.index {
  padding-top: 200px;
}

@keyframes typing {
  from {
    width: 0
  }
  to {
    width: 100%
  }
}

/* 需要显示打字效果的文本 */
.text {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap; /* 禁止换行 */
  animation: typing 2s steps(32, end) forwards; /* 逐字显示，步骤数根据文本长度 */
  font-size: 40px;
}

.title {
  text-align: center;
  width: 400px;
  margin: 0 auto;
  padding-bottom: 100px;
}

.hot_top {
  text-align: center;
  width: 300px;
  margin: 0 auto;
}
</style>