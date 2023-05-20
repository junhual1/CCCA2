<template>
  <div>
    <div class="chart">
      <canvas id="myChart" style="width: 400px; height: 300px;"></canvas>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      mastodonEmployment: null,
      mastodonAgism: null,
      mastodonSexism: null,
    }
  },
  mounted() {
    Promise.all([
      axios.get('http://127.0.0.1:5000/api_mastodon/unemployment'),
      axios.get('http://127.0.0.1:5000/api_mastodon/agism'),
      axios.get('http://127.0.0.1:5000/api_mastodon/sexism')
    ])
      .then(responses => {
        this.mastodonEmployment = responses[0].data.unemployment[0];
        this.mastodonAgism = responses[1].data.agism[0];
        this.mastodonSexism = responses[2].data.sexism[0];
        this.createBarChart();
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    createBarChart() {
      if (this.mastodonAgism) {
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Employment', 'Agism', 'Sexism'],
            datasets: [
              {
                label: 'Mentioned',
                data: [this.mastodonEmployment.mentioned, this.mastodonAgism.mentioned, this.mastodonSexism.mentioned],
                backgroundColor: 'rgba(0, 0, 0, 0.4)',
                borderColor: 'rgba(0, 0, 0, 1)',
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
            plugins: {
              title: {
                display: true,
                text: 'Number of mentions of each topic on Mastodon',
              },
            },
          },
        });
      }
    }

  }
}
</script>

<style>
.chart {
    position: absolute;
    width: 100%;
    height: 100%;
    left: 10%;
    z-index: 1;
}
</style>