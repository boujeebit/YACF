<script>
import { api } from "@/utils/api";
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: ["name"],
  data() {
    return {
      graphloading: true,
      graphlabels: [],
      graphdata: []
    };
  },
  computed: {
    getlabels() {
      return this.graphloading;
    }
  },
  //   beforeMount() {
  //     let that = this;
  //     api('mutation{ teamgraph(name:"Team5"){ timeline, message } }').then(
  //       data => {
  //         that.graphlabels = JSON.parse(data.teamgraph.timeline);
  //         that.graphdata = JSON.parse(data.teamgraph.message);
  //         that.graphloading = false;
  //         console.log(data.teamgraph.timeline, data.teamgraph.message);
  //       }
  //     );
  //   },
  mounted() {
    this.renderLineChart();
  },
  methods: {
    renderLineChart: function() {
      console.log("Graphing: ", this.$props.name);
      let that = this;
      api(
        `mutation{ teamgraph(name:"${this.$props.name}"){ timeline, message } }`
      ).then(data => {
        that.renderChart(
          {
            labels: JSON.parse(data.teamgraph.timeline),
            datasets: JSON.parse(data.teamgraph.message)
          },
          { responsive: true, maintainAspectRatio: false }
        );
        console.log(data.teamgraph.timeline, data.teamgraph.message);
      });
    }
  }
  //   watch: {
  //     graphloading: function() {
  //       this.$data._chart.update();
  //       this.renderLineChart();
  //     }
  //   }
};
</script>

<style scoped>
</style>