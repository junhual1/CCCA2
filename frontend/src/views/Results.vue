<template>
  <div>
    <div class="menu">
      <div class="current">      
        <span>Current Scenario: {{ $route.params.scenario }}</span>
        <!-- <span>Current Sudo Scenario: {{ $route.params.sudo_scenario }}</span> -->
        <!-- <span v-else>Current Scenario: {{ scenario }}</span> -->
        <span>Current Location: {{ $route.params.state }}</span>
        <!-- <span v-else>Current Location: {{ location }}</span> -->
      </div>
      <div class="choose">
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
          <button @click="confirm">Confirm</button>
        </div>
      </div>
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
    <!-- <div class="dynamic-chart">
      <Chart />
    </div> -->
    <div class="graph2">
      <Graph />
    </div>

  </div>
</template>

<script>
import axios from 'axios';
// import Chart from '../components/Chart.vue'
import Graph from '../components/Graph.vue'

export default {
  name: 'Result',
  components: { Graph },

  data() {
    return {
        array: null,

        twi_scenario: null,
        sudo_scenario: null,
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
    };
  },
  mounted() {
    const twi_scenario = this.$route.params.scenario.split('-')[0];
    const sudo_scenario = this.$route.params.scenario.split('-')[1];
    const state = this.$route.params.state;


    let twiDataPromise = null;
    let sudoDataPromise = null;

    // if (!this.scenario)
    twiDataPromise = axios.get(`http://172.26.133.154:5000/api_twi_state_city/${twi_scenario}/${state}`)
      .then(response => {
        this.center = response.data.state;
        this.twi_data = response.data.results;
      })
      .catch(error => {
        console.error('Failed to fetch Twitter data:', error);
      });
    // } else {
    //   twiDataPromise = axios.get(`http://172.26.133.154:5000/api_twi_state_city/${this.scenario}/${this.state}`)
    //     .then(response => {
    //       this.center = response.data.state;
    //       this.twi_data = response.data.results;
    //     })
    //     .catch(error => {
    //       console.error('Failed to fetch Twitter data:', error);
    //     });
    // }

    // console.log(twi_scenario)
    // console.log(sudo_scenario)
    // console.log(state)
    // if (!this.scenario) {
    sudoDataPromise = axios.get(`http://172.26.133.154:5000/api_sudo_state_city/${sudo_scenario}/${state}`)
      .then(response => {
        this.sudo_data = response.data.results;
        // this.sudo_data.forEach(sudo => {
        //   console.log(sudo.lat)
        //   console.log(sudo.lng)
        // })
      })
      .catch(error => {
        console.error('Failed to fetch Sudo data:', error);
      });
    // } else {
    //   sudoDataPromise = axios.get(`http://172.26.133.154:5000/api_sudo_state_city/${this.scenario}/${this.state}`)
    //     .then(response => {
    //       this.sudo_data = response.data.results;
    //     })
    //     .catch(error => {
    //       console.error('Failed to fetch Sudo data:', error);
    //     });
    // }

    Promise.all([twiDataPromise, sudoDataPromise])
      .then(() => {
        this.initMap();
        this.createCircles();
      })
      .catch(error => {
        console.error('Failed to fetch data:', error);
      });

  },

  // mounted() {
  //   const scenario = this.$route.params.scenario;
  //   const state = this.$route.params.state
  //   if (!this.scenario) {
  //     const twiDataPromise = axios.get(`http://172.26.133.154:5000/api_twi_state_city/${scenario}/${state}`)
  //       .then(response => {
  //         this.center = response.data.state;
  //         this.twi_data = response.data.results;
  //       })
  //       .catch(error => {
  //         console.error('Failed to fetch Twitter data:', error);
  //       });
  //   } else {
  //     const twiDataPromise = axios.get(`http://172.26.133.154:5000/api_twi_state_city/${this.scenario}/${this.state}`)
  //       .then(response => {
  //         this.center = response.data.state;
  //         this.twi_data = response.data.results;
  //       })
  //       .catch(error => {
  //         console.error('Failed to fetch Twitter data:', error);
  //       });
  //   }
    
  //   // const twiDataPromise = axios.get('http://172.26.133.154:5000/api_twi_state_city/agism/victoria')
      
  //   if (!this.scenario) {
  //     const sudoDataPromise = axios.get(`http://172.26.133.154:5000/api_sudo_state_city/${scenario}/${state}`)
  //     // const sudoDataPromise = axios.get('http://172.26.133.154:5000/api_sudo_state_city/agism/victoria')
  //       .then(response => {
  //         this.sudo_data = response.data.results;
  //       })
  //       .catch(error => {
  //         console.error('Failed to fetch Sudo data:', error);
  //       });
  //   } else {
  //     const sudoDataPromise = axios.get(`http://172.26.133.154:5000/api_sudo_state_city/${this.scenario}/${this.state}`)
  //     // const sudoDataPromise = axios.get('http://172.26.133.154:5000/api_sudo_state_city/agism/victoria')
  //       .then(response => {
  //         this.sudo_data = response.data.results;
  //       })
  //       .catch(error => {
  //         console.error('Failed to fetch Sudo data:', error);
  //       });
  //   }
    
  //   Promise.all([twiDataPromise, sudoDataPromise])
  //     .then(() => {
  //       // console.log('Data fetched successfully');
  //       this.initMap();
  //       this.createCircles();
  //     })
  //     .catch(error => {
  //       console.error('Failed to fetch data:', error);
  //     });
  

    // Promise.all([
    //   axios.get(`http://172.26.133.154:5000/api_twi_state_city/agism/victoria`),
    //   axios.get(`http://172.26.133.154:5000/api_sudo_state_city/agism/victoria`),
    //   // axios.get(`http://172.26.133.154:5000/api_twi_state_city/${this.scenario}/${this.location}`),

    // ])
    //   .then(responses => {
    //     this.center = responses[0].data.state
    //     this.twi_data = responses[0].data.results
    //     this.sudo_data = responses[1].data.results
    //     // this.array = Object.values(this.twi_data)

    //     console.log(this.center)
    //     console.log(this.twi_data === null)
    //     // this.twi_data.forEach(tweet => {
    //     //   console.log(tweet)
    //     // })
    //     // console.log(typeof this.twi_data)

    //   })
    //   .catch(error => {
    //     console.error(error);
    //   });
    // console.log('1')
    // this.initMap()
    // this.createCircles()
  // },
  methods: {
    toggleDropdown1() {
      this.twi_scenario = "unemployment"
      this.isDropdownOpen1 = !this.isDropdownOpen1;
    },
    toggleDropdown2() {
      this.twi_scenario = "agism"
      this.isDropdownOpen2 = !this.isDropdownOpen2;
    },
    toggleDropdown3() {
      this.twi_scenario = "sexism"
      this.isDropdownOpen3 = !this.isDropdownOpen3;
    },
    initMap() {
      // const state = this.$route.params.state
      // if (state === 'victoria') {
      this.map1 = new google.maps.Map(document.getElementById('map1'), {
          // center: { lat: -25.2744, lng: 133.7751 },
          center: this.center,
          zoom: 7,
          gestureHandling: "none",
          disableDefaultUI: true
      })
      this.map2 = new google.maps.Map(document.getElementById('map2'), {
          // center: { lat: -25.2744, lng: 133.7751 },
          center: this.center,
          zoom: 7,
          gestureHandling: "none",
          disableDefaultUI: true
      })
      // }
    },
    createCircles() {
        // const scenario = this.$route.params.scenario;
        // const keywordTweets = null;
        // if (scenario === 'unemployment') {
        //     this.keywordTweets = this.tweets.unemployment;
        // } else if (scenario === 'agism') {
        //     this.keywordTweets = this.tweets.agism;
        // } else if (scenario === 'sexism') {
        //     this.keywordTweets = this.tweets.sexism;
        // }
        // if (scenario === 'unemployment') {
        //     this.keywordSudo = this.sudo.unemployment;
        // } else if (scenario === 'agism') {
        //     this.keywordSudo = this.sudo.agism;
        // } else if (scenario === 'sexism') {
        //     this.keywordSudo = this.sudo.sexism;
        // }
        // this.keywordTweets = this.twi_data
        // const keywordTweets = this.tweets[scenario];
        this.twi_data.forEach(tweet => {
            const circleOptions = {
                strokeColor: '#FF0000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
                map: this.map1,
                center: new google.maps.LatLng(tweet.lat, tweet.lng),
                radius: tweet.percentage * 50000 // convert count to meters
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
                strokeColor: '#FF0000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
                map: this.map2,
                center: new google.maps.LatLng(sudo.lat, sudo.lng),
                radius: sudo.percentage * 10000 // convert count to meters
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
        const scenario = this.twi_scenario + '-' + this.sudo_scenario
        const new_state = this.location
        console.log(scenario)
        console.log(new_state)
        this.$router.push({ name: 'results', params: { scenario: scenario, state: new_state } })
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
  left: 38%;
  z-index: 1;
}
.graph2 {
  position: absolute;
  top: 50%;
  left: 25%;

}

</style>