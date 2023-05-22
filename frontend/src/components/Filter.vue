<template>
  <div id="filter">
    <div>
        <h1>Filter</h1>
    </div>
    <div class="filterSelect">
        <span class="filterScenario">Scenario: </span>
        <select v-model="select1">
            <option value="unemployment-unemployment">Employment</option>
            <option value="agism-agism">Agism</option>
            <option value="sexism-sexism">Sexism</option>
        </select>
    </div>
    <div class="feature">
        <span>State: </span>
        <select v-model="select2">
            <option value="newsouthwales">NSW</option>
            <option value="victoria">VIC</option>
            <option value="queensland">QLD</option>
            <option value="southaustralia">SA</option>
            <option value="westernaustralia">WA</option>
            <option value="tasmania">TAS</option>
            <option value="australiancapitalterritory">ACT</option>
            <option value="northernterritory">NT</option>
            <option value="offshoreterritories">OT</option>
        </select>
    </div>
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
            select2: null
        }
    },
    methods: {
        search() {
            const scenario = this.select1
            const state = this.select2
            this.$router.push({ name: 'results', params: { scenario: scenario, state: state } })
        }
    }
}
</script>

<style>
  #filter {
    position: absolute;
    width: 30%;
    height: 30%;
    border-radius: 12px;
    background: #f5f5f5;
    color: white;
    padding: 10px 0;
    margin: 20px auto;
    z-index: 3;
    left: 35%;
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
  }
  .filterSelect select {
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
    top: 10%;
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