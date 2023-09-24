<script>
import {Document, Edit, More, Search, Share, Star, Upload, Link} from "@element-plus/icons-vue";

export default {
  name: "DocumentView",
  components: {Share, Star, More, Document, Link},
  data() {
    return {
      searchValue: ""
    }
  },
  computed: {
    Edit() {
      return Edit
    },
    Search() {
      return Search
    }, Upload() {
      return Upload
    }
  }
}
</script>

<template>
  <div class="document">
    <div class="document-header">
      <div class="document-view-title">文档</div>
      <div class="create-document">
        <el-button :icon="Upload">上传</el-button>
        <el-button type="primary" :icon="Edit">新建</el-button>
      </div>
    </div>
    <div class="recent">
      <div class="recent-title">
        <h3>收藏</h3>
      </div>
      <div class="recent-content">
        <div class="recent-item" v-for="i in 5" :key="i">
          <el-card shadow="hover">
            <div class="recent-card">
              <div style="display: flex">
                <div>
                  <el-icon size="40">
                    <Document/>
                  </el-icon>
                </div>
                <div class="recent-content-title">
                  <div class="title">
                    <div>
                      <el-text size="large">Learn-Duck入门必看</el-text>
                    </div>
                    <div class="recent-type">
                      <el-tag :size="'small'" :type="'danger'">私有</el-tag>
                    </div>
                  </div>
                  <div>
                    <el-text size="small">DCQ 2023年9月13日</el-text>
                  </div>
                </div>
              </div>
              <el-popover trigger="hover">
                <template #reference>
                  <div class="operate">
                    <el-icon>
                      <More/>
                    </el-icon>
                  </div>
                </template>
                <template #default>
                  <div>
                    <el-link :underline="false">
                      <el-icon size="20" class="el-icon--left">
                        <Share/>
                      </el-icon>
                      分享
                    </el-link>
                  </div>
                  <el-divider/>
                  <div>
                    <el-link :underline="false">
                      <el-icon size="20" class="el-icon--left">
                        <Link/>
                      </el-icon>
                      复制链接
                    </el-link>
                  </div>
                  <el-divider/>
                  <div>
                    <el-link :underline="false">
                      <el-icon size="20" class="el-icon--left">
                        <Star/>
                      </el-icon>
                      收藏
                    </el-link>
                  </div>
                </template>
              </el-popover>

            </div>
          </el-card>
        </div>
      </div>
    </div>
    <div class="document-list">
      <div class="document-list-title">
        <h3>最近</h3>
      </div>
      <div class="recent-content">
        <div class="recent-item" v-for="i in 50" :key="i">
          <el-card shadow="hover">
            <div class="recent-card">
              <div>
                <el-icon size="40">
                  <Document/>
                </el-icon>
              </div>
              <div class="recent-content-title">
                <div class="title">
                  <div>
                    <el-text size="large">Learn-Duck入门必看</el-text>
                  </div>
                  <div class="recent-type">
                    <el-tag :size="'small'" :type="'success'">公开</el-tag>
                  </div>
                </div>
                <div>
                  <el-text size="small">DCQ 2023年9月13日</el-text>
                </div>
              </div>
            </div>
          </el-card>
        </div>
        <div class="recent-item">
          <el-card shadow="hover">
            <div class="recent-card">
              <div>
                <el-icon size="40">
                  <Document/>
                </el-icon>
              </div>
              <div class="recent-content-title">
                <div>
                  <el-text size="large">Python入门</el-text>
                </div>
                <div>
                  <el-text size="small">DCQ 2023年9月13日</el-text>
                </div>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.document-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.recent-content, .recent-card {
  display: flex;
}

.recent-content {
  flex-direction: row;
  flex-wrap: wrap;
}

.recent-card {
  align-items: center;
  justify-content: space-between;
}

.recent-content-title {
  margin-left: 10px;
}

.recent-content-title > .title {
  display: flex;
  align-items: center;
}

.recent-type {
  margin-left: 5px;
}

.recent-item {
  cursor: pointer;
  margin: 10px;
  width: 350px;
}

.operate {
  width: 20px;
  text-align: center;
  height: 20px;
  border-radius: 6px;
}

.operate:hover {
  background: #dcdfe6;
}
</style>