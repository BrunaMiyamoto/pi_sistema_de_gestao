<script setup>
import { ref } from "vue";
import { useAccessibility } from "../composables/useAccessibility";

const { state, setFontScale, setColorScheme, setHighContrast } =
  useAccessibility();

const isOpen = ref(false);

function toggleOpen() {
  isOpen.value = !isOpen.value;
}
</script>

<template>
  <div class="fixed bottom-6 right-6 z-[60]">
    <div
      v-if="isOpen"
      class="mb-3 w-80 max-w-[calc(100vw-3rem)] bg-white text-surface-dark rounded-xl shadow-2xl p-5"
    >
      <div class="flex justify-between items-start">
        <div>
          <h2 class="font-bold">Acessibilidade</h2>
          <p class="text-xs text-ink-secondary">Ajuste fonte e cores da tela</p>
        </div>
        <button
          type="button"
          class="cursor-pointer text-ink-secondary"
          @click="toggleOpen"
        >
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="mt-4">
        <label class="text-sm font-semibold">Tamanho da fonte</label>
        <div class="flex items-center gap-2 mt-2">
          <span class="text-xs font-bold">A-</span>
          <input
            type="range"
            min="0.875"
            max="1.5"
            step="0.125"
            :value="state.fontScale"
            class="w-full accent-brand-mint"
            @input="setFontScale(Number($event.target.value))"
          />
          <span class="text-base font-bold">A+</span>
        </div>
        <div class="flex gap-3 mt-3">
          <div
            class="border border-surface-borderLight rounded-lg p-2 flex-1"
            :style="{ fontSize: `calc(0.75rem * ${state.fontScale})` }"
          >
            <p class="text-ink-secondary">Exemplo</p>
            <p class="font-semibold">Solicitação #001</p>
          </div>
          <div
            class="border border-surface-borderLight rounded-lg p-2 flex-1"
            :style="{ fontSize: `calc(1.125rem * ${state.fontScale})` }"
          >
            <p class="text-ink-secondary">Exemplo</p>
            <p class="font-semibold">Solicitação #001</p>
          </div>
        </div>
      </div>

      <div class="mt-4">
        <label class="text-sm font-semibold">Esquema de cores</label>
        <div class="flex gap-3 mt-2">
          <button
            type="button"
            class="flex-1 border rounded-lg p-2 cursor-pointer text-left text-xs"
            :class="
              state.colorScheme === 'claro'
                ? 'ring-2 ring-brand-mint border-brand-mint'
                : 'border-surface-borderLight'
            "
            @click="setColorScheme('claro')"
          >
            <span class="flex gap-1">
              <span class="w-3 h-3 rounded-full bg-white border border-surface-borderLight"></span>
              <span class="w-3 h-3 rounded-full bg-surface-page"></span>
              <span class="w-3 h-3 rounded-full bg-brand-mint"></span>
            </span>
            <span class="block mt-1">Claro</span>
          </button>
          <button
            type="button"
            class="flex-1 border rounded-lg p-2 cursor-pointer text-left text-xs bg-surface-dark text-white"
            :class="
              state.colorScheme === 'escuro'
                ? 'ring-2 ring-brand-mint border-brand-mint'
                : 'border-surface-dark'
            "
            @click="setColorScheme('escuro')"
          >
            <span class="flex gap-1">
              <span class="w-3 h-3 rounded-full bg-black"></span>
              <span class="w-3 h-3 rounded-full bg-surface-authBg"></span>
              <span class="w-3 h-3 rounded-full bg-brand-mint"></span>
            </span>
            <span class="block mt-1">Escuro</span>
          </button>
        </div>
      </div>

      <div class="mt-4 flex items-center justify-between">
        <div>
          <p class="text-sm font-semibold">Contraste alto</p>
          <p class="text-xs text-ink-secondary">Ativar contraste alto</p>
        </div>
        <button
          type="button"
          role="switch"
          :aria-checked="state.highContrast"
          class="w-10 h-6 rounded-full relative cursor-pointer transition-colors"
          :class="state.highContrast ? 'bg-brand-mint' : 'bg-surface-borderLight'"
          @click="setHighContrast(!state.highContrast)"
        >
          <span
            class="absolute top-0.5 w-5 h-5 rounded-full bg-white shadow transition-all"
            :class="state.highContrast ? 'left-[18px]' : 'left-0.5'"
          ></span>
        </button>
      </div>
    </div>

    <button
      type="button"
      class="bg-white text-surface-dark rounded-full shadow-lg px-4 py-2 flex items-center gap-2 cursor-pointer ml-auto"
      @click="toggleOpen"
    >
      <i class="fa-solid fa-universal-access"></i>
      <span class="text-xs text-left leading-tight">
        Acessibilidade
        <br />
        <span class="text-ink-secondary">{{ isOpen ? "Aberto" : "Atalho" }}</span>
      </span>
    </button>
  </div>
</template>
