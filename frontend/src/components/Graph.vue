<template>
  <div>
    <img :src="imageSrc" alt="Image" style="width: 1000px; height: 400px;">
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      imageBase64: ''  // Placeholder for the base64-encoded image data
    };
  },
  mounted() {
    // Make the HTTP request to retrieve the image data
    axios.get('http://127.0.0.1:5000/api_histogram/victoria/agism/agism')
      .then(response => {
        this.imageBase64 = response.data.image_base64;
      })
      .catch(error => {
        console.error('Error retrieving image data:', error);
      });
  },
  computed: {
    imageSrc() {
      return `data:image/png;base64,${this.imageBase64}`;
    }
  }
};
</script>

