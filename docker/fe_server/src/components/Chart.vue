<template>
  <div id="chart" style="width: 1000px; height: 400px;"></div>
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
      twi_data: null,
      sudo_data: null,
      twi_perc: [],
      sudo_perc: [],
      twi_city: [],
      sudo_city: [],
      twi_max_perc: null,
      sudo_max_perc: null,
      twi_rank: [],
      sudo_rank: [],
      twi_color: [],
      sudo_color: [],
      chart_title: null,
      twi_interval: null,
      sudo_interval: null
    }
  },
  async mounted() {
    const twi_scenario = this.$route.params.scenario.split('-')[0];
    const sudo_scenario = this.$route.params.scenario.split('-')[1];
    const state = this.$route.params.state;

    // console.log(twi_scenario)
    // console.log(sudo_scenario)
    // console.log(state)

    if (twi_scenario === 'unemployment' && sudo_scenario === 'unemployment') {
      this.chart_title = 'Comparison of employment topic engagement and employment rate'
    } else if (twi_scenario === 'unemployment' && sudo_scenario === 'agism') {
      this.chart_title = 'Comparison of employment topic engagement and ageing population percentage'
    } else if (twi_scenario === 'unemployment' && sudo_scenario === 'sexism') {
      this.chart_title = 'Comparison of employment topic engagement and gender ratio'
    } else if (twi_scenario === 'agism' && sudo_scenario === 'agism') {
      this.chart_title = 'Comparison of agesim topic engagement and ageing population percentage'
    } else if (twi_scenario === 'sexism' && sudo_scenario === 'sexism') {
      this.chart_title = 'Camparison of sexism topic engagement and gender ratio'
    } 

    try {
      const sudoResponse = await axios.get(`${API_PREFIX}/api_sudo_state_city/${sudo_scenario}/${state}`);
      this.sudo_data = sudoResponse.data.results;
      this.sudo_data.forEach(sudo => {
        this.sudo_city.push(sudo.city)
        this.sudo_perc.push(sudo.percentage.toFixed(3))
        this.sudo_rank.push(sudo.rank)
      })
      this.sudo_rank.forEach(rank => {
        if (rank === 0) {
          this.sudo_color.push('#c0c0c0')
        } else if (rank === 1) {
          this.sudo_color.push('#c0c0c0')
        } else if (rank === -1) {
          this.sudo_color.push('#c0c0c0')
        }
      })
      this.sudo_max_perc = Math.max(...this.sudo_perc) * 1.15
      this.sudo_interval = this.sudo_max_perc / 10
    } catch (error) {
      console.error('Failed to fetch Sudo data:', error);
    }

    try {
      const twiResponse = await axios.get(`${API_PREFIX}/api_twi_state_city/${twi_scenario}/${state}`);
      this.twi_data = twiResponse.data.results;
      this.sudo_data.forEach(sudo =>{
        this.twi_data.forEach(twi => {
          if (twi.city === sudo.city){
            this.twi_perc.push(twi.percentage.toFixed(5))
            this.twi_rank.push(twi.rank)
          }
        })
      })
      // this.twi_data.forEach(twi => {
      //   this.twi_city.push(twi.city)
      //   this.twi_perc.push(twi.percentage.toFixed(5))
      //   this.twi_rank.push(twi.rank)
      // })

      this.twi_rank.forEach(rank => {
        if ((state !== 'australiancapitalterritory') && (state !== 'northernterritory') && (state !== 'offshoreterritories')) {
          if (rank === 1) {
            this.twi_color.push('#ff6347')
          } else if (rank === -1) {
            this.twi_color.push('#1e90ff')
          } else {
            this.twi_color.push('#696969')
          }
        } else {
          this.twi_color.push('#696969')
        }
      })
      
      // this.twi_rank.forEach(rank => {
      //   if (rank === 0) {
      //     this.twi_color.push('#696969')
      //   } else if (rank === 1) {
      //     this.twi_color.push('#ff6347')
      //   } else if (rank === -1) {
      //     this.twi_color.push('#1e90ff')
      //   }
      // })
      // console.log(this.twi_color)
      this.twi_max_perc = Math.max(...this.twi_perc) * 1.15
      this.twi_interval = this.twi_max_perc / 10
    } catch (error) {
      console.error('Failed to fetch Twitter data:', error);
    }



    this.initChart();
  },
  methods: {
    initChart() {
      const twiMax = Math.min(this.twi_interval.toFixed(3) * 10, Number.MAX_VALUE);
      const twuInterval = Number(this.twi_interval.toFixed(3));
      const sudoMax = Math.min(this.sudo_interval.toFixed(3) * 10, Number.MAX_VALUE);
      const sudoInterval = Number(this.sudo_interval.toFixed(3));

      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      const option = {
        title: {
          text: this.chart_title,
          textStyle: {
            fontSize: 16,
            fontWeight: 'bold',
            // color: 'blue'
          },
          left: 'center',
          top: 'top'
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
        xAxis: [
          {
            type: 'category',
            data: this.sudo_city,
            axisPointer: {
              type: 'shadow'
            },
            axisLabel: {
              rotate: -45
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'Twitter',
            min: 0,
            max: twiMax,
            interval: twuInterval,
            axisLabel: {
              formatter: '{value} %'
            }
          },
          {
            type: 'value',
            name: 'Sudo',
            min: 0,
            max: sudoMax,
            interval: sudoInterval,
            axisLabel: {
              formatter: '{value} %'
            }
          }
          
        ],
        series: [
          {
            name: 'Twitter',
            type: 'bar',
            itemStyle: {
              color: (params) => {
                return this.twi_color[params.dataIndex];
              }
            },
            tooltip: {
              formatter: '{c} %'
            },
            data: this.twi_perc
          },
          {
            name: 'Sudo',
            type: 'bar',
            yAxisIndex: 1,
            itemStyle: {
              color: (params) => {
                return this.sudo_color[params.dataIndex];
              }
            },
            tooltip: {
              formatter: '{c} %'
            },
            data: this.sudo_perc
          }
        ]
      };
        // Your chart options here
      
      myChart.setOption(option);
    }
  }
}
</script>
