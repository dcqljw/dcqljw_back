<script>
import axios from "axios";

export default {
  name: "IndexView",
  data() {
    return {
      groupInfo: {
        group_name: "Learn-Duck建设组"
      },
      personvalue: 1000
    }
  },
  mounted() {
    let group_id = this.$route.params.id
    axios.get("/group/get_group?gid=" + group_id).then(res => {
      console.log(res)
      if (res.data.code === "2000") {
        this.groupInfo = res.data.data
      } else {
        this.$message.error(res.data.msg)
      }
    }).catch(() => {
      this.$message.error("查询失败")
    })
  }
}
</script>

<template>
  <div class="group-index">
    <div class="group-header">
      <div class="group-title">{{ groupInfo.group_name }}</div>
      <div class="person">
        <el-statistic title="人数" :value="1000"/>
      </div>
    </div>
    <div class="group-content">
      <div class="notice-card">
        <el-card>
          <div class="card-title">通知消息</div>
          <div class="card-content">
            <el-text>恭喜learn-duck成立👏👏👏👏👏</el-text>
          </div>
        </el-card>
      </div>
      <!--      <div class="recommend-card">-->
      <!--        <el-card>-->
      <!--          <div class="card-title">推荐内容</div>-->
      <!--          <div class="card-content">-->
      <!--            <el-text>-->
      <!--              空-->
      <!--            </el-text>-->
      <!--          </div>-->
      <!--        </el-card>-->
      <!--      </div>-->
      <!--      <div class="users-card">-->
      <!--        <el-card>-->
      <!--          <div class="card-title">主要成员</div>-->
      <!--          <div class="user-list">-->
      <!--            <div class="user-item">-->
      <!--              <el-avatar>DCQ</el-avatar>-->
      <!--              <div class="user-info">-->
      <!--                <div class="username">-->
      <!--                  DCQ-->
      <!--                  <el-tag type="danger" size="small">主管理</el-tag>-->
      <!--                </div>-->
      <!--                <el-text size="small" class="desc">我真的不想上班</el-text>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--            <el-divider/>-->
      <!--            <div class="user-item">-->
      <!--              <el-avatar>LJW</el-avatar>-->
      <!--              <div class="user-info">-->
      <!--                <div class="username">LJW-->
      <!--                  <el-tag size="small">管理</el-tag>-->
      <!--                </div>-->
      <!--                <el-text size="small" class="desc">我真的不想上班</el-text>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--            <el-divider/>-->
      <!--            <div class="user-item">-->
      <!--              <el-avatar>LEARN</el-avatar>-->
      <!--              <div class="user-info">-->
      <!--                <div class="username">LEARN-->
      <!--                  <el-tag size="small">管理</el-tag>-->
      <!--                </div>-->
      <!--                <el-text size="small" class="desc">我真的不想上班</el-text>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--            <el-divider/>-->
      <!--            <div class="user-item">-->
      <!--              <el-avatar>DUCK</el-avatar>-->
      <!--              <div class="user-info">-->
      <!--                <div class="username">DUCK-->
      <!--                  <el-tag size="small">管理</el-tag>-->
      <!--                </div>-->
      <!--                <el-text size="small" class="desc">我真的不想上班</el-text>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </el-card>-->
      <!--      </div>-->
      <!--      <div class="chat-group">-->
      <!--        <el-card>-->
      <!--          <div class="card-title">公共聊天室</div>-->
      <!--          <div class="user-list">-->
      <!--            <div class="user-item">-->
      <!--              <el-avatar>全体</el-avatar>-->
      <!--              <div class="user-info">-->
      <!--                <div class="username">-->
      <!--                  全体成员-->
      <!--                  <el-tag type="success" size="small">3人</el-tag>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </el-card>-->
      <!--      </div>-->
    </div>
  </div>
</template>

<style scoped>
.group-header {
  display: flex;
  justify-content: space-between;
}

.group-content {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.group-title {
  font-size: 24px;
}

.group-content > div {
  margin: 10px;
}

.card-title {
  margin-bottom: 10px;
  text-align: center;
  font-size: 20px;
}

.user-item {
  display: flex;
  align-items: center;
}

.user-info {
  margin-left: 15px;
}
</style>