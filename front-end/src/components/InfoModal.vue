<template>
  <b-modal id="modal-info" hide-footer>
    <template #modal-title>
      <p class="modalText mb-0">Help</p>
    </template>
    <div class="d-block text-center">
      <p class="modalText mb-0">
          help text
      </p>    
    </div>
    <b-button class="mt-3" variant="info" block @click="$bvModal.hide('modal-info')">Close</b-button>
  </b-modal>
</template>
<script>

export default {
    name: "InfoModal"
}
</script>