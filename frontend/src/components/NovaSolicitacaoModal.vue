<script setup>
import { reactive } from "vue";

const props = defineProps({
  open: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["close", "submit"]);

const form = reactive({
  tipoServico: "",
  prazo: "",
  descricao: "",
  file: null,
});

function resetForm() {
  form.tipoServico = "";
  form.prazo = "";
  form.descricao = "";
  form.file = null;
}

function fecharModal() {
  emit("close");
}

function onBackdropClick(e) {
  if (e.target === e.currentTarget) {
    fecharModal();
  }
}

function onFileChange(e) {
  form.file = e.target.files[0] ?? null;
}

function enviarForm() {
  emit("submit", { ...form });
  resetForm();
  fecharModal();
}
</script>

<template>
  <div
    v-if="open"
    class="fixed inset-0 z-50 flex items-center justify-center bg-overlay/45 backdrop-blur-sm p-4"
    @click="onBackdropClick"
  >
    <div
      class="rounded-xl shadow-2xl w-full max-w-xl overflow-hidden flex flex-col mx-auto"
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
        <h1 class="font-bold text-xl py-4">+ Nova Solicitação</h1>

        <form @submit.prevent="enviarForm">
          <div class="flex flex-col">
            <label class="font-semibold">Tipo de Serviço</label>
            <select
              v-model="form.tipoServico"
              name="tipoServico"
              class="border border-slate-300 rounded-sm p-1 my-2"
            >
              <option value="">Selecione..</option>
              <option value="molde-injecao">Molde de Injeção</option>
            </select>
          </div>

          <div class="flex flex-col">
            <label class="font-semibold">Prazo Desejado</label>
            <input
              v-model="form.prazo"
              type="date"
              name="prazo"
              id="prazo"
              class="border border-slate-300 rounded-sm p-1 my-2"
            />
          </div>

          <div class="flex flex-col">
            <label class="font-semibold">Descrição</label>
            <textarea
              v-model="form.descricao"
              name="descricao"
              id="descricao"
              class="border border-slate-300 rounded-sm p-1 my-2"
              rows="5"
              cols="50"
              placeholder="Descrição"
            ></textarea>
          </div>

          <div class="flex flex-col">
            <label class="font-semibold">Links dos Arquivos Técnicos</label>
            <input
              type="file"
              name="file"
              id="file"
              class="border border-slate-300 rounded-sm p-1 my-2"
              @change="onFileChange"
            />
          </div>

          <div>
            <button
              type="submit"
              class="bg-brand-mint hover:bg-brand-turquoise text-white font-bold text-center w-full rounded-lg py-1 my-2 cursor-pointer"
            >
              REGISTRAR
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
