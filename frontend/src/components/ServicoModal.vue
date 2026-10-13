<script setup>
import { reactive, watch } from "vue";

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

const emit = defineEmits(["close", "submit"]);

const form = reactive({
  status: "",
  feedback: "",
});

watch(
  () => props.solicitacao,
  (solicitacao) => {
    form.status = solicitacao?.status ?? "";
    form.feedback = solicitacao?.feedback ?? "";
  },
  { immediate: true },
);

function fecharModal() {
  emit("close");
}

function onBackdropClick(e) {
  if (e.target === e.currentTarget) {
    fecharModal();
  }
}

function salvarAlteracoes() {
  emit("submit", { ...form });
  fecharModal();
}
</script>

<template>
  <div
    v-if="open && solicitacao"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4"
    @click="onBackdropClick"
  >
    <div
      class="rounded-xl shadow-2xl w-full max-w-xl overflow-hidden flex flex-col mx-auto"
    >
      <div class="bg-[#1D242F] text-white flex justify-between px-4 py-1">
        <div class="flex items-center">
          <div class="bg-[#E19047] p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold">Jacto</p>
          <p class="text-[#E19047] font-bold">Flow</p>
        </div>
        <span class="py-3 cursor-pointer" @click="fecharModal"
          ><i class="fa-solid fa-circle-xmark" style="color: #ffffff"></i
        ></span>
      </div>
      <div class="shadow p-6 bg-white">
        <h1 class="font-bold text-xl py-4">
          {{ solicitacao.id }}| {{ solicitacao.tipoServico }}
        </h1>

        <div class="flex justify-between">
          <div class="font-semibold text-xs">
            <h5 class="text-slate-500">SOLICITANTE</h5>
            <p class="text-sm">{{ solicitacao.solicitante }}</p>
          </div>
          <div class="font-semibold text-xs">
            <h5 class="text-slate-500">ABERTURA</h5>
            <p class="text-sm">{{ solicitacao.abertura }}</p>
          </div>
          <div class="font-semibold text-xs">
            <h5 class="text-slate-500">ATENDIDO</h5>
            <p class="text-sm">{{ solicitacao.atendido }}</p>
          </div>
        </div>

        <form class="m-3" @submit.prevent="salvarAlteracoes">
          <div class="flex flex-col">
            <h3 class="font-bold py-3">Interativo atalho técnico</h3>
            <label class="font-semibold">Status</label>
            <select
              v-model="form.status"
              name="status"
              class="border border-slate-300 rounded-sm p-1 my-2 focus:outline-none focus:ring-2 focus:ring-[#423adf]"
            >
              <option value="">Selecione..</option>
              <option value="andamento">Em Andamento</option>
              <option value="aguardando">Aguardando</option>
              <option value="concluida">Concluída</option>
            </select>
          </div>

          <div class="flex flex-col">
            <label class="font-semibold">Feedback</label>
            <textarea
              v-model="form.feedback"
              name="feedback"
              id="feedback"
              class="border border-slate-300 rounded-sm p-1 my-2"
              rows="5"
              cols="50"
            ></textarea>
          </div>

          <div>
            <button
              type="submit"
              class="bg-[#423adf] text-white font-bold text-center w-full rounded-lg py-1 my-2 cursor-pointer"
            >
              Salvar Alterações
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
