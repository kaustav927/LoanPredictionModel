<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>LPM</h1>
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
  margin-top: 60px;
}
</style>
