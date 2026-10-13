<script setup>
import { useAccessibility } from "./composables/useAccessibility";
import AccessibilityPanel from "./components/AccessibilityPanel.vue";

useAccessibility();
</script>

<template>
  <router-view />
  <AccessibilityPanel />
</template>
