<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: ['chartData'],
  computed: {
    getlabels () {
      return this.$store.getters.graphlabels
    }
  },
  mounted () {
    this.renderLineChart();
  },
  methods: {
    renderLineChart: function() {
      this.renderChart(
        {
          labels: this.$store.getters.graphlabels,
          datasets: this.$store.getters.graphdata
        },
        { responsive: true, maintainAspectRatio: false }
      );      
    }
  },
  watch: {
    getlabels: function() {
      this.$data._chart.destroy()
      this.renderLineChart();
    }
  }
}
</script>

<style scoped>
</style>