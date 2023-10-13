<script>
import {Delete, Plus} from "@element-plus/icons-vue";
import axios from "axios";
import signOut from "../../plugins/utils"

export default {
  name: "TodoView",
  data() {
    return {
      dialogVisible: false,
      select: "",
      createTodo: {
        todo_title: "",
        details: "",
        status: 0,
        todo_type: "",
        group_id: ""
      },
      showCreateTodo: false,
      currentTodoName: "",
      todoData: {
        "待执行": [],
        "执行中": [],
        "已完成": []
      }
    }
  },
  computed: {
    Plus() {
      return Plus
    }
  },
  methods: {
    selectTodo(uid) {
      this.select = uid
      this.dialogVisible = true
    },
    addTodo() {
      console.log(this.currentTodoName)
      this.createTodo.group_id = this.$route.params.id
      this.createTodo.todo_type = this.currentTodoName
      this.createTodo.status = 0
      console.log(this.createTodo)
      const token = localStorage.getItem('token')
      console.log(token)
      axios.post("/group/create_todo", this.createTodo, {
        headers: {
          'Authorization': token
        }
      }).then(res => {
        console.log(res)
        if (res.data.code === "2000") {
          console.log(res)
          this.showCreateTodo = false
          this.todoData[this.currentTodoName].push(res.data.result)
          console.log(this.todoData)
        } else {
          this.$message.error(res.data.msg)
        }
      })
      this.createTodo = {}
    }
  },
  components: {Delete},
  created() {
    console.log(this.$route.params.id)
    const group_id = this.$route.params.id
    const token = localStorage.getItem('token')
    console.log(token)
    axios.get("/group/get_todos?group_id=" + group_id + "&todo_type=待执行", {
      headers: {
        'Authorization': token
      }
    }).then(res => {
      this.todoData["待执行"] = res.data
      console.log(this.todoData)
    }).catch(res => {
      console.log(res.response.data.detail)
      this.$message.error(res.response.data.detail)
    })
    axios.get("/group/get_todos?group_id=" + group_id + "&todo_type=执行中", {
      headers: {
        'Authorization': token
      }
    }).then(res => {
      this.todoData["执行中"] = res.data
      console.log(this.todoData)
    }).catch(res => {
      console.log(res.response.data.detail)
      this.$message.error(res.response.data.detail)
      signOut(this)
    })
    axios.get("/group/get_todos?group_id=" + group_id + "&todo_type=已完成", {
      headers: {
        'Authorization': token
      }
    }).then(res => {
      this.todoData["已完成"] = res.data
      console.log(this.todoData)
    }).catch(res => {
      console.log(res.response.data.detail)
      this.$message.error(res.response.data.detail)
    })
  }
}
</script>

<template>
  <div class="todo">
    <div class="todo-view-title">计划</div>
  </div>
  <div class="todo-content">
    <div class="todo-list">
      <div class="todo-item" v-for="(todo,key) in todoData" :key="key">
        <div class="todo-item-header">
          <div class="title">{{ key }}
            <el-text>{{ todo.length }}</el-text>
          </div>
          <div class="operate">
            <el-icon color="red">
              <Delete/>
            </el-icon>
          </div>
        </div>
        <div class="todo-item-list">
          <div class="crate-todo">
            <el-button :icon="Plus" style="width: 100%"
                       @click="showCreateTodo = true,currentTodoName = key "></el-button>
          </div>
          <div class="todo-item-card" v-for="todoItem in todo" :key="todoItem.todo_id">
            <el-card body-style="padding:0 10px;display: flex; align-items: center;">
              <el-checkbox v-model="todoItem.status" label="" size="large"/>
              <div style="width: 100%;height: 100%" @click="selectTodo(todoItem.todo_id)">
                <el-text style="margin-left: 10px">{{ todoItem.todo_title }}</el-text>
              </div>
            </el-card>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog
      v-model="dialogVisible"
      width="30%">
    <div>
      {{ select }}
    </div>
  </el-dialog>
  <el-dialog
      v-model="showCreateTodo"
      title="创建任务"
      width="30%"
  >
    <el-form>
      <el-form-item label="任务标题">
        <el-input v-model="createTodo.todo_title"></el-input>
      </el-form-item>
      <el-form-item label="任务详情">
        <el-input v-model="createTodo.details"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="showCreateTodo = false">取消</el-button>
        <el-button type="primary" @click="addTodo">
          创建
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style scoped>
.todo-list {
  display: flex;
}

.operate {
  cursor: pointer;
}

.todo-item {
  width: 300px;
  margin: 10px;
}

.todo-item-list > div {
  margin-bottom: 10px;
}

.todo-item-card {
  cursor: pointer;
}

.todo-item-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.todo-view-title {
  font-size: 20px;
}
</style>