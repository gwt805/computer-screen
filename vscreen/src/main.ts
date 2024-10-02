import './style.css';
import App from './App.vue';
import "vue-data-ui/style.css";
import { createApp } from 'vue';
import 'element-plus/dist/index.css';
import { VueUiRadar } from "vue-data-ui";
import 'element-plus/theme-chalk/dark/css-vars.css';


const app = createApp(App)
app.component("VueUiRadar", VueUiRadar)
app.mount('#app')