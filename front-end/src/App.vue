<template class="align-content-center">
  <div class="pt-4" id="app">
    <h1 class="text-center">Loan Prediction Model</h1>
    <Form />
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
//import { BootstrapVue } from "bootstrap-vue";
import Form from "./components/Form";
import { IconsPlugin } from 'bootstrap-vue';
Vue.use(IconsPlugin)

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
  background-image: linear-gradient(rgba(202, 154, 207, 0.705),  #f3e5f5);
  

  height: 100vh;

  overflow-x: hidden;
}

.ribbon{
    background-image: url("./assets/finastra_ribbon.png");
    background-repeat: no-repeat;
    padding-bottom: 30%;
  }
  

.inputLables{
  font-weight: bold!important;
}
.card {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.1);
}

.modalButton{
  background-color:white !important;
  
}
.modalText{
  color:black;
  align-items: center!important;
}
.btn-info{
  background-color: #8e24aa !important;
}

.modal-result-yes {
  
  color: #fff;
}

#modal-title{
  align-content: center;
}

.modal-result-no {
 
  color: #fff;
}

.imageSource-no{
  background-image: url('./assets/cross.png');
}

.imageSource-yes{
  background-image: url('./assets/check.png');
}

.modal-backdrop {
    opacity: 0.5;
}
</style>
