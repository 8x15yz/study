<template>
  <div id="app">
    <h1>App.vue Page</h1>
    <p>최상위 컴포넌트</p>
    <p>emit 받은 문장: {{sendedEmitData}}</p>
    <hr>
    <input type="text" v-model="propData" @keyup.enter="inputDataChange">
    <p>이 문장은 씀과 동시에 나오고 {{propData}}</p>
    <p>이 문장은 쓰고 엔터를 쳐야 나와 {{whatsData}}</p>
    <TheAbout 
      :whats-data="whatsData"
      @emit-function="emitFunction"/>
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
      propData: 'basicsource +',
      whatsData:'',
      sendedEmitData: '하위 컴포넌트에서 받아온 데이터로 대체될 예정'
    }
  },
  methods: {
    inputDataChange(propData) {
      console.log(propData.path[0]._value) // 데이터의 path => [0] => _value 에 데이터 값이 있음
      this.whatsData = propData.path[0]._value
    },
    emitFunction(emitData) {
      this.sendedEmitData = emitData
      console.log('여기는 됐나 ?')
    }
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
  margin-top: 60px;
  border: 1px solid red;
}
</style>
