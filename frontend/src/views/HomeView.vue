<template>
  <div>
    <div class="home">
      <h1>Home Page</h1>
    </div>
    <div>
      <!-- <div class="select">
        <span class="scenario">Scenario: </span>
        <select>
          <option value="scenario1">scenario1</option>
          <option value="scenario2">scenario2</option>
          <option value="scenario3">scenario3</option>
        </select>
      </div> -->
      <div class="listScenario">
        <Test />
      <!-- <Map /> -->
      </div>
      <button @click="showFilter" class="compare">
        <div class="comparison">
          <div class="lines">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <span class="right">Filter</span>
        </div>
      </button>
    </div>
    
    <div v-if="isPlaying" class="filter">
      <Filter />
      <div class="overlay" @click.self="closeFilter">
      </div>
    </div>

    <div class="mastodon-chart">
      <MChart />
    </div>

  </div>

</template>

<script>
import Filter from '../components/Filter.vue'
import Map from '../components/Map.vue'
import Test from '../components/test.vue'
import MChart from '../components/mastodonChart.vue'

export default {
  name: 'HomeView',
  components: { Filter, Map, Test, MChart },
  data() {
    return {
      // chartData: {
      //     labels: ['Label 1', 'Label 2', 'Label 3'],
      //     datasets: [
      //       {
      //         label: 'Data',
      //         backgroundColor: 'rgba(75, 192, 192, 0.2)',
      //         borderColor: 'rgba(75, 192, 192, 1)',
      //         borderWidth: 1,
      //         data: [10, 20, 15]
      //       }
      //     ]
      //   },
      //   chartOptions: {
      //     responsive: true,
      //     maintainAspectRatio: false,
      //     // Adjust the size of the chart
      //     height: 300, // Set the desired height
      //     width: 400 // Set the desired width
      //   },
        isPlaying: false
    }
  },
  methods: {
    showFilter() {
      this.isPlaying = !this.isPlaying
    },
    closeFilter() {
      this.isPlaying = false
    }
  }
}
</script>

<style>
  .home {
    text-align: center;
    border-bottom: 1px solid #ddd;
  }
  .home h1 {
    display: inline-block;
    font-family: arial;
    font-size: 20px;
    color: #000000;
    width: 200px;
  }
  .select {
    display: inline-block;
    position: relative;
    background: white;
    padding: 10px 10px;
    border-radius: 12px;
    z-index: 2;
  }
  .listScenario {
    display: inline-block;
  }
  .select select {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px 5px;
    gap: 4px;
    width: 500px;
    height: 40px;
    background: #FFFFFF;
    border: 1px solid #D9D9D9;
    box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.043);
    border-radius: 8px;
    font-size: 1em;
    font-family: arial;
  }
  .select select:hover {
    cursor: pointer;
  }
  .lines {
    display: inline-block;
  }
  .lines span {
    display: block;
    width: 15px;
    border-top: 1px solid black;
    margin-top: 3px;
    margin-bottom: 3px;
    margin-right: 5px;
  }
  .compare {
    display: inline-block;
    position: relative;
    background: white;
    border: 1px solid #d9d9d9;
    border-radius: 32px;
    z-index: 2;
    top: 17.2px;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    color: #000000;
    padding: 10px 20px;
  }
  .compare:hover {
    background: #eee;
    cursor: pointer;
  }
  .comparison {
    display: flex;
    align-items: center;
  }
  /* .right {
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    color: #000000;
    padding: 10px 20px;
  } */
  .filterSign {
    width: 20px;
    height: auto;
    padding: 10px 5px;
  }
  .filter {
    display: block;
    top: 12%;
    height: 400px;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.05);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
  }

  .mastodon-chart {
    position: absolute;
    top: 40%;
    width: 20%;
    height: 40%;
    /* left: 5%; */
    z-index: 1;
  }
</style>