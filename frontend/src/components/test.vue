<template>
  <div>
    <!-- <div>
      {{ this.test }}
    </div> -->
    <Table :keyword="keyword" :showTable="showTable"></Table>
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
      showChart: false,

      twi_nsw: null,
      twi_vic: null,
      twi_qld: null,
      twi_sa: null,
      twi_wa: null,
      twi_tas: null,
      twi_act: null,
      twi_nt: null,

      employment: [],
      agism: [],
      sexism: []
    };
  },
  mounted() {
    this.initMap();
    Promise.all([
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/new%20south%20wales'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/victoria'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/queensland'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/south%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/western%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/tasmania'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/australian%20capital%20territory'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/unemployment/northern%20territory'),

      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/new%20south%20wales'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/victoria'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/queensland'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/south%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/western%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/tasmania'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/australian%20capital%20territory'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/agism/northern%20territory'),

      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/new%20south%20wales'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/victoria'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/queensland'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/south%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/western%20australia'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/tasmania'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/australian%20capital%20territory'),
      axios.get('http://127.0.0.1:5000/api_twi_state_total/sexism/northern%20territory')
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

        this.twi_nsw = { ...responses[8].data['new south wales'], ...responses[8].data['summary']};
        this.agism.push(this.twi_nsw)
        this.twi_vic = { ...responses[9].data['victoria'], ...responses[9].data['summary']};
        this.agism.push(this.twi_vic)
        this.twi_qld = { ...responses[10].data['queensland'], ...responses[10].data['summary']};
        this.agism.push(this.twi_qld)
        this.twi_sa = { ...responses[11].data['south australia'], ...responses[11].data['summary']};
        this.agism.push(this.twi_sa)
        this.twi_wa = { ...responses[12].data['western australia'], ...responses[12].data['summary']};
        this.agism.push(this.twi_wa)
        this.twi_tas = { ...responses[13].data['tasmania'], ...responses[13].data['summary']};
        this.agism.push(this.twi_tas)
        this.twi_act = { ...responses[14].data['australian capital territory'], ...responses[14].data['summary']};
        this.agism.push(this.twi_act)
        this.twi_nt = { ...responses[15].data['northern territory'], ...responses[15].data['summary']};
        this.agism.push(this.twi_nt)

        this.twi_nsw = { ...responses[16].data['new south wales'], ...responses[16].data['summary']};
        this.sexism.push(this.twi_nsw)
        this.twi_vic = { ...responses[17].data['victoria'], ...responses[17].data['summary']};
        this.sexism.push(this.twi_vic)
        this.twi_qld = { ...responses[18].data['queensland'], ...responses[18].data['summary']};
        this.sexism.push(this.twi_qld)
        this.twi_sa = { ...responses[19].data['south australia'], ...responses[19].data['summary']};
        this.sexism.push(this.twi_sa)
        this.twi_wa = { ...responses[20].data['western australia'], ...responses[20].data['summary']};
        this.sexism.push(this.twi_wa)
        this.twi_tas = { ...responses[21].data['tasmania'], ...responses[21].data['summary']};
        this.sexism.push(this.twi_tas)
        this.twi_act = { ...responses[22].data['australian capital territory'], ...responses[22].data['summary']};
        this.sexism.push(this.twi_act)
        this.twi_nt = { ...responses[23].data['northern territory'], ...responses[23].data['summary']};
        this.sexism.push(this.twi_nt)
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
        this.createCircles();
        this.current_scenario = this.keyword;
      }
      else {
        this.displayTable()
        this.clearCircles();
        this.current_scenario = null
      }

      this.$emit('toggle-table');

      // this.$emit('variable-updated', this.keyword);
    },
    updateKeyword(keyword) {
      this.keyword = keyword
    },
    displayTable() {
      this.showTable = !this.showTable
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
      } else {
        this.buttonColor1 = 'white'
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
</style>