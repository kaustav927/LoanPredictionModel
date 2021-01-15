<template>
  <div>
    <b-row class="justify-content-center">
      <b-col cols="8">
        <div class="card p-4">
          <b-form id="lpm-form" @submit="onSubmit" method="post" @reset="onReset" v-if="show">
            <b-row>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  class="inputLables"
                  label="Income"
                  label-for="input-2"
                >
                  <b-form-input
                    id="input-2"
          
                    v-model="form.income"
                    placeholder="Enter Income"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  class="inputLables"
                  label="Credit Score"
                  label-for="input-2"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.creditScore"
                    placeholder="Enter Credit Score"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group id="input-group-2"   class="inputLables" label="Debt" label-for="input-2">
                  <b-form-input
                    id="input-2"
                  
                    v-model="form.debt"
                    placeholder="Enter Debt"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12" lg="4">
                <b-form-group id="input-group-2" class="inputLables" label="Loan Term" label-for="input-2">
                  <b-form-input
                    id="input-2"
                    v-model="form.loanTerm"
                    placeholder="Enter Loan Term"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Interest Rate"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.interestRate"
                    placeholder="Enter Interest Rate"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Credit Incidents"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.creditIncidents"
                    placeholder="Enter Credit Incidents"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Home Value"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.homeValue"
                    placeholder="Enter Home Value"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Loan Amount"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.loanAmount"
                    placeholder="Enter Loan Amount"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group id="input-group-2" class="inputLables" label="Latitude" label-for="input-2">
                  <b-form-input
                    id="input-2"
                    v-model="form.lat"
                    placeholder="Enter Latitude"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Longitude"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.long"
                    placeholder="Enter Longitude"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Median Home Value"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.medianHomeValue"
                    placeholder="Enter Median Home Value"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="12" lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Median Household Income"
                  label-for="input-2"
                  class="inputLables"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.medianHouseholdIncome"
                    placeholder="Enter Median Household Income"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
          </b-form>
        </div>
      </b-col>
    </b-row>

    <b-row class="mt-4 justify-content-center">
      <b-col cols="2">
        <b-button :disabled="!isValid" form="lpm-form" class="w-100" squared type="submit" size="lg" variant="info">
          <div v-if="loading" class="loader"></div>
          <span v-else>
            Submit
          </span>
        </b-button>
      </b-col>
    </b-row>
    

    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card> -->
    <result-modal :result="result"></result-modal>
  </div>
</template>

<script>
import ResultModal from "./ResultModal";
import Vue from "vue";
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";

import axios from "axios";
import VueAxios from "vue-axios";
import { BootstrapVue } from "bootstrap-vue";
Vue.use(BootstrapVue);
Vue.use(VueAxios, axios);

export default {
  name: "Form",

  components: { ResultModal },

  mixins: [validationMixin],

  validations: {
    form: {
      income: { required },
      creditScore: { required },
      debt: { required },
      loanTerm: { required },
      interestRate: { required },
      creditIncidents: { required },
      homeValue: { required },
      loanAmount: { required },
      lat: { required },
      long: { required },
      medianHomeValue: { required },
      medianHouseholdIncome: { required }
    }
  },

  data() {
    return {
      form: {
        income: "894604",
        creditScore: "792",
        debt: "134190.6",
        loanTerm: "420",
        interestRate: "0.039",
        creditIncidents: "0",
        homeValue: "136080",
        loanAmount: "27216",
        lat: "35.25064",
        long: "-91.73625",
        medianHomeValue: "48600",
        medianHouseholdIncome: "30060",
      },
      show: true,
      result: 0,
      loading: false
    };
  },

  computed: {
    isValid() {
      return !this.$v.$invalid;
    }
  },

  methods: {
    onSubmit(e) {
      e.preventDefault();
      let currentObj = this;
      this.loading = true;
      //var result = [[]];
      //var formData =JSON.stringify(this.form)
      const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "true",
      };
       console.log("before axios")

      axios
        .post(
          "http://127.0.0.1:5000/predict/",
          {
            income: this.form.income,
            creditScore: this.form.creditScore,
            debt: this.form.debt,
            loanTerm: this.form.loanTerm,
            interestRate: this.form.interestRate,
            creditIncidents: this.form.creditIncidents,
            homeValue: this.form.homeValue,
            loanAmount: this.form.loanAmount,
            lat: this.form.lat,
            long: this.form.long,
            medianHomeValue: this.form.medianHomeValue,
            medianHouseholdIncome: this.form.medianHouseholdIncome,
          },
          { headers }
        )
       
        .then(response => {
          console.log(response)
          const {status} = response.data
          console.log(status)
          //console.log(status)
          this.result = parseInt(status);
          this.loading = false;
           this.$nextTick(() => { 
             this.$bvModal.show('modal-result')
           })
        })
        .catch(function (error) {
          currentObj.output = error;
          console.log(error);
          this.loading = false;
        });
    },

    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.income = null;
      this.form.creditScore = null;
      this.form.debt = null;
      this.form.loanAmount = null;
      this.form.interestRate = null;
      this.form.creditIncidents = null;
      this.form.homeValue = null;
      this.form.loanAmount = null;
      this.form.lat = null;
      this.form.long = null;
      this.form.medianHomeValue = null;
      this.form.medianHouseholdIncome = null;

      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>