<script>
import {Plus} from "@element-plus/icons-vue";
import axios from "axios";

export default {
  name: "CreateGroupView",
  components: {Plus},
  data() {
    return {
      imageUrl: "",
      dialogVisible: false,
      dialogImageUrl: "",
      disabled: false,
      group_name: "",
      description: "",
      group_tag: "",
      avatar: "",
    }
  },
  methods: {
    handleAvatarSuccess(file) {
      console.log(file)
    },
    beforeAvatarUpload(file) {
      console.log(file)
      this.imageUrl = ""
    },
    selectFile(file) {
      console.log(file)
      this.imageUrl = file.url
      this.avatar = file
    },
    create_group() {
      const formData = new FormData();
      formData.append('file', this.avatar.raw)
      formData.append("group_name", this.group_name)
      formData.append("group_tag", this.group_tag)
      formData.append("desc", this.description)
      axios.post("/group/create_group", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {
        if (res.data.code === "2000") {
          const gid = res.data.data.gid
          this.$router.push("group_detail/" + gid + "/groupIndex")
        } else {
          this.$message.error(res.data.data.msg)
        }
      }).catch(() => {
        this.$message.error("error")
      })
    },
  }
}
</script>

<template>
  <el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
      <h1 class="title">创建小组</h1>
      <el-form>
        <el-form-item label="头像">
          <el-upload
              class="avatar-uploader"
              action="#"
              list-type="picture-card"
              :show-file-list="false"
              :auto-upload="false"
              :on-change="selectFile"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar"/>
            <el-icon v-else class="avatar-uploader-icon">
              <Plus/>
            </el-icon>
          </el-upload>
        </el-form-item>
        <el-form-item label="名称">
          <el-input v-model="group_name"></el-input>
        </el-form-item>
        <el-form-item label="简介">
          <el-input type="textarea" v-model="description"></el-input>
        </el-form-item>
        <el-form-item label="标签">
          <el-input v-model="group_tag"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="create_group">创建</el-button>
        </el-form-item>
      </el-form>
    </el-col>
    <el-col :span="8"></el-col>
  </el-row>
</template>

<style scoped>
.title {
  text-align: center;
}

.avatar-uploader .avatar {
  width: 148px;
  height: 148px;
  display: block;
}

.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>