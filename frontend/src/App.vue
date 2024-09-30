<template>
  <div id="app">
    <FormularioPlan />
  </div>
</template>

<script>
import FormularioPlan from './components/FormularioPlan.vue';

export default {
  components: {
    FormularioPlan
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  padding: 20px;
}

</style>