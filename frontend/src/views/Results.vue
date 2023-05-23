<template>
  <div>
    <div class="menu">
      <div class="current">      
        <span v-if="this.scenario1 === 'unemployment'">Main Scenario: <br>Employment Discussion Rate</span>
        <span v-if="this.scenario1 === 'agism'">Main Scenario: <br>Agism Discussion Rate<br></span>
        <span v-if="this.scenario1 === 'sexism'">Main Scenario: <br>Sexism Discussion Rate<br></span>
        <br>
        <span v-if="this.scenario2 === 'unemployment' && !this.scenario3">Compared Scenario: <br>Official Employment Rate</span>
        <span v-if="this.scenario2 === 'agism' && !this.scenario3">Compared Scenario: <br>Official Aging Rate</span>
        <span v-if="this.scenario2 === 'sexism' && !this.scenario3">Compared Scenario: <br>Official Gender Ratio</span>
        <span v-if="this.scenario2 === 'unemployment' && this.scenario3">Compared Scenario1: <br>Employment Discussion Rate</span>
        <span v-if="this.scenario2 === 'agism' && this.scenario3">Compared Scenario1: <br>Agism Discussion Rate</span>
        <span v-if="this.scenario2 === 'sexism' && this.scenario3">Compared Scenario1: <br>Sexism Discussion Rate</span>
        <br>
        <span v-if="this.scenario3 === 'unemployment'">Compared Scenario2: <br>Employment Discussion Rate</span>
        <span v-if="this.scenario3 === 'agism'">Compared Scenario2: <br>Agism Discussion Rate</span>
        <span v-if="this.scenario3 === 'sexism'">Compared Scenario2: <br>Sexism Discussion Rate</span>
        <br v-if="this.scenario3">
        <!-- <span>Current Sudo Scenario: {{ $route.params.scenario2 }}</span> -->
        <!-- <span v-else>Current Scenario: {{ scenario }}</span> -->
        <span v-if="this.location === 'newsouthwales'">Current Location: <br>New South Wales</span>
        <span v-if="this.location === 'victoria'">Current Location: <br>Victoria</span>
        <span v-if="this.location === 'queensland'">Current Location: <br>Queensland</span>
        <span v-if="this.location === 'southaustralia'">Current Location: <br>South Australia</span>
        <span v-if="this.location === 'westernaustralia'">Current Location: <br>Western Australia</span>
        <span v-if="this.location === 'tasmania'">Current Location: <br>Tasmania</span>
        <span v-if="this.location === 'australiancapitalterritory'">Current Location: <br>Australian Capital Territory</span>
        <span v-if="this.location === 'northernterritory'">Current Location: <br>Northern Territory</span>
        <span v-if="this.location === 'offshoreterritories'">Current Location: <br>Offshore Territories</span>
        <!-- <span v-else>Current Location: {{ location }}</span> -->
      </div>

      <div class="back">
        <button @click="goBack">Back</button>
      </div>
      <!-- <div class="choose">
        <span class="title">Change Main Topics</span>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown1">
            1. Employment discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen1 }">
            <li>
              <button @click="this.scenario2 = 'unemployment'">vs offical employment rate</button>
            </li>
            <li>
              <button @click="this.scenario2 = 'agism'">vs offical Aging Rate</button>
            </li>
            <li>
              <button @click="this.scenario2 = 'sexism'">vs offical gender ratio</button>
            </li>
            <li>
              <button>vs other 2 scenarios mentioned in tweets</button>
            </li>
          </ul>
        </div>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown2">
            2. Agism discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen2 }">
            <li>
              <button @click="this.scenario2 = 'agism'">vs offical Aging Rate</button>
            </li>
            <li>
              <button>vs other 2 scenarios mentioned in tweets</button>
            </li>
          </ul>
        </div>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown3">
            3. Sexism discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen3 }">
            <li>
              <button @click="this.scenario2 = 'sexism'">vs offical gender ratio</button>
            </li>
            <li>
              <button>vs other 2 scenarios mentioned in tweets</button>
            </li>
          </ul>
        </div>
        <div class="location">
          <span>Change the location: </span>
          <select v-model="location">
            <option value="newsouthwales">NSW</option>
            <option value="victoria">VIC</option>
            <option value="queensland">QLD</option>
            <option value="southaustralia">SA</option>
            <option value="westernaustralia">WA</option>
            <option value="tasmania">ACT</option>
            <option value="australiancapitalterritory">NT</option>
            <option value="northernterritory">TAS</option>
            <option value="offshoreterritories">Other</option>
          </select>
        </div>
        
        <div class="confirm">
          <span v-if="!this.scenario2">Please choose a scenario!</span>
          <button @click="confirm" :disabled="!this.scenario2">Confirm</button>
        </div> -->
      <!-- </div> -->
    </div>
    <div class="map1">
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'newsouthwales'">Employment Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'victoria'">Employment Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'queensland'">Employment Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'southaustralia'">Employment Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'westernaustralia'">Employment Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'tasmania'">Employment Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'australiancapitalterritory'">Employment Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'northernterritory'">Employment Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario1 === 'unemployment' && this.location === 'offshoreterritories'">Employment Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'newsouthwales'">Sexism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'victoria'">Sexism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'queensland'">Sexism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'southaustralia'">Sexism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'westernaustralia'">Sexism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'tasmania'">Sexism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'australiancapitalterritory'">Sexism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'northernterritory'">Sexism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario1 === 'sexism' && this.location === 'offshoreterritories'">Sexism Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'newsouthwales'">Agism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'victoria'">Agism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'queensland'">Agism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'southaustralia'">Agism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'westernaustralia'">Agism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'tasmania'">Agism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'australiancapitalterritory'">Agism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'northernterritory'">Agism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario1 === 'agism' && this.location === 'offshoreterritories'">Agism Discussion Rate on Twitter for Offshore Territories</h4>
      <div id="map1"></div>
    </div>
    <div v-if="!this.scenario3" class="map2">
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'newsouthwales'">Official Employment Rate for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'victoria'">Official Employment Rate for Victoria</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'queensland'">Official Employment Rate for Queensland</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'southaustralia'">Official Employment Rate for South Australia</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'westernaustralia'">Official Employment Rate for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'tasmania'">Official Employment Rate for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'australiancapitalterritory'">Official Employment Rate for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'northernterritory'">Official Employment Rate for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'offshoreterritories'">Official Employment Rate for Offshore Territories</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'newsouthwales'">Official Gender Ratio for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'victoria'">Official Gender Ratio for Victoria</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'queensland'">Official Gender Ratio for Queensland</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'southaustralia'">Official Gender Ratio for South Australia</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'westernaustralia'">Official Gender Ratio for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'tasmania'">Official Gender Ratio for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'australiancapitalterritory'">Official Gender Ratio for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'northernterritory'">Official Gender Ratio for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'offshoreterritories'">Official Gender Ratio for Offshore Territories</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'newsouthwales'">Official Aging Rate for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'victoria'">Official Aging Rate for Victoria</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'queensland'">Official Aging Rate for Queensland</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'southaustralia'">Official Aging Rate for South Australia</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'westernaustralia'">Official Aging Rate for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'tasmania'">Official Aging Rate for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'australiancapitalterritory'">Official Aging Rate for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'northernterritory'">Official Aging Rate for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'offshoreterritories'">Official Aging Rate for Offshore Territories</h4>
      <div id="map2"></div>
    </div>
    <div v-if="this.scenario3" class="map2">
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'newsouthwales'">Employment Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'victoria'">Employment Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'queensland'">Employment Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'southaustralia'">Employment Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'westernaustralia'">Employment Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'tasmania'">Employment Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'australiancapitalterritory'">Employment Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'northernterritory'">Employment Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'unemployment' && this.location === 'offshoreterritories'">Employment Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'newsouthwales'">Sexism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'victoria'">Sexism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'queensland'">Sexism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'southaustralia'">Sexism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'westernaustralia'">Sexism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'tasmania'">Sexism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'australiancapitalterritory'">Sexism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'northernterritory'">Sexism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'sexism' && this.location === 'offshoreterritories'">Sexism Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'newsouthwales'">Agism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'victoria'">Agism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'queensland'">Agism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'southaustralia'">Agism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'westernaustralia'">Agism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'tasmania'">Agism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'australiancapitalterritory'">Agism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'northernterritory'">Agism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario2 === 'agism' && this.location === 'offshoreterritories'">Agism Discussion Rate on Twitter for Offshore Territories</h4>
      <div id="map2"></div>
    </div>
    <div class="map3">
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'newsouthwales'">Employment Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'victoria'">Employment Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'queensland'">Employment Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'southaustralia'">Employment Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'westernaustralia'">Employment Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'tasmania'">Employment Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'australiancapitalterritory'">Employment Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'northernterritory'">Employment Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario3 === 'unemployment' && this.location === 'offshoreterritories'">Employment Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'newsouthwales'">Sexism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'victoria'">Sexism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'queensland'">Sexism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'southaustralia'">Sexism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'westernaustralia'">Sexism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'tasmania'">Sexism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'australiancapitalterritory'">Sexism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'northernterritory'">Sexism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario3 === 'sexism' && this.location === 'offshoreterritories'">Sexism Discussion Rate on Twitter for Offshore Territories</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'newsouthwales'">Agism Discussion Rate on Twitter for New South Wales</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'victoria'">Agism Discussion Rate on Twitter for Victoria</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'queensland'">Agism Discussion Rate on Twitter for Queensland</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'southaustralia'">Agism Discussion Rate on Twitter for South Australia</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'westernaustralia'">Agism Discussion Rate on Twitter for Western Australia</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'tasmania'">Agism Discussion Rate on Twitter for Tasmania</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'australiancapitalterritory'">Agism Discussion Rate on Twitter for Australian Capital Territory</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'northernterritory'">Agism Discussion Rate on Twitter for Northern Territory</h4>
      <h4 v-if="this.scenario3 === 'agism' && this.location === 'offshoreterritories'">Agism Discussion Rate on Twitter for Offshore Territories</h4>
      <div id="map3"></div>
    </div>

    <!-- <div class="chart">
      <Bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
    </div> -->
    <!-- <Chart /> -->
    <div v-if="!this.scenario3" class="dynamic-chart">
      <Chart />
    </div>


    <!-- <div class="graph2">
      <Graph />
    </div> -->

  </div>
