<template>
    <div class="mem-container">
        <div class="mem"><VueUiSparkStackbar :config="config_mem" :dataset="mem" v-if="mem" /></div>
        <div class="mem-wheel" style="margin-top: 10px;"><VueUiWheel class="mem-wheel" :config="config_mem_wheel" :dataset="mem_wheel" v-if="mem_wheel" /></div>
    </div>
</template>

<script setup lang="ts">
import { ref, inject } from 'vue';
import { VueUiSparkStackbar, VueUiWheel } from "vue-data-ui";
const config_mem:any = ref({"theme": "hack","style": {"title": {"text": "内存"}}});
const config_mem_wheel:any = ref({"theme": "hack","style": {"chart": {"animation": {"use": true,"speed": 0.1,"acceleration": 1},"title": {"text": "内存占用率"}}}, "userOptions": {"show": false}});

const mem:any = inject('mem');
const mem_wheel:any = inject('mem_wheel');
</script>

<style scoped lang="less">
.mem-container {
    .mem-wheel {
        width: 320px !important;
        margin: 0 auto;
    }
}
</style>