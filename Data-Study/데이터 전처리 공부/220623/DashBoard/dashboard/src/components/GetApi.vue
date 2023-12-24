<template>
    <div>
        <div v-for="(trade, idx) in trades" :key="idx">
            {{trade.id}} {{trade.amo_im}}
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'GetApi',
    data() {
        return {
            trades: []
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/api/v1/trade_list')
            .then(response => {
                console.log(response.data)
                this.trades = response.data
            })
            .catch(err => {
                console.log('there is somthing wrong with this process')
                console.log(err)
            })
    }
}




</script>