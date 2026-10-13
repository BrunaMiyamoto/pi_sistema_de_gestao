<script setup>
import { computed, reactive, ref } from "vue";
import AppHeader from "../components/AppHeader.vue";
import StatusCards from "../components/StatusCards.vue";
import NovaSolicitacaoModal from "../components/NovaSolicitacaoModal.vue";
import ServicoModal from "../components/ServicoModal.vue";

const stats = reactive({
  pendentes: 1,
  emAnalise: 1,
  emAtendimento: 1,
  concluidas: 1,
});

const solicitacoes = reactive([
  {
    id: "#001",
    data: "18/08/2026",
    solicitante: "Engenharia - Jacto Agrícola",
    tipoServico: "Molde de Injeção",
    prazo: "18/08/2026",
    status: "andamento",
    abertura: "18/08/2026",
    atendido: "18/08/2026",
    feedback: "",
  },
  {
    id: "#002",
    data: "18/08/2026",
    solicitante: "Engenharia - Jacto Agrícola",
    tipoServico: "Molde de Injeção",
    prazo: "18/08/2026",
    status: "andamento",
    abertura: "18/08/2026",
    atendido: "18/08/2026",
    feedback: "",
  },
  {
    id: "#003",
    data: "18/08/2026",
    solicitante: "Engenharia - Jacto Agrícola",
    tipoServico: "Molde de Injeção",
    prazo: "18/08/2026",
    status: "concluida",
    abertura: "18/08/2026",
    atendido: "18/08/2026",
    feedback: "",
  },
  {
    id: "#004",
    data: "18/08/2026",
    solicitante: "Engenharia - Jacto Agrícola",
    tipoServico: "Molde de Injeção",
    prazo: "18/08/2026",
    status: "concluida",
    abertura: "18/08/2026",
    atendido: "18/08/2026",
    feedback: "",
  },
]);

const statusLabel = {
  andamento: "Em Andamento",
  aguardando: "Aguardando",
  concluida: "Concluída",
};

const statusClasses = {
  andamento: "bg-[#a7affc] text-[#423adf]",
  aguardando: "bg-[#fcd9a7] text-[#F29949]",
  concluida: "bg-[#9afac3] text-[#328C59]",
};

const pesquisa = ref("");

const solicitacoesFiltradas = computed(() => {
  const termo = pesquisa.value.trim().toLowerCase();
  if (!termo) return solicitacoes;

  return solicitacoes.filter((solicitacao) =>
    [solicitacao.id, solicitacao.solicitante, solicitacao.tipoServico]
      .join(" ")
      .toLowerCase()
      .includes(termo),
  );
});

const novaSolicitacaoAberta = ref(false);
const servicoModalAberto = ref(false);
const solicitacaoSelecionada = ref(null);

function abrirNovaSolicitacao() {
  novaSolicitacaoAberta.value = true;
}

function fecharNovaSolicitacao() {
  novaSolicitacaoAberta.value = false;
}

function registrarSolicitacao(dadosForm) {
  const proximoId = solicitacoes.length + 1;
  solicitacoes.push({
    id: `#${String(proximoId).padStart(3, "0")}`,
    data: new Date().toLocaleDateString("pt-BR"),
    solicitante: "Engenharia - Jacto Agrícola",
    tipoServico: dadosForm.tipoServico,
    prazo: dadosForm.prazo,
    status: "andamento",
    abertura: new Date().toLocaleDateString("pt-BR"),
    atendido: "-",
    feedback: "",
  });
}

function abrirServico(solicitacao) {
  solicitacaoSelecionada.value = solicitacao;
  servicoModalAberto.value = true;
}

function fecharServico() {
  servicoModalAberto.value = false;
}

function salvarServico(dadosForm) {
  if (!solicitacaoSelecionada.value) return;
  solicitacaoSelecionada.value.status = dadosForm.status;
  solicitacaoSelecionada.value.feedback = dadosForm.feedback;
}

