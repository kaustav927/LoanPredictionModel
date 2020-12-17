<template>
  <b-modal :content-class="`modal-result-${resultText.toLowerCase()}`" id="modal-result" hide-footer>
    <template #modal-title>
      Result
    </template>
    <div class="d-block text-center">
      <h3>The Results is: </h3>
      <p>
          {{ resultText }}
      </p>
    </div>
    <b-button class="mt-3" block @click="$bvModal.hide('modal-result')">Close</b-button>
  </b-modal>
</template>
<script>
export default {
    name: "ResultModal",
    
    props: {
        result: {
            type: [Number],
            required: true
        }
    },

    computed: {
        resultText() {
            return this.result === 0 ? "No" : "Yes";
        }
    }
}
</script>