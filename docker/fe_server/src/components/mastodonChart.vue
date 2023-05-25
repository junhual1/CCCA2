<template>

  <div id="Mchart" style="width: 430px; height: 300px;"></div>
  
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';
import 'echarts/lib/chart/bar';
import 'echarts/lib/chart/line';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/toolbox';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/title';
import { API_PREFIX } from '../req_config.js';

export default {
  data() {
    return {
      mastodonEmployment: null,
      mastodonAgism: null,
      mastodonSexism: null,
      twiEmployment: null,
      twiAgism: null,
      twiSexism: null,
      mastodon_data: [],
      twi_data: [],
      mastodon_max: null,
      twi_max: null
    }
  },
  async mounted() {
    try {
      const masEmployResponse = await axios.get(API_PREFIX + '/api_mastodon/unemployment');
      this.mastodonEmployment = masEmployResponse.data.percentage * 100;
      this.mastodon_data.push(this.mastodonEmployment.toFixed(3))
    } catch (error) {
      console.error('Failed to fetch Mastodon data:', error);
    }
    try {
      const masAgismResponse = await axios.get(API_PREFIX + '/api_mastodon/agism');
      this.mastodonAgism = masAgismResponse.data.percentage * 100;
      this.mastodon_data.push(this.mastodonAgism.toFixed(3))
    } catch (error) {
      console.error('Failed to fetch Mastodon data:', error);
    }
    try {
      const masSexismResponse = await axios.get(API_PREFIX + '/api_mastodon/sexism');
      this.mastodonSexism = masSexismResponse.data.percentage * 100;
      this.mastodon_data.push(this.mastodonSexism.toFixed(3))
      this.mastodon_max = Math.ceil(Math.max(...this.mastodon_data) * 10) / 10
    } catch (error) {
      console.error('Failed to fetch Mastodon data:', error);
    }
    try {
      const twiEmployResponse = await axios.get(API_PREFIX + '/api_twi_total/unemployment');
      this.twiEmployment = twiEmployResponse.data.summary.percentage * 100;
      this.twi_data.push(this.twiEmployment.toFixed(3))
    } catch (error) {
      console.error('Failed to fetch Twitter data:', error);
    }
    try {
      const twiAgismResponse = await axios.get(API_PREFIX + '/api_twi_total/agism');
      this.twiAgism = twiAgismResponse.data.summary.percentage * 100;
      this.twi_data.push(this.twiAgism.toFixed(3))
    } catch (error) {
      console.error('Failed to fetch Twitter data:', error);
    }
    try {
      const twiSexismResponse = await axios.get(API_PREFIX + '/api_twi_total/sexism');
      this.twiSexism = twiSexismResponse.data.summary.percentage * 100;
      this.twi_data.push(this.twiSexism.toFixed(3))
      this.twi_max = Math.ceil(Math.max(...this.twi_data) * 10) / 10
    } catch (error) {
      console.error('Failed to fetch Twitter data:', error);
    }

    this.initChart();
  },
  methods: {
      initChart() {

      const chartDom = document.getElementById('Mchart');
      const myChart = echarts.init(chartDom);
      const option = {
        title: {
          text: 'Comparasion of Topic Discussion Rate Between Twitter and Mastodon',
          textStyle: {
            fontSize: 12,
            fontWeight: 'bold',
          },
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        legend: {
          data: ['Twitter', 'Mastodon'],
          right: 40, 
          top: 30
        },
        xAxis: [
          {
            type: 'category',
            data: ['Employment', 'Agism', 'Sexism'],
            axisPointer: {
              type: 'shadow'
            },
            axisLabel: {
              rotate: 0
            }
          }
        ],
        yAxis: {
          type: 'value',
          name: 'Discussion Rate',
          min: 0,
          max: this.mastodon_max, 
          interval: 0.1,
          axisLabel: {
            formatter: '{value} %'
          }
        },
        series: [
          {
            name: 'Twitter',
            type: 'bar',
            itemStyle: {
              color: 'rgba(0, 0, 0, 0.6)'
            },
            tooltip: {
              formatter: '{c} %'
            },
            data: this.twi_data 
          },
          {
            name: 'Mastodon',
            type: 'bar',
            itemStyle: {
              color: 'rgba(0, 0, 0, 0.3)'
            },
            tooltip: {
              formatter: '{c} %'
            },
            data: this.mastodon_data
          }
        ]
      };
      
      myChart.setOption(option);
    }
  }
}
</script>
