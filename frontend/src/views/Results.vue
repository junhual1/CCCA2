<template>
  <div>
    <div class="menu">
      <div class="current">      
        <span v-if="!this.scenario">Current Scenario: {{ $route.params.scenario }}</span>
        <span v-else>Current Scenario: {{ scenario }}</span>
        <span v-if="!this.location">Current Location: {{ $route.params.state }}</span>
        <span v-else>Current Location: {{ location }}</span>
      </div>
      <div class="choose">
        <span class="title">Change Main Topics</span>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown1">
            1. Employment discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen1 }">
            <li>
              <button>vs offical employment rate</button>
            </li>
            <li>
              <button>vs offical aging percentage</button>
            </li>
            <li>
              <button>vs offical gender ratio</button>
            </li>
          </ul>
        </div>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown2">
            2. Agism discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen2 }">
            <li>
              <button>vs offical employment rate</button>
            </li>
            <li>
              <button>vs offical aging percentage</button>
            </li>
            <li>
              <button>vs offical gender ratio</button>
            </li>
          </ul>
        </div>
        <div class="dropdown">
          <button class="dropdown-toggle" @click="toggleDropdown3">
            3. Sexism discussion rate on Twitter
          </button>
          <ul class="dropdown-list" :class="{ 'is-open': isDropdownOpen3 }">
            <li>
              <button>vs offical employment rate</button>
            </li>
            <li>
              <button>vs offical aging percentage</button>
            </li>
            <li>
              <button>vs offical gender ratio</button>
            </li>
          </ul>
        </div>
        <div class="location">
          <span>Change the location: </span>
          <select v-model="location">
            <option value="NSW">NSW</option>
            <option value="VIC">VIC</option>
            <option value="QlD">QLD</option>
            <option value="SA">SA</option>
            <option value="WA">WA</option>
            <option value="ACT">ACT</option>
            <option value="NT">NT</option>
            <option value="TAS">TAS</option>
            <option value="Other">Other</option>
          </select>
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
    <div class="dynamic-chart">
      <Chart />
    </div>

  </div>
</template>

<script>
import Chart from '../components/Chart.vue'