</template>

<script>
import axios from 'axios';
import Chart from '../components/Chart.vue'

export default {
  name: 'Result',
  components: { Chart },

  data() {
    return {
        zoom_size: null,

        scenario1: null,
        scenario2: null,
        scenario3: null,
        // scenario1: null,
        // scenario2: null,
        scenario: null,
        location: null,
        isDropdownOpen1: false,
        isDropdownOpen2: false,
        isDropdownOpen3: false,
        map1: null,
        map2: null,
        circles1: [],
        circles2: [],
        circles3: [],
    //   keyword: null,
        keywordTweets: null,
        keywordSudo: null,

        center: null,
        twi_data: null,
        sudo_data: null,

        twi_data1: null,
        twi_data2: null,
        twi_data3: null,

        twi_percentage: [],
        twi_percentage1: [],
        twi_percentage2: [],
        twi_percentage3: [],

        twi_max: null,
        twi_min: null,
        twi_max1: null,
        twi_min1: null,
        twi_max2: null,
        twi_min2: null,
        twi_max3: null,
        twi_min3: null,
        sudo_max: null,
        sudo_min: null,

        twi_color: null,
        plot_radius: null
    };
  },
  created() {
    this.scenario = this.$route.params.scenario;
    this.location = this.$route.params.state;
    if (this.scenario.split('-').length === 2) {
      this.scenario1 = this.scenario.split('-')[0]
      this.scenario2 = this.scenario.split('-')[1]
    } else if (this.scenario.split('-').length === 3) {
      this.scenario1 = this.scenario.split('-')[0]
      this.scenario2 = this.scenario.split('-')[1]
      this.scenario3 = this.scenario.split('-')[2]
    }
    
  },
  watch: {
    "$route.params.scenario": function(newValue) {
      this.scenario = newValue;
    },
    "$route.params.state": function(newValue) {
      this.location = newValue;
    }
  },
  async mounted() {
    // console.log(this.scenario)
    // console.log(this.scenario1)
    // console.log(this.scenario2)
    // console.log(this.location)
    // const scenario1 = this.$route.params.scenario.split('-')[0];
    // const scenario2 = this.$route.params.scenario.split('-')[1];
    // const state = this.$route.params.state;

    if (!this.scenario3) {
      try {
        const twiResponse = await axios.get(`http://127.0.0.1:5000/api_twi_state_city/${this.scenario1}/${this.location}`);
        this.center = twiResponse.data.state;
        this.twi_data = twiResponse.data.results;
        this.twi_data.forEach(twi => {
          this.twi_percentage.push(twi.percentage)
        })
        this.twi_max = Math.max(...this.twi_percentage)
        this.twi_min = Math.min(...this.twi_percentage)
      } catch (error) {
        console.error('Failed to fetch Twitter data:', error);
      }

      try {
        const sudoResponse = await axios.get(`http://127.0.0.1:5000/api_sudo_state_city/${this.scenario2}/${this.location}`);
        this.sudo_data = sudoResponse.data.results;
        this.sudo_max = this.sudo_data[0].percentage
        this.sudo_min = this.sudo_data[this.sudo_data.length-1].percentage
      } catch (error) {
        console.error('Failed to fetch Sudo data:', error);
      }
    } else {
      try {
        const twiResponse1 = await axios.get(`http://127.0.0.1:5000/api_twi_state_city/${this.scenario1}/${this.location}`);
        this.center = twiResponse1.data.state;
        this.twi_data1 = twiResponse1.data.results;
        this.twi_data1.forEach(twi => {
          this.twi_percentage1.push(twi.percentage)
        })
        this.twi_max1 = Math.max(...this.twi_percentage1)
        this.twi_min1 = Math.min(...this.twi_percentage1)
      } catch (error) {
        console.error('Failed to fetch Twitter data:', error);
      }

      try {
        const twiResponse2 = await axios.get(`http://127.0.0.1:5000/api_twi_state_city/${this.scenario2}/${this.location}`);
        // this.center = twiResponse.data.state;
        this.twi_data2 = twiResponse2.data.results;
        this.twi_data2.forEach(twi => {
          this.twi_percentage2.push(twi.percentage)
        })
        this.twi_max2 = Math.max(...this.twi_percentage2)
        this.twi_min2 = Math.min(...this.twi_percentage2)
      } catch (error) {
        console.error('Failed to fetch Twitter data:', error);
      }

      try {
        const twiResponse3 = await axios.get(`http://127.0.0.1:5000/api_twi_state_city/${this.scenario3}/${this.location}`);
        // this.center = twiResponse.data.state;
        this.twi_data3 = twiResponse3.data.results;
        this.twi_data3.forEach(twi => {
          this.twi_percentage3.push(twi.percentage)
        })
        this.twi_max3 = Math.max(...this.twi_percentage3)
        this.twi_min3 = Math.min(...this.twi_percentage3)
      } catch (error) {
        console.error('Failed to fetch Twitter data:', error);
      }
    }

    this.initMap();
    this.createCircles();
  },
  methods: {
    goBack() {
      this.$router.push('/')
    },
    // toggleDropdown1() {
    //   this.scenario1 = "unemployment"
    //   this.isDropdownOpen1 = !this.isDropdownOpen1;
    // },
    // toggleDropdown2() {
    //   this.scenario1 = "agism"
    //   this.isDropdownOpen2 = !this.isDropdownOpen2;
    // },
    // toggleDropdown3() {
    //   this.scenario1 = "sexism"
    //   this.isDropdownOpen3 = !this.isDropdownOpen3;
    // },
    initMap() {
      // const state = this.$route.params.state
      if (this.location === 'newsouthwales') {
        this.zoom_size = 5.3
      } else if (this.location === 'victoria') {
        this.zoom_size = 5.8
      } else if (this.location === 'queensland') {
        this.zoom_size = 4.9
      } else if (this.location === 'southaustralia') {
        this.zoom_size = 4.4
      } else if (this.location === 'westernaustralia') {
        this.zoom_size = 4.2
      } else if (this.location === 'tasmania') {
        this.zoom_size = 6.4
      } else if (this.location === 'australiancapitalterritory') {
        this.zoom_size = 7
      } else if (this.location === 'northernterritory') {
        this.zoom_size = 4.8
      } else {
        this.zoom_size = 7
      }
      this.map1 = new google.maps.Map(document.getElementById('map1'), {
          // center: { lat: -25.2744, lng: 133.7751 },
          center: this.center,
          zoom: this.zoom_size,
          gestureHandling: "none",
          disableDefaultUI: true
      })
      this.map2 = new google.maps.Map(document.getElementById('map2'), {
          // center: { lat: -25.2744, lng: 133.7751 },
          center: this.center,
          zoom: this.zoom_size,
          gestureHandling: "none",
          disableDefaultUI: true
      })
      if (this.scenario3) {
        this.map3 = new google.maps.Map(document.getElementById('map3'), {
          // center: { lat: -25.2744, lng: 133.7751 },
          center: this.center,
          zoom: this.zoom_size,
          gestureHandling: "none",
          disableDefaultUI: true
      })
      }
      // }
    },
    createCircles() {
      if (!this.scenario3) {
        this.twi_data.forEach(tweet => {
            if ((this.location !== 'australiancapitalterritory') && (this.location !== 'northernterritory') && (this.location !== 'offshoreterritories')) {
              if (tweet.rank === 1) {
                this.twi_color = '#ff6347'
              } else if (tweet.rank === -1) {
                this.twi_color = '#1e90ff'
              } else {
                this.twi_color = '#696969'
              }
            } else {
              this.twi_color = '#696969'
            }
            
            if (tweet.percentage === 0){
              this.plot_radius = 0
            } else{
              this.plot_radius = (1 + 9 * (tweet.percentage - this.twi_min) / (this.twi_max - this.twi_min)) * 25000 / (this.zoom_size ** (1/2)) 
            }

            const circleOptions = {
                strokeColor: this.twi_color,
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: this.twi_color,
                fillOpacity: 0.35,
                map: this.map1,
                center: new google.maps.LatLng(tweet.lat, tweet.lng),
                radius: this.plot_radius
            };
            const circle1 = new google.maps.Circle(circleOptions);
            circle1.addListener('mouseover', () => {
                this.showInfoWindow1(circle1, tweet.city, tweet.count, tweet.total, tweet.percentage);
            });
            circle1.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles1.push(circle1);
        });

        this.sudo_data.forEach(sudo => {
            const circleOptions = {
                strokeColor: '#404040',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#808080',
                fillOpacity: 0.35,
                map: this.map2,
                center: new google.maps.LatLng(sudo.lat, sudo.lng),
                // radius: (sudo.percentage - this.sudo_min * 0.9) ** 2 * 50 
                radius: (1+9 * (sudo.percentage - this.sudo_min) / (this.sudo_max - this.sudo_min)) * 25000 / (this.zoom_size ** (2/3)) 
            };
            const circle2 = new google.maps.Circle(circleOptions);
            circle2.addListener('mouseover', () => {
              if (this.scenario2 === 'unemployment') {
                this.showInfoWindow2(circle2, sudo.city, sudo.population, sudo.percentage);
              } else if (this.scenario2 === 'agism') {
                this.showInfoWindow3(circle2, sudo.city, sudo.population, sudo.percentage);
              } else if (this.scenario2 === 'sexism') {
                this.showInfoWindow4(circle2, sudo.city, sudo.population, sudo.percentage);
              }
                
            });
            circle2.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles2.push(circle2);
        });
      } else {
        this.twi_data1.forEach(tweet => {
            if ((this.location !== 'australiancapitalterritory') && (this.location !== 'northernterritory') && (this.location !== 'offshoreterritories')) {
              if (tweet.rank === 1) {
                this.twi_color = '#ff6347'
              } else if (tweet.rank === -1) {
                this.twi_color = '#1e90ff'
              } else {
                this.twi_color = '#696969'
              }
            } else {
              this.twi_color = '#696969'
            }
            
            if (tweet.percentage === 0){
              this.plot_radius = 0
            } else{
              this.plot_radius = (1 + 9 * (tweet.percentage - this.twi_min1) / (this.twi_max1 - this.twi_min1)) * 25000 / (this.zoom_size ** (1/2)) 
            }

            const circleOptions = {
                strokeColor: this.twi_color,
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: this.twi_color,
                fillOpacity: 0.35,
                map: this.map1,
                center: new google.maps.LatLng(tweet.lat, tweet.lng),
                radius: this.plot_radius
            };
            const circle1 = new google.maps.Circle(circleOptions);
            circle1.addListener('mouseover', () => {
                this.showInfoWindow1(circle1, tweet.city, tweet.count, tweet.total, tweet.percentage);
            });
            circle1.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles1.push(circle1);
        });

        this.twi_data2.forEach(tweet => {
            if ((this.location !== 'australiancapitalterritory') && (this.location !== 'northernterritory') && (this.location !== 'offshoreterritories')) {
              if (tweet.rank === 1) {
                this.twi_color = '#ff6347'
              } else if (tweet.rank === -1) {
                this.twi_color = '#1e90ff'
              } else {
                this.twi_color = '#696969'
              }
            } else {
              this.twi_color = '#696969'
            }
            
            if (tweet.percentage === 0){
              this.plot_radius = 0
            } else{
              this.plot_radius = (1 + 9 * (tweet.percentage - this.twi_min2) / (this.twi_max2 - this.twi_min2)) * 25000 / (this.zoom_size ** (1/2)) 
            }

            const circleOptions = {
                strokeColor: this.twi_color,
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: this.twi_color,
                fillOpacity: 0.35,
                map: this.map2,
                center: new google.maps.LatLng(tweet.lat, tweet.lng),
                radius: this.plot_radius
            };
            const circle2 = new google.maps.Circle(circleOptions);
            circle2.addListener('mouseover', () => {
                this.showInfoWindow1(circle2, tweet.city, tweet.count, tweet.total, tweet.percentage);
            });
            circle2.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles2.push(circle2);
        });

        this.twi_data3.forEach(tweet => {
            if ((this.location !== 'australiancapitalterritory') && (this.location !== 'northernterritory') && (this.location !== 'offshoreterritories')) {
              if (tweet.rank === 1) {
                this.twi_color = '#ff6347'
              } else if (tweet.rank === -1) {
                this.twi_color = '#1e90ff'
              } else {
                this.twi_color = '#696969'
              }
            } else {
              this.twi_color = '#696969'
            }
            
            if (tweet.percentage === 0){
              this.plot_radius = 0
            } else{
              this.plot_radius = (1 + 9 * (tweet.percentage - this.twi_min3) / (this.twi_max3 - this.twi_min3)) * 25000 / (this.zoom_size ** (1/2)) 
            }

            const circleOptions = {
                strokeColor: this.twi_color,
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: this.twi_color,
                fillOpacity: 0.35,
                map: this.map3,
                center: new google.maps.LatLng(tweet.lat, tweet.lng),
                radius: this.plot_radius
            };
            const circle3 = new google.maps.Circle(circleOptions);
            circle3.addListener('mouseover', () => {
                this.showInfoWindow1(circle3, tweet.city, tweet.count, tweet.total, tweet.percentage);
            });
            circle3.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles3.push(circle3);
        });
      }
    },
    showInfoWindow1(circle, city, count, total, percentage) {
      const infoWindow1 = new google.maps.InfoWindow({
        content: `Name: ${city}<br>Count: ${count}<br>Total: ${total}<br>Percentage: ${percentage.toFixed(3)}%`,
        // disableAutoPan: true
      });
      infoWindow1.setPosition(circle.getCenter());
      infoWindow1.open(this.map1);
      this.infoWindow = infoWindow1;
    },
    showInfoWindow2(circle, city, population, percentage) {
      const infoWindow2 = new google.maps.InfoWindow({
        content: `Name: ${city}<br>Employed Population: ${population}<br>Employment Rate: ${percentage.toFixed(3)}%`,
        // disableAutoPan: true
      });
      infoWindow2.setPosition(circle.getCenter());
      infoWindow2.open(this.map2);
      this.infoWindow = infoWindow2;
    },
    showInfoWindow3(circle, city, population, percentage) {
      const infoWindow2 = new google.maps.InfoWindow({
        content: `Name: ${city}<br>Ageing Population: ${population}<br>Ageing Rate: ${percentage.toFixed(3)}%`,
        // disableAutoPan: true
      });
      infoWindow2.setPosition(circle.getCenter());
      infoWindow2.open(this.map2);
      this.infoWindow = infoWindow2;
    },
    showInfoWindow4(circle, city, population, percentage) {
      const infoWindow2 = new google.maps.InfoWindow({
        content: `Name: ${city}<br>Population Difference: ${population}<br>Gender Ratio: ${percentage.toFixed(3)}`,
        // disableAutoPan: true
      });
      infoWindow2.setPosition(circle.getCenter());
      infoWindow2.open(this.map2);
      this.infoWindow = infoWindow2;
    },
    hideInfoWindow() {
      if (this.infoWindow) {
        this.infoWindow.close();
      }
    }
    // confirm() {
    //     const new_scenario1 = this.scenario1;
    //     const new_scenario2 = this.scenario2;
    //     const new_state = this.location;

    //     try {
    //       const new_twiResponse = axios.get(`http://127.0.0.1:5000/api_twi_state_city/${new_scenario1}/${new_state}`);
    //       this.center = new_twiResponse.data.state;
    //       this.twi_data = new_twiResponse.data.results;
    //     } catch (error) {
    //       console.error('Failed to fetch Twitter data:', error);
    //     }

    //     try {
    //       const new_sudoResponse = axios.get(`http://127.0.0.1:5000/api_sudo_state_city/${new_scenario2}/${new_state}`);
    //       this.sudo_data = new_sudoResponse.data.results;
    //     } catch (error) {
    //       console.error('Failed to fetch Sudo data:', error);
    //     }

    //     this.initMap();
    //     this.createCircles();

    //     const scenario = this.scenario1 + '-' + this.scenario2
    //     // const new_state = this.location
    //     // this.$router.push({ name: 'results', params: { scenario: scenario, state: new_state } })
    //     this.$router.push({ path: `/${scenario}/${new_state}`, query: { scenario, new_state } })



        // this.$router.push({ path: `/${scenario}/${new_state}` });
        // window.location.reload();
    // }
  }
}
</script>

