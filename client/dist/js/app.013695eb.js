(function(){"use strict";var e={7990:function(e,t,n){var a=n(9242),i=n(3396);function o(e,t,n,a,o,r){const l=(0,i.up)("router-view");return(0,i.wg)(),(0,i.j4)(l)}var r=n(4161),l={name:"App",data(){return{title:""}},methods:{get_title(){r.Z.get("https://dcqljw.xyz:8000/home/").then((e=>{this.title=e.data})).catch((e=>{console.log(e)}))}},created(){}},s=n(89);const u=(0,s.Z)(l,[["render",o]]);var d=u,c=n(2483),h=n(7139);const g={id:"barrage"},m=["data-line"],p={class:"barrage_item"},f=["src"],v={class:"barrage_text"},b={class:"send_barrage"};function w(e,t,n,o,r,l){const s=(0,i.up)("el-input");return(0,i.wg)(),(0,i.iD)("div",g,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(r.barrage_list,(e=>((0,i.wg)(),(0,i.iD)("div",{class:"item",key:e.id,"data-line":e.line,onTransitionend:t[0]||(t[0]=(...e)=>l.removeBullet&&l.removeBullet(...e))},[(0,i._)("div",p,[(0,i._)("img",{src:"https://api.multiavatar.com/"+e.id+".png"},null,8,f),(0,i._)("div",v,(0,h.zw)(e.text),1)])],40,m)))),128)),(0,i._)("div",b,[(0,i.Wm)(s,{modelValue:r.send_text,"onUpdate:modelValue":t[1]||(t[1]=e=>r.send_text=e),placeholder:"Please input",onKeydown:(0,a.D2)(l.send_barrage,["enter"])},null,8,["modelValue","onKeydown"])])])}n(7658);const _=()=>Math.random()+Math.random();var x={name:"App",data(){return{send_text:"",top:0,barrage_list:[],waitBarrage:[],lines:8,currentLine:1}},methods:{showNextBarrage(){if(!this.waitBarrage.length)return;this.currentLine=this.currentLine%5+1;const e=this.waitBarrage.shift();e.line=this.currentLine,this.barrage_list.push(e)},send_barrage(){console.log(this.send_text);const e={id:_(),text:this.send_text,line:0};this.waitBarrage.push(e),this.send_text=""},removeBullet(){this.barrage_list.shift(),console.log(this.barrage_list)},get_data(){r.Z.get("https://dcqljw.xyz:8000/home").then((e=>{console.log(e);for(let t=0;t<e.data.length;t++){console.log(e.data[t]);const n={id:_(),text:e.data[t].title,line:0};this.waitBarrage.push(n)}}))}},created(){this.showNextBarrage(),this.get_data(),setInterval(this.showNextBarrage,700)}};const V=(0,s.Z)(x,[["render",w],["__scopeId","data-v-6d3909e8"]]);var y=V;const k=e=>((0,i.dD)("data-v-087b420a"),e=e(),(0,i.Cn)(),e),B={class:"main"},O=k((()=>(0,i._)("h1",{class:"title"},"算命（玉皇大帝认证）",-1))),j=k((()=>(0,i._)("span",null,[(0,i._)("h1",null,"封建迷信不可信！！！！！")],-1))),T={class:"dialog-footer"};function C(e,t,n,a,o,r){const l=(0,i.up)("el-input"),s=(0,i.up)("el-button"),u=(0,i.up)("el-dialog"),d=(0,i.Q2)("loading");return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i.wy)(((0,i.wg)(),(0,i.iD)("div",B,[O,(0,i.Wm)(l,{placeholder:"输入姓名",class:"item",modelValue:o.name,"onUpdate:modelValue":t[0]||(t[0]=e=>o.name=e)},null,8,["modelValue"]),(0,i.Wm)(l,{placeholder:"输入生辰",class:"item",modelValue:o.bir,"onUpdate:modelValue":t[1]||(t[1]=e=>o.bir=e)},null,8,["modelValue"]),(0,i.Wm)(s,{class:"item",style:{width:"100%"},onClick:r.kaisuan},{default:(0,i.w5)((()=>[(0,i.Uk)("开算！！")])),_:1},8,["onClick"])])),[[d,o.loading]]),(0,i.Wm)(u,{modelValue:o.dialogVisible,"onUpdate:modelValue":t[3]||(t[3]=e=>o.dialogVisible=e),title:"Tips",width:"30%","before-close":r.handleClose},{footer:(0,i.w5)((()=>[(0,i._)("span",T,[(0,i.Wm)(s,{onClick:t[2]||(t[2]=e=>o.dialogVisible=!1)},{default:(0,i.w5)((()=>[(0,i.Uk)("关闭")])),_:1})])])),default:(0,i.w5)((()=>[j])),_:1},8,["modelValue","before-close"])],64)}var D={name:"FortuneTellerView",data(){return{loading:!1,dialogVisible:!1,name:"",bir:""}},methods:{kaisuan(){""!==this.name&&""!==this.bir?(console.log(this.loading),this.loading=!0,setTimeout((()=>{this.loading=!1,this.dialogVisible=!0}),3e3),console.log(this.loading)):this.$message.error("请输入必填项")},handleClose(){this.dialogVisible=!1}}};const U=(0,s.Z)(D,[["render",C],["__scopeId","data-v-087b420a"]]);var W=U;const Z=[{path:"/",name:"index",component:y},{path:"/FortuneTeller",name:"FortuneTellerView",component:W}],F=(0,c.p7)({history:(0,c.r5)(),routes:Z});var L=F,M=n(65),z=(0,M.MT)({state:{},getters:{},mutations:{},actions:{},modules:{}}),I=n(8013);n(4415);const K=(0,a.ri)(d);K.use(z).use(L).use(I.Z).mount("#app")}},t={};function n(a){var i=t[a];if(void 0!==i)return i.exports;var o=t[a]={exports:{}};return e[a].call(o.exports,o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(t,a,i,o){if(!a){var r=1/0;for(d=0;d<e.length;d++){a=e[d][0],i=e[d][1],o=e[d][2];for(var l=!0,s=0;s<a.length;s++)(!1&o||r>=o)&&Object.keys(n.O).every((function(e){return n.O[e](a[s])}))?a.splice(s--,1):(l=!1,o<r&&(r=o));if(l){e.splice(d--,1);var u=i();void 0!==u&&(t=u)}}return t}o=o||0;for(var d=e.length;d>0&&e[d-1][2]>o;d--)e[d]=e[d-1];e[d]=[a,i,o]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var a in t)n.o(t,a)&&!n.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={143:0};n.O.j=function(t){return 0===e[t]};var t=function(t,a){var i,o,r=a[0],l=a[1],s=a[2],u=0;if(r.some((function(t){return 0!==e[t]}))){for(i in l)n.o(l,i)&&(n.m[i]=l[i]);if(s)var d=s(n)}for(t&&t(a);u<r.length;u++)o=r[u],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(d)},a=self["webpackChunkclient"]=self["webpackChunkclient"]||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))}();var a=n.O(void 0,[998],(function(){return n(7990)}));a=n.O(a)})();