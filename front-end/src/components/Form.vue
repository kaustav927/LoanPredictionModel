<template>
  <div>
    <b-form @submit="onSubmit" method="post" @reset="onReset" v-if="show">
      <div class="container">
        <b-row>
          <b-col>
            <b-form-group
              id="input-group-2"
              label="Income:"
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                v-model="form.income"
                placeholder="Enter Income"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group
              id="input-group-2"
              label="Credit Score:"
              label-for="input-2"
            >
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
          </b-col>
        </b-row>

        <b-form-group id="input-group-2" label="Loan Term:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.loanTerm"
            placeholder="Enter Loan Term"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Interest Rate:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.interestRate"
            placeholder="Enter Interest Rate"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Credit Incidents:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.creditIncidents"
            placeholder="Enter Credit Incidents"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Home Value:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.homeValue"
            placeholder="Enter Home Value"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Loan Amount:"
          label-for="input-2"
        >
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

        <b-form-group
          id="input-group-2"
          label="Longditude:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.long"
            placeholder="Enter Longditude"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Median Home Value:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.medianHomeValue"
            placeholder="Enter Median Home Value"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Median Household Income:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.medianHouseholdIncome"
            placeholder="Enter Median Household Income"
            required
          ></b-form-input>
        </b-form-group>

        <b-button pill type="submit" size="lg" variant="outline-primary"
          >Submit</b-button
        >
        <b-button pill type="reset" variant="danger">Reset</b-button>
      </div>
    </b-form>

    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import { BootstrapVue } from "bootstrap-vue";
Vue.use(BootstrapVue);
Vue.use(VueAxios, axios);

export default {
  name: "Form",
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
    };
  },

  methods: {
    onSubmit(e) {
      e.preventDefault();
      let currentObj = this;
      //var result = [[]];
      //var formData =JSON.stringify(this.form)
      const headers = {
        "Content-Type": "application/json",
        "Accept-Charset": "UTF-8",
        "Access-Control-Allow-Origin": "true",
      };

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
        .then(function (response) {
          // Handle success
          console.log(response.text);
          currentObj.output = response.data;

          alert(JSON.stringify(this.form));
        })
        .catch(function (error) {
          currentObj.output = error;
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