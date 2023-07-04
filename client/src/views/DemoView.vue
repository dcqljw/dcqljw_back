<template>
  <div class="demo-main">
    <!--    <h1 style="text-align: center">ljw专属立体展开图</h1>-->
    <div class="suv">
      <canvas id="canvas1" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <canvas id="canvas2" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <canvas id="canvas3" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <canvas id="canvas4" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <canvas id="canvas5" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <canvas id="canvas6" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
              @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
      <el-button class="run" type="primary" @click="renderScene">运行</el-button>
    </div>
    <div class="canvas-container">
      <div class="xuanran">
        <div id="result">
        </div>
      </div>
    </div>

  </div>
</template>
<script>
import * as THREE from 'three'
import {OrbitControls} from "three/addons/controls/OrbitControls.js";

export default {
  name: "DemoView",
  data() {
    return {
      isDrawing: false,
      context: null,
      texture: null,
      material: null,
      canvasRect: null,
      isrun: false
    }
  },
  mounted() {
    for (let i = 1; i < 7; i++) {
      const c = document.getElementById(`canvas${i}`)
      const context = c.getContext("2d")
      context.fillStyle = 'white'
      context.fillRect(0, 0, c.width, c.height)
      context.font = '25px 微软雅黑'
      context.fillStyle = 'black'
      context.fillText(`序号:${i}`, 0, 30)

    }
    // const canvas = document.getElementById('canvas1');
    // this.context = canvas.getContext('2d');
    // this.canvasRect = canvas.getBoundingClientRect();
  },
  methods: {
    startDrawing(event) {
      console.log(event)
      this.context = event.target.getContext('2d')
      this.isDrawing = true;
      this.context.beginPath();
      this.context.strokeStyle = 'blue';
      let mouseX = 0
      let mouseY = 0
      if (event instanceof TouchEvent) {
        const rect = event.target.getBoundingClientRect();
        const touch = event.touches[0];
        const scaleX = event.target.width / rect.width;
        const scaleY = event.target.height / rect.height;
        console.log(scaleX, scaleY)
        mouseX = (touch.clientX - rect.left) * scaleX;
        mouseY = (touch.clientY - rect.top) * scaleY;
      } else {
        const rect = event.target.getBoundingClientRect();
        const scaleX = event.target.width / rect.width;
        const scaleY = event.target.height / rect.height;
        console.log(scaleX, scaleY)
        mouseX = (event.clientX - rect.left) * scaleX;
        mouseY = (event.clientY - rect.top) * scaleY;
      }
      this.context.moveTo(mouseX, mouseY);
    },
    draw(event) {
      if (!this.isDrawing) return;
      let mouseX = 0
      let mouseY = 0
      event.preventDefault()
      if (event instanceof TouchEvent) {
        const rect = event.target.getBoundingClientRect();
        const touch = event.touches[0];
        const scaleX = event.target.width / rect.width;
        const scaleY = event.target.height / rect.height;
        console.log(scaleX, scaleY)
        mouseX = (touch.clientX - rect.left) * scaleX;
        mouseY = (touch.clientY - rect.top) * scaleY;
      } else {
        const rect = event.target.getBoundingClientRect();
        const scaleX = event.target.width / rect.width;
        const scaleY = event.target.height / rect.height;
        console.log(scaleX, scaleY)
        mouseX = (event.clientX - rect.left) * scaleX;
        mouseY = (event.clientY - rect.top) * scaleY;
      }
      this.context.lineTo(mouseX, mouseY);
      this.context.stroke();
    },
    stopDrawing() {
      this.isDrawing = false;
    },
    renderScene() {
      if (this.isrun) {
        document.getElementById("result").getElementsByTagName("canvas")[0].parentNode.removeChild(document.getElementById("result").getElementsByTagName("canvas")[0]);
        this.isrun = false
      }
      this.isrun = true
      const canvasContainer = document.getElementById("result")
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, 800 / 600, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(800, 600);
      renderer.setClearColor(0xf7f7f8);
      canvasContainer.appendChild(renderer.domElement);

      const materials = [];
      const l = [3, 1, 5, 6, 2, 4]
      for (const i of l) {
        const c = document.getElementById(`canvas${i}`)
        const context = c.getContext("2d")
        const texture = new THREE.CanvasTexture(context.canvas);
        const material = new THREE.MeshBasicMaterial({map: texture});
        materials.push(material)
      }


      const geometry = new THREE.BoxGeometry(3, 3, 3);

      const cube = new THREE.Mesh(geometry, materials);

      scene.add(cube);

      const edgesGeometry = new THREE.EdgesGeometry(geometry);
      const edgesMaterial = new THREE.LineBasicMaterial({color: 0x871F78});
      const edges = new THREE.LineSegments(edgesGeometry, edgesMaterial);
      cube.add(edges);


      const controls = new OrbitControls(camera, renderer.domElement);
      controls.minPolarAngle = -Math.PI
      controls.maxPolarAngle = Math.PI
      camera.position.z = 5;
      controls.update()

      function animate() {
        requestAnimationFrame(animate);
        controls.update()
        renderer.render(scene, camera);
      }

      animate()
    },
  },
  created() {

  }
}
</script>
<style>
.canvas-container {
  display: flex;
  flex-direction: column; /* 垂直排列子元素 */
}

#canvas1, #canvas2, #canvas3, #canvas4, #canvas5, #canvas6 {
  width: 200px;
  height: 200px;
  display: block;
  border: 1px solid;
  position: absolute;
}

#canvas1 {
  top: 200px;
}

#canvas2 {
  left: 200px;
  top: 200px;
}

#canvas3 {
  left: 400px;
  top: 200px;
}

#canvas4 {
  left: 600px;
  top: 200px;
}

#canvas5 {
  left: 200px;
}

#canvas6 {
  left: 200px;
  top: 400px;
}

.demo-main {
  height: 100%;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}

.suv {
  height: 600px;
  width: 800px;
  position: relative;
}

.run {
  position: absolute;
  right: 40px;
  bottom: 40px;
}

.xuanran {
  width: 50%;
}
</style>