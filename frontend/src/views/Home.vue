<script setup>
import { reactive } from "vue";
import AppHeader from "../components/AppHeader.vue";
import StatusCards from "../components/StatusCards.vue";

const stats = reactive({
  pendentes: 1,
  emAnalise: 1,
  emAtendimento: 1,
  concluidas: 1,
});
</script>

<template>
  <div class="bg-surface-page dark:bg-surface-authBg min-h-screen">
    <AppHeader />

    <main class="max-w-7xl mx-auto px-4 py-8">
      <h1 class="font-bold text-surface-dark dark:text-white text-2xl">Visão Geral</h1>
      <StatusCards :stats="stats" />
    </main>

    <footer>
      <div class=""></div>
    </footer>
  </div>
</template>
