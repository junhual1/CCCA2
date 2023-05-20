<template>
  <div>
    <div class="MChart">
      <canvas id="MChart" style="width: 400px; height: 300px;"></canvas>
    </div>
    <div class="MChart2">
      <canvas id="MChart2" style="width: 400px; height: 300px;"></canvas>
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
      twiEmployment: null,
      twiAgism: null,
      twiSexism: null,
    }
  },
  mounted() {
    Promise.all([
      axios.get('http://172.26.133.154:5984/api_mastodon/unemployment'),
      axios.get('http://172.26.133.154:5984/api_mastodon/agism'),
      axios.get('http://172.26.133.154:5984/api_mastodon/sexism'),

      axios.get('http://172.26.133.154:5984/api_twi_total/unemployment'),
      axios.get('http://172.26.133.154:5984/api_twi_total/agism'),
      axios.get('http://172.26.133.154:5984/api_twi_total/sexism')
    ])
      .then(responses => {
        this.mastodonEmployment = responses[0].data.unemployment[0];
        this.mastodonAgism = responses[1].data.agism[0];
        this.mastodonSexism = responses[2].data.sexism[0];
        this.twiEmployment = responses[3].data.summary;
        this.twiAgism = responses[4].data.summary;
        this.twiSexism = responses[5].data.summary;
        this.createBarChart();
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    createBarChart() {
      const ctx = document.getElementById('MChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Employment', 'Agism', 'Sexism'],
          datasets: [
            {
              label: 'Percentage',
              data: [this.mastodonEmployment.percentage, this.mastodonAgism.percentage, this.mastodonSexism.percentage],
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
              text: 'Percentage of mentions of each topic on Mastodon',
            },
          },
        },
      });

      const ctx2 = document.getElementById('MChart2').getContext('2d');
      new Chart(ctx2, {
        type: 'bar',
        data: {
          labels: ['Employment', 'Agism', 'Sexism'],
          datasets: [
            {
              label: 'Percentage',
              data: [this.twiEmployment.percentage, this.twiAgism.percentage, this.twiSexism.percentage],
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
              text: 'Percentage of mentions of each topic on Twitter',
            },
          },
        },
      });
    }

  }
}
</script>

<style>
.MChart {
    position: relative;
    /* display: block; */
    width: 100%;
    height: 100%;
    left: 10%;
    z-index: 1;
}

.MChart2 {
    position: relative;
    /* display: block; */
    width: 100%;
    height: 100%;
    left: 10%;
    z-index: 1;
}
</style>