<script setup>
defineProps({
  stats: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div class="grid grid-1 lg:grid-cols-4 gap-6 my-10">
    <article class="bg-status-pending rounded-xl shadow-sm text-white px-4 py-5">
      <div class="flex justify-between items-center pb-3">
        <p class="text-xs font-semibold">PENDENTES</p>
        <div>
          <i class="fa-regular fa-clock" style="color: #ffffff"></i>
        </div>
      </div>
      <div class="text-3xl font-bold">{{ stats.pendentes }}</div>
    </article>

    <article class="bg-status-analysisBlue rounded-xl shadow-sm text-white px-4 py-5">
      <div class="flex justify-between items-center pb-3">
        <p class="text-xs font-semibold">EM ANÁLISE</p>
        <div>
          <i class="fa-solid fa-magnifying-glass" style="color: #ffffff"></i>
        </div>
      </div>
      <div class="text-3xl font-bold">{{ stats.emAnalise }}</div>
    </article>

    <article class="bg-status-inProgress rounded-xl shadow-sm text-white px-4 py-5">
      <div class="flex justify-between items-center pb-3">
        <p class="text-xs font-semibold">EM ATENDIMENTO</p>
        <div>
          <i class="fa-solid fa-gear" style="color: #ffffff"></i>
        </div>
      </div>
      <div class="text-3xl font-bold">{{ stats.emAtendimento }}</div>
    </article>

    <article class="bg-brand-mint rounded-xl shadow-sm text-white px-4 py-5">
      <div class="flex justify-between items-center pb-3">
        <p class="text-xs font-semibold">CONCLUÍDAS</p>
        <div>
          <i class="fa-regular fa-circle-check" style="color: #ffffff"></i>
        </div>
      </div>
      <div class="text-3xl font-bold">{{ stats.concluidas }}</div>
    </article>
  </div>
</template>
