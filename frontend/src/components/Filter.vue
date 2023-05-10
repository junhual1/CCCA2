<template>
  <div id="filter">
    <div>
        <h1>Filter</h1>
    </div>
    <div class="filterSelect">
        <span class="filterScenario">Scenario: </span>
        <select v-model="select1">
            <option value="scenario1">scenario1</option>
            <option value="scenario2">scenario2</option>
            <option value="scenario3">scenario3</option>
        </select>
    </div>
    <div class="feature">
        <div class="feature1">
            <span>Feature 1: </span>
            <select v-model="select2">
                <option value="feature1">feature1</option>
                <option value="feature2">feature2</option>
                <option value="feature3">feature3</option>
            </select>
        </div>
        <div class="feature2">
            <span>Feature 2: </span>
            <select v-model="select3">
                <option value="feature1">feature1</option>
                <option value="feature2">feature2</option>
                <option value="feature3">feature3</option>
            </select>
        </div>
    </div>
    <div class="submit">
        <button @click="search">Search</button>
    </div>
    <!-- <button class="close">X</button> -->
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
        // search() {
        //     const query = {
        //         select1: this.select1,
        //         select2: this.select2,
        //         select3: this.select3
        //     }
        //     this.$router.push({ name: 'results', query: query })
        // }
    }
}
</script>

<style>
  #filter {
    position: absolute;
    width: 70%;
    height: 50%;
    border-radius: 12px;
    background: #f5f5f5;
    color: white;
    padding: 10px 0;
    margin: 40px auto;
    z-index: 3;
    left: 15%;
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
    display: inline-block;
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
    width: 500px;
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
    top: 15%;
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
    width: 200px;
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
    top: 40%;
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