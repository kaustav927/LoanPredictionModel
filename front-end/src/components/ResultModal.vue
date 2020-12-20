<template>
  <b-modal :content-class="`modal-result-${modalClass}`" id="modal-result" hide-footer>
    <template #modal-title>
      <p class="modalText">LPM</p>
    </template>
    <div class="d-block text-center">
      <p class="modalText">
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
            return this.result === 0 ? "It is unlikely that this application would be accepted by the lender." : "Congratulations! There's a good chance this application would be accepted by the lender.";
        },

        
        modalClass(){
          return this.result=== 0 ? "no" : "yes";
        }
    }
}
</script>