export default {
  name: 'Result',
  components: { Chart },

  data() {
    return {

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
        tweets: {
            unemployment: [
                { lat: -37.8136, lng: 144.9631, count: 25, percentage: 0.125 },
                { lat: -33.8688, lng: 151.2093, count: 75, percentage: 0.375 },
                { lat: -27.4698, lng: 153.0251, count: 100, percentage: 0.5 }
            ],
            agism: [
                {name: 'Bacchus Marsh', lat: -37.6379445774, lng: 144.4546154062, total: 241,count: 0, percentage: 0 },
                {name: 'Bairnsdale', lat: -37.8291637497, lng: 147.6139838657, total: 389,count: 1, percentage: 0.2570694087403599 },
                {name: 'Ballarat', lat: -37.5539742558, lng: 143.8367094122, total: 12699,count: 9, percentage: 0.07087172218284904 },
                {name: 'Bendigo', lat: -36.7458615926, lng: 144.2889256877, total: 3436,count: 7, percentage: 0.2037252619324796 },
                {name: 'Colac', lat: -38.3588349683, lng: 143.5785465831, total: 340,count: 2, percentage: 0.5882352941176471 },
                {name: 'Echuca - Moama', lat: -36.1133830072, lng: 144.7738363123, total: 922,count: 11, percentage: 1.193058568329718 },
                {name: 'Geelong', lat: -38.0923903539, lng: 144.3916701496, total: 18145,count: 43, percentage: 0.23697988426563793 },
                {name: 'Gisborne - Macedon', lat: -37.4659211929, lng: 144.5865661907, total: 375,count: 1, percentage: 0.26666666666666666 },
                {name: 'Horsham', lat: -36.7317621101, lng: 142.2144937682, total: 353,count: 2, percentage: 0.56657223796034 },
                {name: 'Melbourne', lat: -37.8283723017, lng: 145.1490390294, total: 368849,count: 852, percentage: 0.2309888328286101 },
                {name: 'Melton', lat: -37.6750038142, lng: 144.5698450445, total: 1974,count: 3, percentage: 0.1519756838905775 },
                {name: 'Mildura - Wentworth', lat: -34.1570351773, lng: 142.0723447447, total: 874,count: 1, percentage: 0.11441647597254005 },
                {name: 'Moe - Newborough', lat: -38.1966133627, lng: 146.2959155886, total: 128,count: 1, percentage: 0.78125 },
                {name: 'Not in any Significant Urban Area (Vic.)', lat: -36.8071613754, lng: 144.2665797455, total: 23513,count: 62, percentage: 0.2636839195338749 },
                {name: 'Portland', lat: -38.3402529101, lng: 141.5841230557, total: 191,count: 0, percentage: 0 },
                {name: 'Sale', lat: -38.1046583718, lng: 147.0562625015, total: 514,count: 1, percentage: 0.19455252918287938 },
                {name: 'Shepparton - Mooroopna', lat: -36.402272672, lng: 145.4104356114, total: 1074,count: 3, percentage: 0.27932960893854747 },
                {name: 'Swan Hill', lat: -35.3621875475, lng: 143.5117836979, total: 1065,count: 2, percentage: 0.18779342723004694 },
                {name: 'Traralgon - Morwell', lat: -38.1992130926, lng: 146.5279232456, total: 2500,count: 3, percentage: 0.12 },
                {name: 'Wangaratta', lat: -36.3589038754, lng: 146.3096517668, total: 593,count: 2, percentage: 0.33726812816188867 },
                {name: 'Warragul - Drouin', lat: -38.1762242401, lng: 145.873434429, total: 994,count: 3, percentage: 0.30181086519114686 },
                {name: 'Warrnambool', lat: -38.3744226411, lng: 142.547431729, total: 1882,count: 4, percentage: 0.21253985122210414 }
            ],
            sexism: [
            { lat: -37.8136, lng: 144.9631, count: 25, percentage: 0.125 },
            { lat: -33.8688, lng: 151.2093, count: 75, percentage: 0.375 },
            { lat: -27.4698, lng: 153.0251, count: 100, percentage: 0.5 }
            ]
        },
        sudo: {
            agism: [
                {name: 'Bacchus Marsh', lat: -37.6379445774, lng: 144.4546154062, total: 2938, percentage: 18.5269264724 },
                {name: 'Bairnsdale', lat: -37.8291637497, lng: 147.6139838657, total: 3337, percentage: 28.354150735 },
                {name: 'Ballarat', lat: -37.5539742558, lng: 143.8367094122, total: 16297, percentage: 20.5438180718 },
                {name: 'Bendigo', lat: -36.7458615926, lng: 144.2889256877, total: 15899, percentage: 21.1724128747 },
                {name: 'Colac', lat: -38.3588349683, lng: 143.5785465831, total: 2486, percentage: 25.6950904393 },
                {name: 'Echuca - Moama', lat: -36.1133830072, lng: 144.7738363123, total: 4766, percentage: 28.6728432198 },
                {name: 'Geelong', lat: -38.0923903539, lng: 144.3916701496, total: 42112, percentage: 21.4091438274 },
                {name: 'Gisborne - Macedon', lat: -37.4659211929, lng: 144.5865661907, total: 2927, percentage: 19.2098182057 },
                {name: 'Horsham', lat: -36.7317621101, lng: 142.2144937682, total: 3182, percentage: 24.7819314642 },
                {name: 'Melbourne', lat: -37.8283723017, lng: 145.1490390294, total: 591138, percentage: 16.8119427367 },
                {name: 'Melton', lat: -37.6750038142, lng: 144.5698450445, total: 6316, percentage: 13.9306116147 },
                {name: 'Mildura - Wentworth', lat: -34.1570351773, lng: 142.0723447447, total: 9646, percentage: 23.6560721993 },
                {name: 'Moe - Newborough', lat: -38.1966133627, lng: 146.2959155886, total: 3410, percentage: 25.3305600951 },
                {name: 'Not in any Significant Urban Area (Vic.)', lat: -36.8071613754, lng: 144.2665797455, total: 144577, percentage: 26.1024911443 },
                {name: 'Portland', lat: -38.3402529101, lng: 141.5841230557, total: 2074, percentage: 23.8857537717 },
                {name: 'Sale', lat: -38.1046583718, lng: 147.0562625015, total: 2618, percentage: 22.5553545274 },
                {name: 'Shepparton - Mooroopna', lat: -36.402272672, lng: 145.4104356114, total: 8206, percentage: 20.9700500869 },
                {name: 'Swan Hill', lat: -35.3621875475, lng: 143.5117836979, total: 2138, percentage: 24.1636528029 },
                {name: 'Traralgon - Morwell', lat: -38.1992130926, lng: 146.5279232456, total: 7272, percentage: 22.3740077534 },
                {name: 'Wangaratta', lat: -36.3589038754, lng: 146.3096517668, total: 4238, percentage: 28.0142781597 },
                {name: 'Warragul - Drouin', lat: -38.1762242401, lng: 145.873434429, total: 6564, percentage: 24.0995704373 },
                {name: 'Warrnambool', lat: -38.3744226411, lng: 142.547431729, total: 6089, percentage: 22.3605449671 }
            ]
        },
        // current_scenario: null
        center: {
            VIC: { lat: -36.8500942662, lng: 144.3042883399 },
        }
    };
  },
  mounted() {
    this.initMap()
    this.createCircles()
  },
  methods: {
    toggleDropdown1() {
      this.scenario = "Employment"
      this.isDropdownOpen1 = !this.isDropdownOpen1;
    },
    toggleDropdown2() {
      this.scenario = "Agism"
      this.isDropdownOpen2 = !this.isDropdownOpen2;
    },
    toggleDropdown3() {
      this.scenario = "Sexism"
      this.isDropdownOpen3 = !this.isDropdownOpen3;
    },
    initMap() {
      const state = this.$route.params.state
      if (state === 'VIC') {
        this.map1 = new google.maps.Map(document.getElementById('map1'), {
            // center: { lat: -25.2744, lng: 133.7751 },
            center: this.center.VIC,
            zoom: 6,
            gestureHandling: "none",
            disableDefaultUI: true
        })
        this.map2 = new google.maps.Map(document.getElementById('map2'), {
            // center: { lat: -25.2744, lng: 133.7751 },
            center: this.center.VIC,
            zoom: 6,
            gestureHandling: "none",
            disableDefaultUI: true
        })
      }
    },
    createCircles() {
        const scenario = this.$route.params.scenario;
        // const keywordTweets = null;
        if (scenario === 'Unemployment') {
            this.keywordTweets = this.tweets.unemployment;
        } else if (scenario === 'Agism') {
            this.keywordTweets = this.tweets.agism;
        } else if (scenario === 'Sexism') {
            this.keywordTweets = this.tweets.sexism;
        }
        if (scenario === 'Unemployment') {
            this.keywordSudo = this.sudo.unemployment;
        } else if (scenario === 'Agism') {
            this.keywordSudo = this.sudo.agism;
        } else if (scenario === 'Sexism') {
            this.keywordSudo = this.sudo.sexism;
        }
        // const keywordTweets = this.tweets[scenario];
        this.keywordTweets.forEach(tweet => {
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
                this.showInfoWindow1(circle1, tweet.name, tweet.count, tweet.total, tweet.percentage);
            });
            circle1.addListener('mouseout', () => {
                this.hideInfoWindow();
            });
            this.circles1.push(circle1);
        });
        this.keywordSudo.forEach(sudo => {
            const circleOptions = {
                strokeColor: '#FF0000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
                map: this.map2,
                center: new google.maps.LatLng(sudo.lat, sudo.lng),
                radius: (sudo.percentage-10)**3.7 // convert count to meters
            };
            const circle2 = new google.maps.Circle(circleOptions);
            circle2.addListener('mouseover', () => {
                this.showInfoWindow2(circle2, sudo.name, sudo.count, sudo.total, sudo.percentage);
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

</style>