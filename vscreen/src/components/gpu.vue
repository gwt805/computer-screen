<template>
    <div class="gpu-conntainer">
        <div class="gpu-m" v-for="(val,key) in gpu" :key="key" v-if="gpu">
            <div class="gpu-mem"><VueUiSparkStackbar :config="gpu_conf(val)" :dataset="gpu_data(val)" v-if="gpu" /></div>
            <div class="gpu-temp-used">
                <div class="used"><div class="mem-wheel" ><VueUiWheel :config="gpu_conf_used()" :dataset="{'percentage': val['load']}" v-if="gpu" /></div></div>
                <div class="temp"><VueUiSparkgauge :config="gpu_conf_temp" :dataset="{'value': val['temp'],'min': 0,'max': 100,'title': '显卡温度'}" v-if="gpu" /></div>
                <!-- <div class="temp"><div class="mem-wheel"><VueUiWheel :config="gpu_conf_temp()" :dataset="{'percentage': val['temp']}" v-if="gpu" /></div></div> -->
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref,inject } from "vue";
import { VueUiWheel, VueUiSparkStackbar, VueUiSparkgauge } from "vue-data-ui";

const gpu:any = inject("gpu");

const gpu_conf:any = (data:any) => {
    const gdata = {"theme": "hack","style": {"title": {"text": data['name']}}};
    return gdata;
}

const gpu_conf_used:any = () => {
    const gdata = {"theme": "hack","style": {"chart": {"animation": {"use": true,"speed": 0.1,"acceleration": 1},"title": {"text": "显卡使用率"}}}, "userOptions": {"show": false}}
    return gdata;
}

// const gpu_conf_temp:any = () => {
//     const gdata = {"theme": "hack","style": {"chart": {"animation": {"use": true,"speed": 0.1,"acceleration": 1},"title": {"text": "显卡温度"}}}}
//     return gdata;
// }

const gpu_conf_temp:any = ref({
    "theme": "hack",
    "style": {
        "animation": {"show": true, "speedMs": 150},
        "dataLabel": {"autoColor": true, 'suffix': '℃'},
        "title": {"fontSize": 18, "bold": true,}
    }
})

const gpu_data:any = (data:any) => {
    const gdata = [
        {"name": "总内存", "value": data['total'], "color": "#42d392"},
        {"name": "已使用", "value": data['used'], "color": "#ff9900"},
        {"name": "剩余", "value": data['free'], "color": "#5f8bee"},
    ]
    return gdata;
}
</script>

<style scoped lang="less">
.gpu-conntainer {
    width: 600px;
    .gpu-temp-used {
        width: 100%;
        display: flex;
        .used,.temp {
            width: 50%;
        }
    }
}
</style>