<style>
.dropdown-list {
  display: none;
  list-style: none;
  margin: 0;
  padding: 0;
}
.dropdown-list button {
  /* border: 1px solid #ddd; */
  border: none;
  border-bottom: 1px solid #ddd;
  background: white;
  width: 100%;
  padding: 3px;
  text-align: left;
}
.dropdown-list button:hover {
  background: #eee;
}
.dropdown-list.is-open {
  display: block;
}
.dropdown-item::before {
  content: none;
}
.dropdown-toggle {
  width: 100%;
  text-align: left;
}


.menu {
  position: absolute;
  width: 20%;
  height: 95%;
  border: 1px solid #ddd;
}
.menu div {
  position: relative;
}
.menu span {
  display: inline-block;
}
.current {
  position: relative;
  margin: 10px;
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
}
.current span {
  display: block;
}
.choose .title {
  position: relative;
  display: inline;
  margin: 20px;
  padding: 10px 0;
}
.choose div {
  position: relative;
  /* display: flex; */
  margin-top: 20px;
  margin-bottom: 60px;
}

.map1 {
    position: absolute;
    width: 33%;
    height: 40%;
    left: 25%;
    z-index: 1;
}
.map1 h3 {
    position: relative;
    z-index: 1;
}
#map1 {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
}
.map2 {
    position: absolute;
    width: 33%;
    height: 40%;
    right: 5%;
    z-index: 1;
}
.map2 h3 {
    position: relative;
    z-index: 1;
}
#map2 {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
}
.map3 {
    position: absolute;
    width: 33%;
    height: 40%;
    top: 50%;
    left: 43%;
    /* right: 5%; */
    z-index: 1;
}
.map3 h3 {
    position: relative;
    z-index: 1;
}
#map3 {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
}
/* .scenario {
    position: relative;
}
.scenario button {
    display: inline-block;
    position: relative;
    background: white;
    border: 1px solid #d9d9d9;
    padding: 10px 20px;
    border-radius: 32px;
    z-index: 2;
    top: 15px;
    margin-right: 10px;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    color: #000000;
}
.scenario button:hover {
  cursor: pointer;
  background: #eee;
} */

.dynamic-chart {
  position: absolute;
  top: 51%;
  width: 35%;
  /* height: 10%; */
  left: 25%;
  z-index: 1;
}
.graph2 {
  position: absolute;
  top: 50%;
  left: 25%;
}
.back button {
    position: relative;
    border: 1px solid #d9d9d9;
    padding: 5px 10px;
    border-radius: 8px;
    z-index: 2;
    top: 15px;
    margin-right: 10px;
    font-size: 1em;
    background: white;
}
.back button:hover {
  background: #eee;
  cursor: pointer;
}

</style>