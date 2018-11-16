import { Line, mixins } from 'vue-chartjs'

export default {
  extends: Line,
  props: ['labels'],
  mixins: [mixins.reactiveProp],
  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: this.labels,
      datasets: this.chartData,
     
      // datasets: [
      //   {
      //     label: 'Team 1',
      //     backgroundColor: '#f87979',
      //     borderColor: '#f87979',
      //     fill: false,
      //     data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
      //   },
      //   {
      //     label: 'Team 2',
      //     backgroundColor: '#837979',
      //     borderColor: '#837979',
      //     fill: false,
      //     data: [56, 20, 12, 39, 67, 67, 39, 80, 12, 20, 12, 20]
      //   }
      // ]
    },{
      maintainAspectRatio:false,
    })
  }
}