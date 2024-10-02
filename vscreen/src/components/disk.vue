<template>
    <div class="disk">
        <div class="disk-body" v-for="(val,key) in disk" v-if="disk">
            <VueUiSparkStackbar :config="conf(key)" :dataset="val" v-if="disk" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { inject } from "vue";
import { VueUiSparkStackbar } from "vue-data-ui";

const disk:any = inject("disk");

const conf:any = (key:number) => {
    const config = {'theme': 'hack','style': {'title': {'text':  key+' 盘(GB)'}}}
    return config
}
</script>

<style scoped lang="less">
.disk {
    width: 600px;
    height: auto;
    display: flex;
    flex-direction: column;
}
</style>