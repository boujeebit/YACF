<script>
import { api } from "@/utils/api";
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: ["chartData"],
  data() {
    return {
      graphloading: true,
      graphlabels: [],
      graphdata: []
    };
  },
  computed: {
    getlabels() {
      return this.$store.getters.graphlabels;
    }
  },
  beforeMount() {
    let that = this;
    api("mutation{ graph{ timeline, message } }").then(data => {
      that.$store.commit("SET_GRAPH", {
        data: JSON.parse(data.graph.message),
        labels: JSON.parse(data.graph.timeline)
      });

      that.graphloading = false;
    });
  },
  mounted() {
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
      this.$data._chart.update();
      this.renderLineChart();
    }
  }
};
</script>

<style scoped>
</style>