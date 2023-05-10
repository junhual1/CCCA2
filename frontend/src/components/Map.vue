<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'Map',
  data() {
    return {
        map: null
    }
  },
  mounted() {
    this.initMap()
  },
  methods: {
    initMap() {
        this.map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -25.2744, lng: 133.7751 },
        zoom: 4.5,
      })
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
</style>
