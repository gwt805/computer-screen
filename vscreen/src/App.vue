<template>
  <div class="container">
    <div class="top"><h1>Monitor 可视化大屏</h1><span>{{ datetimes }}</span></div>
    <div class="middle">
      <div class="m-l">
        <div class="c"><cpu_ui /></div>
        <div class="m"><mem_ui /></div>
      </div>
      <div class="m-d">
        <div class="g"><gpu_ui /></div>
        <div class="d"><disk_ui /></div>
      </div>
      <div class="m-r">
        <div class="u"><user_ui/></div>
        <div class="n"><net_ui /></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import "vue-data-ui/style.css"
import http from './utils/axios';
import { ref, onMounted, onUnmounted, provide } from 'vue';
import user_ui from './components/user.vue'
import mem_ui from './components/mem.vue'
import cpu_ui from './components/cpu.vue'
import gpu_ui from './components/gpu.vue'
import disk_ui from './components/disk.vue'
import net_ui from "./components/net.vue";

const datetimes = ref();
const cpu = ref();
const gpu = ref();
const disk = ref();
const mem = ref();
const mem_wheel = ref();
const net = ref();
const user = ref([]);
const interval = ref()
const date_interval = ref()

provide("user", user)
provide("cpu", cpu)
provide("gpu", gpu)
provide("disk", disk)
provide("mem", mem)
provide("mem_wheel", mem_wheel)
provide("net", net)

const create_interval = () => {
  interval.value = setInterval(() =>{get_data()}, 100);
}

const get_data = () => {
  clearInterval(interval.value)
  http.get("/").then((res:any)=> {
    cpu.value = res.cpu;
    gpu.value = res.gpu;
    disk.value = res.disk;
    mem.value = res.mem;
    mem_wheel.value = {"percentage": res.mem[1].value/res.mem[0].value*100};
    net.value = res.net;
    user.value = res.user_info;
    create_interval()
  })
}

date_interval.value = setInterval(() => {
  const date = new Date();
  const year = date.getFullYear();
  const month = (date.getMonth() + 1) >= 10 ? date.getMonth() + 1 : '0' + (date.getMonth() + 1);
  const day = date.getDate() >= 10 ? date.getDate() : '0' + date.getDate();
  const hour = date.getHours() >= 10 ? date.getHours() : '0' + date.getHours();
  const minute = date.getMinutes() >= 10 ? date.getMinutes() : '0' + date.getMinutes();
  const second = date.getSeconds() >= 10 ? date.getSeconds() : '0' + date.getSeconds();
  const time = `${year}-${month}-${day} ${hour}:${minute}:${second}`;
  datetimes.value = time;
}, 1000);

onMounted(() => {
  get_data()
})

onUnmounted(() => { clearInterval(interval.value) })
</script>

<style scoped lang="less">
.container {
  .top {
    width: 100%;
    height: 50px;
    border-bottom: 1px dashed #686868;
    text-align: center;
    overflow: hidden;
    h1 {
      text-align: center;
      display: inline-block;
      margin: auto;
      color: #2a81e4;
    }
    span {
      float: right;
      line-height: 50px;
    }
  }
  .middle {
    width: 100%;
    height: calc(100% - 51px);
    position: fixed;
    top: 51px;
    display: flex;
    flex-wrap: wrap;
    overflow: auto;
    .m-l,.m-d,.m-r {
      width: calc(100% / 3 - 2px);
      height: 100%;
    }

    .m-l {
      .c,.m {
        width: 100%;
        height: 50%;
      }
    }
    .m-d {
      .g,.d {
        width: 100%;
        height: 50%;
      }
    }
    .m-r {
      .u,.n {
        width: 100%;
        height: 50%;
      }
    }
  }
  @media screen and (max-width: 768px) {
    .middle {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      .m-l,.m-d,.m-r {
        width: 100%;
        height: 100%;
      }
    }
  }
  @media screen and (min-width: 768px) and (max-width: 1900px) {
    .middle {
      display: flex;
      flex-direction: row;
      .m-l,.m-d,.m-r {
        width: calc(100% / 2);
        height: 100%;
      }
    }
  }
  @media screen and (min-width: 1920px) {
    .middle {
      display: flex;
      flex-direction: row;
      .m-l,.m-d,.m-r {
        width: calc(100% / 3);
        height: 100%;
      }
    }
  }
}
</style>