<template>
  <div class="pt-4" id="app">
    <h1 class="text-center">LPM</h1>
    <Form />
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
//import { BootstrapVue } from "bootstrap-vue";
import Form from "./components/Form";

Vue.use(VueAxios, axios);
export default {
  name: "App",
  components: {
    Form,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
 
  color: #2c3e50;
  background-color: #f3e5f5;

  height: 100vh;

  overflow-x: hidden;
}

.card {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background-color: #8e24aa !important;
}

.modal-result-yes {
  background-color: #00e676 !important;
  color: #fff;
}

.modal-result-no {
  background-color: #b71c1c !important;
  color: #fff;
}

.modal-backdrop {
    opacity: 0.5;
}
</style>