function excluirSolicitacao(solicitacao) {
  if (!confirm("Deseja excluir o registro?")) return;
  const index = solicitacoes.indexOf(solicitacao);
  if (index !== -1) solicitacoes.splice(index, 1);
}
</script>

<template>
  <div class="bg-slate-100 min-h-screen">
    <AppHeader logged-in />

    <main class="max-w-7xl mx-auto px-4 py-8">
      <div class="flex justify-between items-center">
        <h1 class="font-bold text-[#1D242F] text-2xl">Dashboard</h1>
        <button
          class="bg-[#F29949] text-[#1D242F] text-sm font-bold py-1.5 px-4 rounded-xl cursor-pointer"
          @click="abrirNovaSolicitacao"
        >
          + Nova Solicitação
        </button>
      </div>

      <StatusCards :stats="stats" />

      <!-- BARRA DE PESQUISA -->
      <div class="bg-white p-2 rounded-xl shadow">
        <div class="flex gap-2 items-center">
          <i class="fa-solid fa-magnifying-glass" style="color: #68768a"></i>

          <input
            v-model="pesquisa"
            type="text"
            name="pesquisar"
            id="pesquisar"
            placeholder="Buscar solicitação po ID,solicitante ou tipo..."
            class="w-full"
          />
        </div>
      </div>
      <!-- FIM DA BARRA DE PESQUISA -->

      <!-- TABELA TABELA TABELA TABELA  -->
      <div
        class="bg-white shadow-sm border border-slate-200 rounded-xl overflow-hidden mt-9"
      >
        <table class="w-full text-left border-collapse">
          <thead class="">
            <tr
              class="bg-slate-50 border-b border-slate-200 text-slate-500 text-sm font-semibold"
            >
              <th class="px-3 py-3 font-semibold hidden">ID</th>
              <th class="py-3 font-semibold hidden sm:table-cell">Data</th>
              <th class="py-3 font-semibold hidden sm:table-cell">
                Solicitante
              </th>
              <th class="py-3 px-3 font-semibold">Tipo de Serviço</th>
              <th class="py-3 font-semibold">Prazo</th>
              <th class="py-3 font-semibold">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="solicitacao in solicitacoesFiltradas"
              :key="solicitacao.id"
              class="shadow"
            >
              <td class="font-semibold text-black px-3">
                {{ solicitacao.id }}
              </td>
              <td class="text-slate-500 hidden sm:table-cell">
                {{ solicitacao.data }}
              </td>
              <td class="font-semibold text-black hidden sm:table-cell">
                {{ solicitacao.solicitante }}
              </td>
              <td class="font-semibold text-black hidden sm:table-cell">
                {{ solicitacao.tipoServico }}
              </td>
              <td class="text-slate-500 w-24 sm:w-auto">
                {{ solicitacao.prazo }}
              </td>
              <td class="p-2">
                <div
                  :class="statusClasses[solicitacao.status]"
                  class="text-sm font-bold rounded-2xl my-2 p-1 max-w-32 text-center"
                >
                  {{ statusLabel[solicitacao.status] }}
                </div>
              </td>
              <td class="p-2">
                <a @click="abrirServico(solicitacao)"
                  ><i
                    class="fa-solid fa-pen-to-square cursor-pointer fa-[20px]"
                    style="color: #1d242f"
                  ></i
                ></a>
                <a @click="excluirSolicitacao(solicitacao)"
                  ><i
                    class="fa-solid fa-trash-can cursor-pointer fa-[20px]"
                    style="color: #1d242f"
                  ></i
                ></a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- FIM TABELA FIM TABELA FIM TABELA FIM TABELA  -->

      <NovaSolicitacaoModal
        :open="novaSolicitacaoAberta"
        @close="fecharNovaSolicitacao"
        @submit="registrarSolicitacao"
      />

      <ServicoModal
        :open="servicoModalAberto"
        :solicitacao="solicitacaoSelecionada"
        @close="fecharServico"
        @submit="salvarServico"
      />
    </main>
    <footer>
      <div class="bg-[#1D242F] p-5"></div>
    </footer>
  </div>
</template>
