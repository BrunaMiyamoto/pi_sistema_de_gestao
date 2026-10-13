<script setup>
import { computed, reactive, ref } from "vue";

const form = reactive({ email: "" });
const submitting = ref(false);
const enviado = ref(false);
const emailTouched = ref(false);

const emailValido = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email));
const emailErro = computed(() =>
  emailTouched.value && !emailValido.value ? "Informe um e-mail válido." : ""
);

function enviarLink() {
  emailTouched.value = true;
  if (!emailValido.value) return;
  submitting.value = true;
  setTimeout(() => {
    submitting.value = false;
    enviado.value = true;
  }, 600);
}
</script>

<template>
  <div class="bg-surface-authBg min-h-screen flex items-center justify-center p-4">
    <main class="mx-auto my-auto px-4 py-8 w-full max-w-sm">
      <section class="bg-surface-dark rounded-xl m-4 p-8">
        <div class="flex items-center py-4 justify-center">
          <div class="bg-brand-mint p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold text-white">Jacto</p>
          <p class="text-brand-turquoise font-bold">Flow</p>
        </div>

        <template v-if="!enviado">
          <div class="flex flex-col items-center text-center">
            <h2 class="text-white font-bold text-xl">Esqueceu sua senha?</h2>
            <p class="text-ink-mutedDark text-xs">
              Informe o e-mail da sua conta. Enviaremos um link para redefinir sua
              senha.
            </p>
          </div>

          <form @submit.prevent="enviarLink">
            <div class="flex flex-col py-4">
              <label class="text-white font-semibold pb-2">E-mail</label>
              <div class="relative">
                <input
                  v-model="form.email"
                  type="email"
                  name="email"
                  id="email"
                  placeholder="usuario@jacto.com.br"
                  @blur="emailTouched = true"
                  class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 pr-9 w-full border border-surface-border focus:outline-none focus:border-brand-mint"
                />
                <button
                  v-if="form.email"
                  type="button"
                  tabindex="-1"
                  class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-mutedDark cursor-pointer"
                  @click="form.email = ''"
                >
                  <i class="fa-solid fa-xmark"></i>
                </button>
              </div>
              <p v-if="emailErro" class="text-red-400 text-xs pt-1">{{ emailErro }}</p>
            </div>

            <button
              type="submit"
              :disabled="!emailValido || submitting"
              class="inline-block text-center bg-brand-mint text-white font-bold py-1.5 w-full rounded-lg cursor-pointer mt-4 hover:bg-brand-turquoise disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ submitting ? "Enviando..." : "ENVIAR LINK" }}
            </button>
          </form>
        </template>

        <template v-else>
          <div class="flex flex-col items-center text-center py-2">
            <i class="fa-regular fa-circle-check text-brand-mint text-3xl pb-3"></i>
            <h2 class="text-white font-bold text-lg">Link enviado!</h2>
            <p class="text-ink-mutedDark text-xs">
              Verifique seu e-mail para redefinir sua senha.
            </p>
          </div>
        </template>

        <p class="text-center text-ink-mutedDark text-xs pt-4">
          <router-link to="/login" class="text-brand-mint underline">
            ← Voltar ao login
          </router-link>
        </p>
      </section>
    </main>
  </div>
</template>
