<template>
  <div id="theabout">
      <h1>here is lower class</h1>
      <input type="text" 
      v-model="visualised"
      @click="clickedFunction"
      @keyup.enter="enterdFunction"
      >
      <p>prop 받은 데이터: {{propData}}</p>
      
  </div>
</template>

<script>
export default {
    name: 'TheAbout',
    props: {
        propData:String
    },
    data() {
        return {
            emitData: '',
            visualised: '몬가를 입력해봐'
        }
    },
    methods: {
        clickedFunction() {
            this.visualised=''
        },
        enterdFunction(event) {
            this.emitData=event.path[0]._value
            this.$emit('emit-keyword', this.emitData)
        }
    }

}
</script>

<style>
#theabout {
    border: 10px solid gold;
    padding: 1rem;
    text-align: center;
}
</style>