<template>
  <div>
    <b-form @submit="onSubmit" method="post" @reset="onReset" v-if="show">

    <div class="container">

   
      <b-form-group id="input-group-2" label="Income:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.income"
          placeholder="Enter Income"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Credit Score:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.creditScore"
          placeholder="Enter Credit Score"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Debt:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.debt"
          placeholder="Enter Debt"
          required
        ></b-form-input>
      </b-form-group>
      
       <b-form-group id="input-group-2" label="Loan Term:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.loanTerm"
          placeholder="Enter Loan Term"
          required
        ></b-form-input>
      </b-form-group>
      
       <b-form-group id="input-group-2" label="Interest Rate:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.interestRate"
          placeholder="Enter Interest Rate"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Credit Incidents:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.creditIncidents"
          placeholder="Enter Credit Incidents"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Home Value:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.homeValue"
          placeholder="Enter Home Value"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Loan Amount:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.loanAmount"
          placeholder="Enter Loan Amount"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Latitude:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.lat"
          placeholder="Enter Latitude"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-2" label="Longditude:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.long"
          placeholder="Enter Longditude"
          required
        ></b-form-input>
      </b-form-group>

        <b-form-group id="input-group-2" label="Median Home Value:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.medianHomeValue"
          placeholder="Enter Median Home Value"
          required
        ></b-form-input>
      </b-form-group>

        <b-form-group id="input-group-2" label="Median Household Income:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.medianHouseholdIncome"
          placeholder="Enter Median Household Income"
          required
        ></b-form-input>
      </b-form-group>

     
      


      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </div>
    </b-form>


    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>



  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
  export default {
    name: "Form",
    data() {
      return {
        form: {
          income: null,
          creditScore: null,
          debt: null,
          loanTerm: null,
          interestRate: null,
          creditIncidents: null,
          homeValue: null,
          loanAmount: null,
          lat: null,
          long: null,
          medianHomeValue: null,
          medianHouseholdIncome: null,
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        //this.axios.post("http://localhost:8081/post/",this.posts)
        //.then((result)=>{
        //    console.warn(result)
        //})
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.income = null
        this.form.creditScore = null
        this.form.debt = null
        this.form.loanAmount = null
        this.form.interestRate = null
        this.form.creditIncidents = null
        this.form.homeValue = null
        this.form.loanAmount = null
        this.form.lat = null
        this.form.long = null
        this.form.medianHomeValue= null
        this.form.medianHouseholdIncome = null
        
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>