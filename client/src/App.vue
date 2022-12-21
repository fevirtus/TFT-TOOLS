<script setup>
import axios from "axios";
import { ref } from "vue";
import HelloWorld from "./components/HelloWorld.vue";

const path = "http://127.0.0.1:5000";

const result = ref();

const getTest = async (path) => {
  result.value = (await axios.get(path)).data;
  console.log(result);
};

getTest(path);
</script>

<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <div>123: {{ result }}</div>
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
