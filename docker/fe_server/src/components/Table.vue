<template>
    <div>
      <div>
        <table v-if="keyword === 'employment' && showTable">
          <caption>Comparison Between Mastodon and Twitter About Employment Topic</caption>
          <thead>
          <tr>
              <th></th>
              <th>Mentioned</th>
              <th>Total</th>
              <th>Percentage (%)</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>Mastodon</td>
              <td>{{ this.masEmploymentMentioned }}</td>
              <td>{{ this.masEmploymentTotal }}</td>
              <td>{{ this.masEmploymentPercentage * 100 }}</td>
          </tr>
          <tr>
              <td>Twitter</td>
              <td>{{ this.twiEmploymentCount }}</td>
              <td>{{ this.twiEmploymentTotal }}</td>
              <td>{{ this.twiEmploymentPercentage * 100 }}</td>
          </tr>
          </tbody>
        </table>

        <table v-else-if="keyword === 'agism' && showTable">
          <caption>Comparison Between Mastodon and Twitter About Agism Topic</caption>
          <thead>
          <tr>
              <th></th>
              <th>Mentioned</th>
              <th>Total</th>
              <th>Percentage (%)</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>Mastodon</td>
              <td>{{ this.masAgismMentioned }}</td>
              <td>{{ this.masAgismTotal }}</td>
              <td>{{ this.masAgismPercentage * 100 }}</td>
          </tr>
          <tr>
              <td>Twitter</td>
              <td>{{ this.twiAgismCount }}</td>
              <td>{{ this.twiAgismTotal }}</td>
              <td>{{ this.twiAgismPercentage * 100 }}</td>
          </tr>
          </tbody>
        </table>

        <table v-else-if="keyword === 'sexism' && showTable">
          <caption>Comparison Between Mastodon and Twitter About Sexism Topic</caption>
          <thead>
          <tr>
              <th></th>
              <th>Mentioned</th>
              <th>Total</th>
              <th>Percentage (%)</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>Mastodon</td>
              <td>{{ this.masSexismMentioned }}</td>
              <td>{{ this.masSexismTotal }}</td>
              <td>{{ this.masSexismPercentage * 100 }}</td>
          </tr>
          <tr>
              <td>Twitter</td>
              <td>{{ this.twiSexismCount }}</td>
              <td>{{ this.twiSexismTotal }}</td>
              <td>{{ this.twiSexismPercentage * 100 }}</td>
          </tr>
          </tbody>
        </table>
      </div>

        
    </div>

</template>

<script>
import axios from 'axios';
import { API_PREFIX } from '../req_config.js';

export default {
    props: 
        ['keyword', 'showTable']
    ,
  data() {
    return {
        showEmployment: false,
        showAgism: false,
        showSexism: false,

        masEmploymentMentioned: null,
        masEmploymentTotal: null,
        masEmploymentPercentage: null,
        masAgismMentioned: null,
        masAgismTotal: null,
        masAgismPercentage: null,
        masSexismMentioned: null,
        masSexismTotal: null,
        masSexismPercentage: null,

        twiEmploymentCount: null,
        twiEmploymentTotal: null,
        twiEmploymentPercentage: null,
        twiAgismCount: null,
        twiAgismTotal: null,
        twiAgismPercentage: null,
        twiSexismCount: null,
        twiSexismTotal: null,
        twiSexismPercentage: null
    }
  },
  mounted() {

    Promise.all([
      axios.get(API_PREFIX + '/api_mastodon/unemployment'),
      axios.get(API_PREFIX + '/api_mastodon/agism'),
      axios.get(API_PREFIX + '/api_mastodon/sexism'),

      axios.get(API_PREFIX + '/api_twi_total/unemployment'),
      axios.get(API_PREFIX + '/api_twi_total/agism'),
      axios.get(API_PREFIX + '/api_twi_total/sexism')
    ])
      .then(responses => {
        this.masEmploymentMentioned = responses[0].data.mentioned;
        this.masEmploymentTotal = responses[0].data.total;
        this.masEmploymentPercentage = responses[0].data.percentage.toFixed(3);
        this.masAgismMentioned = responses[1].data.mentioned;
        this.masAgismTotal = responses[1].data.total;
        this.masAgismPercentage = responses[1].data.percentage.toFixed(3);
        this.masSexismMentioned = responses[2].data.mentioned;
        this.masSexismTotal = responses[2].data.total;
        this.masSexismPercentage = responses[2].data.percentage.toFixed(3);

        this.twiEmploymentCount = responses[3].data.summary.count;
        this.twiEmploymentTotal = responses[3].data.summary.total;
        this.twiEmploymentPercentage = responses[3].data.summary.percentage.toFixed(3);
        this.twiAgismCount = responses[4].data.summary.count;
        this.twiAgismTotal = responses[4].data.summary.total;
        this.twiAgismPercentage = responses[4].data.summary.percentage.toFixed(3);
        this.twiSexismCount = responses[5].data.summary.count;
        this.twiSexismTotal = responses[5].data.summary.total;
        this.twiSexismPercentage = responses[5].data.summary.percentage.toFixed(3);
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>

<style>
  table {
    position: relative;
    width: 95%;
    height: 100%;
    z-index: 1;
    border-collapse: collapse;
    margin-bottom: 150px;
  }
  th {
    border: 1px solid black;
    padding: 8px;
  }
  td {
    border: 1px solid black;
    padding: 8px;
  }
  caption {
    font-size: 1em;
    font-weight: bold;
  }
</style>