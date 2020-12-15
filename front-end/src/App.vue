<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>LPM</h1>
    <Form/>
  </div>
</template>

<script>
import Form from './components/Form'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  name: 'App',
  components: {
    Form
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  
  justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left | right ... + safe | unsafe;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
