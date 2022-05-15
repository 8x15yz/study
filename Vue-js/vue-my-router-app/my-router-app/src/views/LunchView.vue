<template>
  <div class="d-flex m-5 justify-content-evenly">
      <div id="outLine">
          <h1>LunchView</h1>
      </div>
    
    <div class="">
        <ChartVue />
    </div>
  </div>
</template>

<script>
import ChartVue from '@/components/ChartVue.vue'

export default {
    name: 'LunchView',
    components: {
        ChartVue
    }
}
</script>

<style>
#outLine {
  outline: solid green;
  width: 600px;
  padding: 2rem;
}
</style>