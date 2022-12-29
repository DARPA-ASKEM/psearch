import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import "primevue/resources/themes/saga-blue/theme.css"; //theme
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css"; //core css
const app = createApp(App);
app.use(PrimeVue);

createApp(App).use(PrimeVue).mount('#app')

// app.mount("#app");
