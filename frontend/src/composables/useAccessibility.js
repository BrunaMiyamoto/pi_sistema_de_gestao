import { reactive, watch } from "vue";

const STORAGE_KEY = "jactoflow:accessibility";
const defaults = { fontScale: 1, colorScheme: "claro", highContrast: false };

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? { ...defaults, ...JSON.parse(raw) } : { ...defaults };
  } catch {
    return { ...defaults };
  }
}

const state = reactive(load());

function applyToDocument() {
  const root = document.documentElement;
  root.style.setProperty("--a11y-font-scale", String(state.fontScale));
  root.classList.toggle("dark", state.colorScheme === "escuro");
  root.classList.toggle("high-contrast", state.highContrast);
}

watch(
  state,
  () => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    applyToDocument();
  },
  { deep: true },
);

applyToDocument();

export function useAccessibility() {
  return {
    state,
    setFontScale: (value) => (state.fontScale = value),
    setColorScheme: (value) => (state.colorScheme = value),
    setHighContrast: (value) => (state.highContrast = value),
  };
}
