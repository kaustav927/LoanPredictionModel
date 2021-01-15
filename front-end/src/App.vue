<template class="align-content-center">
  <div class="pt-4 ribbon" id="app">
    <i @click="showInfoModal" class="fa fa-info-circle help-icon"></i>
    <div class="d-flex justify-content-center">
      <img src="logo.png" class="img-responsive" width="300px" alt="">
    </div>
    <Form />
    <Footer />
    <info-modal></info-modal>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
//import { BootstrapVue } from "bootstrap-vue";
import Form from "./components/Form";
import InfoModal from "./components/InfoModal";
import Footer from "./components/Footer";
import { IconsPlugin } from 'bootstrap-vue';
Vue.use(IconsPlugin)

Vue.use(VueAxios, axios);
export default {
  name: "App",
  components: {
    Form,
    InfoModal,
    Footer
  },
  methods: {
    showInfoModal() {
      this.$nextTick(() => {
        this.$bvModal.show('modal-info')
      })
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 22px !important;

  color: #2c3e50;
  background:  url("./assets/finastra_ribbon.png") no-repeat, linear-gradient(rgba(255, 255, 255, 0.705),  #f4adff);
  background-position: bottom;
  background-size: contain;
  height: 100vh;
  overflow-x: hidden;
} 

.form-control {
  font-size: 20px !important;
}

input:focus {
  box-shadow: none !important;
  border-color:  #8e24aa !important;
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

.btn-info {
  background-color: #8e24aa !important;
  border-color: #8e24aa !important;
  outline: none !important;
  box-shadow: none !important;
}

.btn-info:focus {
  outline: none !important;
  box-shadow: none !important;
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

.help-icon {
  color: #8e24aa !important;
  position: absolute;
  top: 20px;
  right: 20px;
  cursor: pointer;
}

.page-footer {
  position: fixed;
  bottom: 0px;
  width: 100%;
  background-color: #424242;
  color: white;
  font-weight: bold;
}

.page-footer  a {
  color: white !important;
}

.loader,
.loader:after {
  border-radius: 50%;
  width: 10em;
  height: 10em;
}
.loader {
  margin-left: auto;
  margin-right: auto;
  font-size: 3px;
  position: relative;
  text-indent: -9999em;
  border-top: 1.1em solid rgba(255, 255, 255, 0.2);
  border-right: 1.1em solid rgba(255, 255, 255, 0.2);
  border-bottom: 1.1em solid rgba(255, 255, 255, 0.2);
  border-left: 1.1em solid #ffffff;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation: load8 1.1s infinite linear;
  animation: load8 1.1s infinite linear;
}
@-webkit-keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>
