<template>
    <div>
        <h2 class="header">Score Board</h2>


        <GChart
          type="LineChart"
          :data="chartData"
          :options="chartOptions"
        />


        <hr>
        <h3>Teams</h3>
        <table id="socreboard" class="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team name</th>
              <th>Correct Flags</th>
              <th>Wrong Flags</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(team, index) in this.$store.getters.teamRanks" :key="team.id" style="cursor: pointer;" @click="$router.push(`/team/${team.name}`);">
                <td>{{index+1}}</td>
                <td>{{team.name}}</td>
                <td>{{team.correctFlags}}</td>
                <td>{{team.wrongFlags}}</td>
                <td>{{team.points}}</td>
            </tr>
          </tbody>
        </table>
        
    </div>
</template>

<script>

export default {
  name: 'scoreboard',
  data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Year', 'Sales', 'Expenses', 'Profit'],
        ['2014', 1000, 400, 200],
        ['2015', 1170, 0, 250],
        ['2016', 660, 1120, 300],
        ['2017', 1030, 540, 350]
      ],
      chartOptions: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        }
      }
    }
  },
  beforeMount () {
    this.$store.dispatch('loadTeams');
    this.$store.dispatch('connectScoreboard');
  }
}
</script>

<style scoped>
.header {
  text-align: left;
  margin: 10px 0 20px 10px;
  font-family: "Marker Felt";
}
</style>