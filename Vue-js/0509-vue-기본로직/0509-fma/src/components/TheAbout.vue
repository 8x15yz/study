<template>
  <div id="theAbout">
      <h1>TheAbout Page</h1>
      <p>하위 컴포넌트인 것이다</p>
      <p>prop 받은 문장: {{whatsData}}</p>
      <input type="text" v-model="emitData" 
      @click="clearFunction"
      @keyup.enter="emitFunction">
  </div>
</template>

<script>
export default {
  name: 'TheAbout', // 이게 있어야 prop이 되네 ??
  props: {
    whatsData: String
  },
  data() {
    return {
      emitData: '여기에 아이디를 입력하세요'
    }
  },
  methods: {
    emitFunction() {
      this.$emit('emit-function', this.emitData)
      console.log('이 단계는 됐을까 ?')
    },
    clearFunction() {
      this.emitData=''
    }
  },
}
</script>

<style>
#theAbout {
  border: 1px solid blue;
  padding: 2rem;
  margin: 1rem
}
</style>