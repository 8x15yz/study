<template>
  <div class="d-flex">
    <div id="app">
      <h1>here is upper class</h1>
      <input type="text" 
      v-model="visualised" 
      @click="clickedFunction"
      @keyup.enter="enterdFunction">
      <p>emit 받은 데이터: {{sendedData}}</p>
    </div>
    
    <TheAbout 
    :prop-data="propData" 
    @emit-keyword="sendedEmitFunction"
    />
  </div>
</template>

<script>
import TheAbout from '@/components/TheAbout.vue'

export default {
  name: 'App',
  components: {
    TheAbout
  },
  data() {
    return {
      visualised: '뭔가를 입력해보세요',
      propData: '',
      sendedData: ''
    }
  },
  methods: {
    enterdFunction(event) {
      this.propData = event.path[0]._value
    },
    clickedFunction() {
      this.visualised=''
    },
    sendedEmitFunction(data) {
      this.sendedData=data
    }
  }
}
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  outline: 10px;
  border: 10px solid black;
  padding: 1rem;
}
</style>
