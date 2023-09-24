<script>
import {Delete, Plus} from "@element-plus/icons-vue";

export default {
  name: "TodoView",
  data() {
    return {
      dialogVisible: false,
      select: "",
      todoData: [
        {
          name: "待执行",
          todoList: [
            {
              uid: "abc",
              todoName: "完成Learn-Duck开发",
              check: false,
            }, {
              uid: "abcd",
              todoName: "完成计划模块开发",
              check: false,
            }, {
              uid: "abcdf",
              todoName: "完成日历模块开发",
              check: true,
            }
          ]
        },
        {
          name: "进行中",
          todoList: [
            {
              uid: "abcd",
              todoName: "完成计划模块开发",
              check: false,
            }
          ]
        },
        {
          name: "已完成",
          todoList: []
        }
      ]
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
    }
  },
  components: {Delete}
}
</script>

<template>
  <div class="todo">
    <div class="todo-view-title">计划</div>
  </div>
  <div class="todo-content">
    <div class="todo-list">
      <div class="todo-item" v-for="todo in todoData" :key="todo.name">
        <div class="todo-item-header">
          <div class="title">{{ todo.name }}
            <el-text>{{ todo.todoList.length }}</el-text>
          </div>
          <div class="operate">
            <el-icon color="red">
              <Delete/>
            </el-icon>
          </div>
        </div>
        <div class="todo-item-list">
          <div class="crate-todo">
            <el-button :icon="Plus" style="width: 100%"></el-button>
          </div>
          <div class="todo-item-card" v-for="todoItem in todo.todoList" :key="todoItem.uid">
            <el-card body-style="padding:0 10px;display: flex; align-items: center;">
              <el-checkbox v-model="todoItem.check" label="" size="large"/>
              <div style="width: 100%;height: 100%" @click="selectTodo(todoItem.uid)">
                <el-text style="margin-left: 10px">{{ todoItem.todoName }}</el-text>
              </div>
            </el-card>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog
      v-model="dialogVisible"
      width="30%"
      :before-close="handleClose">
    <div>
      {{ select }}
    </div>
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