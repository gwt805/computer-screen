<template>
    <div class="user">
        <p>
            <label for="user">用户: </label>
            <span id="user">{{ user[0] }}</span>
        </p>
        <p>
            <label for="hostname">主机名: </label>
            <span id="hostname">{{ user[1] }}</span>
        </p>
        <p>
            <label for="ip">IP: </label>
            <span id="ip">{{ user[2] }}</span>
        </p>
    </div>
</template>

<script setup lang="ts">
import { inject } from "vue"
const user: any = inject("user")
</script>

<style scoped lang="less">
.user {
    width: 230px;
    height: 130px;
    p {
        padding: 10px 0;
    }
    margin: auto;
    align-content: center;
}
</style>