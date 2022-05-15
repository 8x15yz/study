<template>
  <div class="d-flex m-5 justify-content-evenly">
      <div id="outLine">
          <h1>LottoVue</h1>
          <button
          @click="selectedNumbers"
          >
          get numbers
          </button>
          <p>{{selectedNumbers}}</p>
      </div>
    
    <div>
        <ChartVue />
    </div>
  </div>
</template>

<script>
import ChartVue from '@/components/ChartVue.vue'
import _ from 'lodash'

export default {
    name: 'LottoVue',
    components: {
        ChartVue
    },
    data() {
        return {
            selectedNumbers: null
        }
    },
    methods: {
    getLuckyNumbers() {
      this.selectedNumbers = _.sortBy(_.sampleSize(_.range(1, 46), this.$route.params.number))
    }
  },
  created() {
    console.log('created', this.$route.params.number)
  },
  mounted() {
    console.log('mounted', this.$route.params.number)
  },
  updated() {
    console.log('updated', this.$route.params.number)
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