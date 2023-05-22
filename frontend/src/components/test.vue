<template>
  <div>
    <div class="graph">
      <Table :keyword="keyword" :showTable="showTable" ></Table>
      <MChart :keyword="keyword" :showChart="showChart" ></MChart>
    </div>

    <div id="map" style="height: 82%"></div>
    <div class="scenario">
      <button :style="{ backgroundColor: buttonColor1 }" @click="onKeywordClick('employment')">Employment</button>
      <button :style="{ backgroundColor: buttonColor2 }" @click="onKeywordClick('agism')">Agism</button>
      <button :style="{ backgroundColor: buttonColor3 }" @click="onKeywordClick('sexism')">Sexism</button>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import Table from '../components/Table.vue'
import MChart from '../components/mastodonChart.vue'

export default {
  components: {
    Table, MChart
  },
  data() {
    return {
      map: null,
      circles: [],
      keyword: null,
      buttonColor1: 'white',
      buttonColor2: 'white',
      buttonColor3: 'white',

      current_scenario: null,
      keywordTweets: null,
      showTable: false,
      showChart: true,

      twi_nsw: null,
      twi_vic: null,
      twi_qld: null,
      twi_sa: null,
      twi_wa: null,
      twi_tas: null,
      twi_act: null,
      twi_nt: null,
      twi_ot: null,

      employment: [],
      agism: [],
      sexism: []
    };
  },
  mounted() {
    this.initMap();
    Promise.all([
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/newsouthwales'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/victoria'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/queensland'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/southaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/westernaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/tasmania'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/australiancapitalterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/northernterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/unemployment/offshoreterritories'),

      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/newsouthwales'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/victoria'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/queensland'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/southaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/westernaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/tasmania'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/australiancapitalterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/northernterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/agism/offshoreterritories'),

      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/newsouthwales'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/victoria'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/queensland'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/southaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/westernaustralia'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/tasmania'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/australiancapitalterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/northernterritory'),
      axios.get('http://172.26.133.154:5000/api_twi_state_total/sexism/offshoreterritories')
    ])
      .then(responses => {
        this.twi_nsw = { ...responses[0].data['new south wales'], ...responses[0].data['summary']};
        this.employment.push(this.twi_nsw)
        this.twi_vic = { ...responses[1].data['victoria'], ...responses[1].data['summary']};
        this.employment.push(this.twi_vic)
        this.twi_qld = { ...responses[2].data['queensland'], ...responses[2].data['summary']};
        this.employment.push(this.twi_qld)
        this.twi_sa = { ...responses[3].data['south australia'], ...responses[3].data['summary']};
        this.employment.push(this.twi_sa)
        this.twi_wa = { ...responses[4].data['western australia'], ...responses[4].data['summary']};
        this.employment.push(this.twi_wa)
        this.twi_tas = { ...responses[5].data['tasmania'], ...responses[5].data['summary']};
        this.employment.push(this.twi_tas)
        this.twi_act = { ...responses[6].data['australian capital territory'], ...responses[6].data['summary']};
        this.employment.push(this.twi_act)
        this.twi_nt = { ...responses[7].data['northern territory'], ...responses[7].data['summary']};
        this.employment.push(this.twi_nt)
        this.twi_ot = { ...responses[8].data['offshore territories'], ...responses[8].data['summary']};
        this.employment.push(this.twi_ot)

        this.twi_nsw = { ...responses[9].data['new south wales'], ...responses[9].data['summary']};
        this.agism.push(this.twi_nsw)
        this.twi_vic = { ...responses[10].data['victoria'], ...responses[10].data['summary']};
        this.agism.push(this.twi_vic)
        this.twi_qld = { ...responses[11].data['queensland'], ...responses[11].data['summary']};
        this.agism.push(this.twi_qld)
        this.twi_sa = { ...responses[12].data['south australia'], ...responses[12].data['summary']};
        this.agism.push(this.twi_sa)
        this.twi_wa = { ...responses[13].data['western australia'], ...responses[13].data['summary']};
        this.agism.push(this.twi_wa)
        this.twi_tas = { ...responses[14].data['tasmania'], ...responses[14].data['summary']};
        this.agism.push(this.twi_tas)
        this.twi_act = { ...responses[15].data['australian capital territory'], ...responses[15].data['summary']};
        this.agism.push(this.twi_act)
        this.twi_nt = { ...responses[16].data['northern territory'], ...responses[16].data['summary']};
        this.agism.push(this.twi_nt)
        this.twi_ot = { ...responses[17].data['offshore territories'], ...responses[17].data['summary']};
        this.agism.push(this.twi_ot)

        this.twi_nsw = { ...responses[18].data['new south wales'], ...responses[18].data['summary']};
        this.sexism.push(this.twi_nsw)
        this.twi_vic = { ...responses[19].data['victoria'], ...responses[19].data['summary']};
        this.sexism.push(this.twi_vic)
        this.twi_qld = { ...responses[20].data['queensland'], ...responses[20].data['summary']};
        this.sexism.push(this.twi_qld)
        this.twi_sa = { ...responses[21].data['south australia'], ...responses[21].data['summary']};
        this.sexism.push(this.twi_sa)
        this.twi_wa = { ...responses[22].data['western australia'], ...responses[22].data['summary']};
        this.sexism.push(this.twi_wa)
        this.twi_tas = { ...responses[23].data['tasmania'], ...responses[23].data['summary']};
        this.sexism.push(this.twi_tas)
        this.twi_act = { ...responses[24].data['australian capital territory'], ...responses[24].data['summary']};
        this.sexism.push(this.twi_act)
        this.twi_nt = { ...responses[25].data['northern territory'], ...responses[25].data['summary']};
        this.sexism.push(this.twi_nt)
        this.twi_ot = { ...responses[26].data['offshore territories'], ...responses[26].data['summary']};
        this.sexism.push(this.twi_ot)
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    initMap() {
      this.map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -28.2744, lng: 133.7751 },
        zoom: 4.5,
        gestureHandling: "none",
        disableDefaultUI: true
      });
    },
    createCircles() {
      if (this.keyword === 'employment') {
        this.keywordTweets = this.employment
        this.changeButtonColor1();
      } else if (this.keyword === 'agism') {
        this.keywordTweets = this.agism
        this.changeButtonColor2();
      } else if (this.keyword === 'sexism') {
        this.keywordTweets = this.sexism
        this.changeButtonColor3();
      }
      this.keywordTweets.forEach(tweet => {
        const circleOptions = {
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          map: this.map,
          center: new google.maps.LatLng(tweet.lat, tweet.lng),
          radius: Math.sqrt(tweet.percentage) * 5000000 // convert count to meters
        };
        const circle = new google.maps.Circle(circleOptions);
        circle.addListener('mouseover', () => {
          this.showInfoWindow(circle, tweet.count, tweet.percentage, tweet.total);
        });
        circle.addListener('mouseout', () => {
          this.hideInfoWindow();
        });
        this.circles.push(circle);
      });
    },
    showInfoWindow(circle, count, percentage, total) {
      const infoWindow = new google.maps.InfoWindow({
        content: `Count: ${count}<br>Percentage: ${percentage.toFixed(3)}<br>Total: ${total}`,
        disableAutoPan: true
      });
      infoWindow.setPosition(circle.getCenter());
      infoWindow.open(this.map);
      this.infoWindow = infoWindow;
    },
    hideInfoWindow() {
      if (this.infoWindow) {
        this.infoWindow.close();
      }
    },
    onKeywordClick(keyword) {
      this.updateKeyword(keyword)
      
      this.clearButtonColor();
      
      if (this.keyword !== this.current_scenario) {
        this.clearCircles();
        this.showTable = true;
        // this.displayChart()
        this.createCircles();
        this.current_scenario = this.keyword;
      }
      else {
        this.displayTable()
        this.clearCircles();
        this.current_scenario = null
      }

      // this.$emit('toggle-table');

      // this.$emit('variable-updated', this.keyword);
    },
    updateKeyword(keyword) {
      this.keyword = keyword
    },
    displayTable() {
      this.showTable = !this.showTable
    },
    displayChart() {
      this.showChart = !this.showChart
    },
    clearCircles() {
      this.circles.forEach(circle => {
        circle.setMap(null);
      });
      this.circles = [];
    },
    changeButtonColor1() {
      if (this.buttonColor1 === 'white') {
        this.buttonColor1 = 'grey';
        // this.showChart = false
      } else {
        this.buttonColor1 = 'white'
        // this.showChart = true
      }
    },
    changeButtonColor2() {
      if (this.buttonColor2 === 'white') {
        this.buttonColor2 = 'grey';
      } else {
        this.buttonColor2 = 'white'
      }
    },
    changeButtonColor3() {
      if (this.buttonColor3 === 'white') {
        this.buttonColor3 = 'grey';
      } else {
        this.buttonColor3 = 'white'
      }
    },
    clearButtonColor() {
      this.buttonColor1 = 'white'
      this.buttonColor2 = 'white'
      this.buttonColor3 = 'white'
    }
  }
}
</script>

<style>
#map {
    position: absolute;
    width: 100%;
    height: 82%;
    left: 0px;
    bottom: 0px;
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
.graph {
  position: absolute;
  z-index: 2;
  left: 3%;
  bottom: 5%;
}
</style>