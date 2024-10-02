<template>
    <div class="cpu-container" v-if="cpu">
        <div class="cpu-he-logical" style="text-align: center;">
            <VueUiKpi class="he" :config="config('CPU 核数')" :dataset="cpu[1]" />
            <VueUiKpi class="logical" :config="config('CPU 逻辑数')" :dataset="cpu[0]" />
        </div>
        <div class="used-div"><VueUiWheel class="used" :config="cpu_conf_used()" :dataset="{'percentage': cpu[2]}" v-if="cpu"/></div>
    </div>
</template>

<script setup lang="ts">
import "vue-data-ui/style.css"
import { inject } from "vue";
import { VueUiKpi, VueUiWheel } from "vue-data-ui";

const cpu:any = inject("cpu");
const config = (title: string) => {
    const config = {
        "animationFrames": 60,
        "animationValueStart": 0,
        "backgroundColor": "rgb(26,26,26)",
        "fontFamily": "inherit",
        "layoutClass": "p-4 m-4 rounded-md shadow",
        "layoutCss": "",
        "prefix": "",
        "suffix": "",
        "title": title,
        "titleBold": true,
        "titleColor": "rgb(98,195,93)",
        "titleClass": "",
        "titleCss": "",
        "titleFontSize": 16,
        "useAnimation": true,
        "valueBold": true,
        "valueColor": "#6376DD",
        "valueClass": "",
        "valueCss": "",
        "valueFontSize": 32,
        "valueRounding": 0
    }
    return config
}
const cpu_conf_used:any = () => {
    const gdata = {
    "responsive": false,
    "theme": "hack",
    "style": {
        "fontFamily": "inherit",
        "chart": {
        "backgroundColor": "#FFFFFF",
        "color": "#1A1A1A",
        "animation": {
            "use": true,
            "speed": 0.5,
            "acceleration": 1
        },
        "layout": {
            "wheel": {
                "ticks": {
                    "rounded": true,
                    "inactiveColor": "#e1e5e8",
                    "activeColor": "#6376DD",
                    "gradient": {
                    "show": true,
                    "shiftHueIntensity": "100"
                    }
                }
                },
                "innerCircle": {
                    "show": true,
                    "stroke": "#e1e5e8",
                    "strokeWidth": 1
                },
                "percentage": {
                "show": true,
                "fontSize": 48,
                "rounding": 0,
                "bold": true
                }
            },
            "title": {
                "text": "CPU 使用率",
                "color": "#1A1A1A",
                "fontSize": 20,
                "bold": true,
                "subtitle": {
                    "color": "#A1A1A1",
                    "text": "",
                    "fontSize": 16,
                    "bold": false
                }
            }
        }
    },
    "userOptions": {
            "show": false,
            "buttons": {
            "tooltip": false,
            "pdf": true,
            "csv": false,
            "img": true,
            "table": false,
            "labels": false,
            "fullscreen": true,
            "sort": false,
            "stack": false,
            "animation": false
        },
        "buttonTitles": {
            "open": "Open options",
            "close": "Close options",
            "pdf": "Download PDF",
            "img": "Download PNG",
            "fullscreen": "Toggle fullscreen"
        }
    }
}
    return gdata;
}
</script>

<style scoped lang="less">
.cpu-container {
    display: flex;
    flex-direction: column;
    .cpu-he-logical {
        height: 60px;
        display: flex;
        margin: 0 auto;
        .logical {
            margin-left: 5px;
        }
    }
    .used-div {
        margin-top: 10px;
        .used {
            width: 320px !important;
            margin: 0 auto;
        }
    }
}
</style>