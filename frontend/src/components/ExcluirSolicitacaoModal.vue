<script setup>
const props = defineProps({
  open: {
    type: Boolean,
    default: false,
  },
  solicitacao: {
    type: Object,
    default: null,
  },
});

const emit = defineEmits(["close", "confirm"]);

function fecharModal() {
  emit("close");
}

function onBackdropClick(e) {
  if (e.target === e.currentTarget) {
    fecharModal();
  }
}

function confirmarExclusao() {
  emit("confirm");
  fecharModal();
}
</script>

<template>
  <div
    v-if="open && solicitacao"
    class="fixed inset-0 z-50 flex items-center justify-center bg-overlay/45 backdrop-blur-sm p-4"
    @click="onBackdropClick"
  >
    <div
      class="rounded-xl shadow-2xl w-full max-w-md overflow-hidden flex flex-col mx-auto"
    >
      <div class="bg-surface-dark text-white flex justify-between px-4 py-1">
        <div class="flex items-center">
          <div class="bg-brand-mint p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold">Jacto</p>
          <p class="text-brand-turquoise font-bold">Flow</p>
        </div>
        <span class="py-3 cursor-pointer" @click="fecharModal"
          ><i class="fa-solid fa-circle-xmark" style="color: #ffffff"></i
        ></span>
      </div>

      <div class="shadow p-6 bg-white">
        <h2 class="font-bold text-xl">Excluir solicitação?</h2>
        <p class="text-sm text-ink-secondary mt-1">
          Você está prestes a excluir a solicitação abaixo.
        </p>

        <div class="bg-surface-subtle rounded-lg p-3 my-4">
          <p class="font-bold">
            {{ solicitacao.id }} | {{ solicitacao.tipoServico }}
          </p>
          <h5 class="text-ink-secondary text-xs font-semibold mt-2">
            SOLICITANTE
          </h5>
          <p class="text-sm">{{ solicitacao.solicitante }}</p>
        </div>

        <div class="bg-red-50 border border-red-200 rounded-lg p-3 flex gap-2">
          <i class="fa-solid fa-triangle-exclamation text-red-600 mt-0.5"></i>
          <div>
            <p class="font-bold text-sm text-red-700">
              Esta exclusão é permanente.
            </p>
            <p class="text-sm text-red-700">
              A solicitação será removida e não poderá ser recuperada.
            </p>
          </div>
        </div>

        <div class="flex flex-col sm:flex-row gap-2 mt-6">
          <button
            type="button"
            class="w-full border border-slate-300 bg-white hover:bg-surface-subtle text-surface-dark font-bold rounded-lg py-2 cursor-pointer"
            @click="fecharModal"
          >
            Cancelar
          </button>
          <button
            type="button"
            class="w-full bg-red-600 hover:bg-red-700 text-white font-bold rounded-lg py-2 cursor-pointer flex items-center justify-center gap-2"
            @click="confirmarExclusao"
          >
            <i class="fa-solid fa-trash-can"></i>
            Excluir solicitação
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
