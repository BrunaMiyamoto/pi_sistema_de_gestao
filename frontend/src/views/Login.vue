<script setup>
import { computed, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { blockPasteOverLimit } from "../composables/usePasswordPasteLimit";
import { useAuth } from "../composables/useAuth";

const router = useRouter();
const { autenticar } = useAuth();

const form = reactive({
  email: "",
  senha: "",
});

const emailTouched = ref(false);
const emailValido = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email));
const emailErro = computed(() =>
  emailTouched.value && !emailValido.value ? "Informe um e-mail válido." : ""
);

function entrar() {
  emailTouched.value = true;
  if (!emailValido.value) return;
  autenticar(form.email);
  router.push("/dashboard");
}
</script>

<template>
  <div
    class="bg-surface-authBg min-h-screen flex items-center justify-center p-4"
  >
    <main class="mx-auto my-auto px-4 py-8 w-full max-w-sm">
      <section class="bg-surface-dark rounded-xl m-4 p-8">
        <div class="flex items-center py-4 justify-center">
          <div class="bg-brand-mint p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold text-white">Jacto</p>
          <p class="text-brand-turquoise font-bold">Flow</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <h2 class="text-white font-bold text-xl">Acessar JactoFlow</h2>
          <p class="text-ink-mutedDark text-xs">
            Gestão de solicitações técnicas industriais
          </p>
        </div>

        <form @submit.prevent="entrar">
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

          <div class="flex flex-col py-1">
            <label class="text-white font-semibold pb-2">Senha</label>
            <input
              v-model="form.senha"
              type="password"
              name="senha"
              id="senha"
              placeholder="*********"
              maxlength="8"
              @paste="blockPasteOverLimit"
              class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 border border-surface-border focus:outline-none focus:border-brand-mint"
            />
          </div>

          <div class="flex justify-end underline text-brand-mint text-xs py-2">
            <router-link to="/recuperar-senha">Esqueceu sua senha?</router-link>
          </div>

          <button
            type="submit"
            class="inline-block text-center bg-brand-mint text-white font-bold py-1.5 w-full rounded-lg cursor-pointer mt-4 hover:bg-brand-turquoise"
          >
            ENTRAR
          </button>

          <p class="text-center text-ink-mutedDark text-xs pt-4">
            Não tem uma conta?
            <router-link to="/cadastro" class="text-brand-mint underline"
              >Criar conta</router-link
            >
          </p>
        </form>
      </section>
    </main>
    <footer></footer>
  </div>
</template>
