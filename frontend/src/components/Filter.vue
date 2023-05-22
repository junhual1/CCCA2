<template>
  <div id="filter">
    <div>
        <h1>Filter</h1>
    </div>
    <div class="filterSelect">
      <div class="scenario1">
        <span class="filterScenario">Scenario: </span>
        <select v-model="select1">
            <option value="unemployment">Employment discussion rate on Twitter</option>
            <option value="agism">Agism discussion rate on Twitter</option>
            <option value="sexism">Sexism discussion rate on Twitter</option>
        </select>
      </div>

      <div class="scenario2">
        <span class="filterScenario2">VS</span>
        <select v-model="select2" :disabled="this.select1 === null">
            <option v-if="this.select1 === 'unemployment'" value="unemployment">Official employment rate</option>
            <option v-if="this.select1 === 'unemployment' || this.select1 === 'agism'" value="agism">Official Aging Rate</option>
            <option v-if="this.select1 === 'unemployment' || this.select1 === 'sexism'" value="sexism">Official gender ratio</option>
            <!-- <option v-if="this.select1 === 'unemployment'" value="agism-sexism">Agism and Sexism discussion rate on Twitter</option> -->
            <!-- <option v-if="this.select1 === 'agism'" value="agism-sexism">Employment and Sexism discussion rate on Twitter</option> -->
            <!-- <option v-if="this.select1 === 'sexism'" value="agism-sexism">Employment and Agism discussion rate on Twitter</option> -->
        </select>
      </div>
    </div>
        
    <div class="state">
      <span class="filterScenario">State: </span>
      <select v-model="select3">
          <option value="newsouthwales">New South Wales</option>
          <option value="victoria">Victoria</option>
          <option value="queensland">Queensland</option>
          <option value="southaustralia">South Australia</option>
          <option value="westernaustralia">Western Australia</option>
          <option value="tasmania">Tasmania</option>
          <option value="australiancapitalterritory">Australian Capital Territory</option>
          <option value="northernterritory">Northern Territory</option>
          <option value="offshoreterritories">Offshore Territories</option>
      </select>
    </div>
    
    <!-- <div class="summary">
      <p>Click "Search" to see </p>
    </div> -->
    <div class="submit">
        <button @click="search">Search</button>
    </div>
  </div>
  
  
</template>

<script>
export default {
    data() {
        return {
            select1: null,
            select2: null,
            select3: null
        }
    },
    methods: {
        search() {
            const scenario = this.select1 + '-' + this.select2
            const state = this.select3
            this.$router.push({ name: 'results', params: { scenario: scenario, state: state } })
        }
    }
}
</script>

<style>
  #filter {
    position: absolute;
    width: 64%;
    height: 40%;
    border-radius: 12px;
    background: #f5f5f5;
    color: white;
    padding: 10px 0;
    margin: 20px auto;
    z-index: 3;
    left: 18%;
    top: 20%;
  }  
  #filter h1 {
    font-family: arial;
    font-size: 24px;
    color: #000000;
    text-align: center;
    margin: 10px auto;
  }
  .filterSelect {
    /* display: inline-block; */
    position: relative;
    padding: 10px 10px;
    border-radius: 12px;
    z-index: 3;
  }
  .filterSelect select:hover {
    cursor: pointer;
  }
  .filterScenario {
    display: inline-block;
    position: relative;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    color: #000000;
    padding: 5px 0px;
    margin-right: 5px;
  }
  .filterScenario2 {
    display: inline-block;
    position: relative;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    color: #000000;
    padding: 5px 0px;
    margin-right: 25px;
    left: 0%;
  }
  .filterSelect select {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px 5px;
    gap: 4px;
    width: 80%;
    height: 40px;
    background: #FFFFFF;
    border: 1px solid #D9D9D9;
    box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.043);
    border-radius: 8px;
    font-size: 1em;
    font-family: arial;
  }
  .state {
    position: relative;
    top: 15%;
    right: 2%;
  }
  .state select {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px 5px;
    gap: 4px;
    /* width: 80%; */
    height: 40px;
    background: #FFFFFF;
    border: 1px solid #D9D9D9;
    box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.043);
    border-radius: 8px;
    font-size: 1em;
    font-family: arial;
  }
  .scenario1 {
    display: inline-block;
    width: 43%;
    left: 0%;
  }
  .scenario2 {
    display: inline-block;
    width: 50%;
    right: 0%;
  }
  .feature {
    position: relative;
    color: #000000;
    /* top: 10%; */
    padding: 10px 10px;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
  }
  .feature select {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px 5px;
    gap: 4px;
    width: 50%;
    height: 40px;
    background: #FFFFFF;
    border: 1px solid #D9D9D9;
    box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.043);
    border-radius: 8px;
    font-size: 1em;
    font-family: arial;
  }
  .feature select:hover {
    cursor: pointer;
  }
  .feature1 {
    display: inline-block;
    position: relative;
    padding: 10px 10px;
    border-radius: 12px;
    z-index: 3;
  }
  .feature2 {
    display: inline-block;
    position: relative;
    padding: 10px 10px;
    border-radius: 12px;
    z-index: 3;
  }
  .submit {
    position: relative;
    top: 35%;
  }
  .submit button {
    border: none;
    color: white;
    background: crimson;
    font-size: 1em;
    font-family: arial;
    font-weight: bold;
    width: 80px;
    height: 40px;
    border-radius: 8px;
  }
  .submit button:hover {
    background: rgb(178, 16, 48);
    cursor: pointer;
  }
  .close {
    position: absolute;
    top: 15px;
    right: 15px;
  }
</style>