<template>
  <div>
    <div class="menu">
      <div class="current">      
        <span v-if="this.twi_scenario === 'unemployment'">Main Scenario: <br>Employment Discussion Rate</span>
        <span v-if="this.twi_scenario === 'agism'">Main Scenario: <br>Agism Discussion Rate<br></span>
        <span v-if="this.twi_scenario === 'sexism'">Main Scenario: <br>Sexism Discussion Rate<br></span>
        <br>
        <span v-if="this.sudo_scenario === 'unemployment'">Compared Scenario: <br>Official Employment Rate</span>
        <span v-if="this.sudo_scenario === 'agism'">Compared Scenario: <br>Official Aging Percentage</span>
        <span v-if="this.sudo_scenario === 'sexism'">Compared Scenario: <br>Official Gender Ratio</span>
        <br>
        <!-- <span>Current Sudo Scenario: {{ $route.params.sudo_scenario }}</span> -->
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
              <button @click="this.sudo_scenario = 'unemployment'">vs offical employment rate</button>
            </li>
            <li>
              <button @click="this.sudo_scenario = 'agism'">vs offical aging percentage</button>
            </li>
            <li>
              <button @click="this.sudo_scenario = 'sexism'">vs offical gender ratio</button>
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
              <button @click="this.sudo_scenario = 'agism'">vs offical aging percentage</button>
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
              <button @click="this.sudo_scenario = 'sexism'">vs offical gender ratio</button>
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
          <span v-if="!this.sudo_scenario">Please choose a scenario!</span>
          <button @click="confirm" :disabled="!this.sudo_scenario">Confirm</button>
        </div> -->
      <!-- </div> -->
    </div>
    <div class="map1">
      <h3>Data from Twitter</h3>
      <div id="map1"></div>
    </div>
    <div class="map2">
      <h3>Data from Sudo</h3>
      <div id="map2"></div>
    </div>

    <!-- <div class="chart">
      <Bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
    </div> -->
    <!-- <Chart /> -->
    <div class="dynamic-chart">
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

        twi_scenario: null,
        sudo_scenario: null,
        scenario: null,
        location: null,
        isDropdownOpen1: false,
        isDropdownOpen2: false,
        isDropdownOpen3: false,
        map1: null,
        map2: null,
        circles1: [],
        circles2: [],
    //   keyword: null,
        keywordTweets: null,
        keywordSudo: null,

        center: null,
        twi_data: null,
        sudo_data: null,

        twi_percentage: [],

        twi_max: null,
        twi_min: null,
        sudo_max: null,
        sudo_min: null,

        twi_color: null,
        plot_radius: null
    };
  },
  created() {
    this.scenario = this.$route.params.scenario;
    this.twi_scenario = this.scenario.split('-')[0]
    this.sudo_scenario = this.scenario.split('-')[1]
    this.location = this.$route.params.state;
  },
  watch: {
    "$route.params.state": function(newValue) {
      this.location = newValue;
    }
  },
  async mounted() {
    // console.log(this.scenario)
    // console.log(this.twi_scenario)
    // console.log(this.sudo_scenario)
    // console.log(this.location)
    // const twi_scenario = this.$route.params.scenario.split('-')[0];
    // const sudo_scenario = this.$route.params.scenario.split('-')[1];
    // const state = this.$route.params.state;

    try {
      const twiResponse = await axios.get(`http://127.0.0.1:5000/api_twi_state_city/${this.twi_scenario}/${this.location}`);
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
      const sudoResponse = await axios.get(`http://127.0.0.1:5000/api_sudo_state_city/${this.sudo_scenario}/${this.location}`);
      this.sudo_data = sudoResponse.data.results;
      this.sudo_max = this.sudo_data[0].percentage
      this.sudo_min = this.sudo_data[this.sudo_data.length-1].percentage
    } catch (error) {
      console.error('Failed to fetch Sudo data:', error);
    }

    this.initMap();
    this.createCircles();
  },
  methods: {
    goBack() {
      this.$router.push('/')
    },
    // toggleDropdown1() {
    //   this.twi_scenario = "unemployment"
    //   this.isDropdownOpen1 = !this.isDropdownOpen1;
    // },
    // toggleDropdown2() {
    //   this.twi_scenario = "agism"
    //   this.isDropdownOpen2 = !this.isDropdownOpen2;
    // },
    // toggleDropdown3() {
    //   this.twi_scenario = "sexism"
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
      // }
    },
    createCircles() {
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
                this.showInfoWindow2(circle2, sudo.city, sudo.count, sudo.total, sudo.percentage);
            });
            circle2.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles2.push(circle2);
        });
    },
    showInfoWindow1(circle, name, count, total, percentage) {
      const infoWindow1 = new google.maps.InfoWindow({
        content: `Name: ${name}<br>Count: ${count}<br>Total: ${total}<br>Percentage: ${percentage.toFixed(3)}%`,
        // disableAutoPan: true
      });
      infoWindow1.setPosition(circle.getCenter());
      infoWindow1.open(this.map1);
      this.infoWindow = infoWindow1;
    },
    showInfoWindow2(circle, name, count, total, percentage) {
      const infoWindow2 = new google.maps.InfoWindow({
        content: `Name: ${name}<br>Count: ${count}<br>Ageing population: ${total}<br>Ageing population percentage: ${percentage.toFixed(3)}%`,
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
    },
    confirm() {
        const new_twi_scenario = this.twi_scenario;
        const new_sudo_scenario = this.sudo_scenario;
        const new_state = this.location;

        try {
          const new_twiResponse = axios.get(`http://127.0.0.1:5000/api_twi_state_city/${new_twi_scenario}/${new_state}`);
          this.center = new_twiResponse.data.state;
          this.twi_data = new_twiResponse.data.results;
        } catch (error) {
          console.error('Failed to fetch Twitter data:', error);
        }

        try {
          const new_sudoResponse = axios.get(`http://127.0.0.1:5000/api_sudo_state_city/${new_sudo_scenario}/${new_state}`);
          this.sudo_data = new_sudoResponse.data.results;
        } catch (error) {
          console.error('Failed to fetch Sudo data:', error);
        }

        this.initMap();
        this.createCircles();

        const scenario = this.twi_scenario + '-' + this.sudo_scenario
        // const new_state = this.location
        // this.$router.push({ name: 'results', params: { scenario: scenario, state: new_state } })
        this.$router.push({ path: `/${scenario}/${new_state}`, query: { scenario, new_state } })



        // this.$router.push({ path: `/${scenario}/${new_state}` });
        // window.location.reload();
    }
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
.scenario {
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
}

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

</style>