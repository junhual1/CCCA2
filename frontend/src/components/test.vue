<template>
  <div>
    <div id="map" style="height: 82%"></div>
    <div class="scenario">
      <button @click="onKeywordClick('unemployment')">Unemployment</button>
      <button @click="onKeywordClick('agism')">Agism</button>
      <button @click="onKeywordClick('sexism')">Sexism</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      map: null,
      circles: [],
      keyword: null,
      tweets: {
        unemployment: [
          { lat: -37.8136, lng: 144.9631, count: 100, percentage: 0.5 },
          { lat: -33.8688, lng: 151.2093, count: 200, percentage: 1.0 },
          { lat: -27.4698, lng: 153.0251, count: 50, percentage: 0.25 }
        ],
        agism: [
          { lat: -37.8136, lng: 144.9631, count: 50, percentage: 0.25 },
          { lat: -33.8688, lng: 151.2093, count: 150, percentage: 0.75 },
          { lat: -27.4698, lng: 153.0251, count: 75, percentage: 0.375 }
        ],
        sexism: [
          { lat: -37.8136, lng: 144.9631, count: 25, percentage: 0.125 },
          { lat: -33.8688, lng: 151.2093, count: 75, percentage: 0.375 },
          { lat: -27.4698, lng: 153.0251, count: 100, percentage: 0.5 }
        ]
      },
      current_scenario: null
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      this.map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -25.2744, lng: 133.7751 },
        zoom: 4.5,
        gestureHandling: "none"
      });
    },
    createCircles() {
      const keywordTweets = this.tweets[this.keyword];
      keywordTweets.forEach(tweet => {
        const circleOptions = {
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          map: this.map,
          center: new google.maps.LatLng(tweet.lat, tweet.lng),
          radius: tweet.count * 1000 // convert count to meters
        };
        const circle = new google.maps.Circle(circleOptions);
        circle.addListener('mouseover', () => {
          this.showInfoWindow(circle, tweet.count, tweet.percentage);
        });
        circle.addListener('mouseout', () => {
          this.hideInfoWindow();
        });
        this.circles.push(circle);
      });
    },
    showInfoWindow(circle, count, percentage) {
      const infoWindow = new google.maps.InfoWindow({
        content: `Count: ${count}<br>Percentage: ${percentage}`
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
      this.keyword = keyword;
      
      if (this.keyword !== this.current_scenario) {
        this.clearCircles();
        this.createCircles();
        this.current_scenario = this.keyword;
      }
      else {
        this.clearCircles();
        this.current_scenario = null
      }
    },
    clearCircles() {
      this.circles.forEach(circle => {
        circle.setMap(null);
      });
      this.circles = [];
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