<template>
  <b-modal :content-class="`modal-result-${modalClass}`" id="modal-result" hide-footer>
    <template #modal-title>
      <p class="modalText mb-0">LPM</p>
    </template>
    <div class="d-block text-center">
      <div class="d-flex flex-row justify-content-center">
        <i style="font-size:70px" class="fa" :class="iconClass" ></i>
      </div>
      <p class="modalText">
          {{ resultText }}
      </p>
    </div>

    <b-button class="mt-3" variant="info" block @click="$bvModal.hide('modal-result')">Close</b-button>
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
        },

        iconClass() {
          return this.result === 0 ? "fa-times-circle no-icon" : "fa-check-circle yes-icon";
        }
    }
}
</script>