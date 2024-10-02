<template>
    <div class="net-container">
        <div><VueUiSparkgauge :config="config" :dataset="{'value': net[1],'min': 0,'max': 200,'title': '下载带宽'}" v-if="net" /></div>
        <div><VueUiSparkgauge :config="config" :dataset="{'value': net[0],'min': 0,'max': 200,'title': '上传带宽'}" v-if="net" /></div>
    </div>
</template>

<script setup lang="ts">
import "vue-data-ui/style.css"
import { ref, inject } from "vue";
import { VueUiSparkgauge } from "vue-data-ui";

const net: any = inject("net");
const config: any = ref({
    "theme": "hack",
    "style": {
        "animation": {"show": true, "speedMs": 150},
        "dataLabel": {"autoColor": true, 'suffix': 'Mbps'},
        "title": {"fontSize": 18, "bold": true},
        "track": {"autoColor": true}
    }
})
</script>

<style scoped lang="less">
    .net-container {
        display: flex;
        flex-direction: row;
    }
</style>