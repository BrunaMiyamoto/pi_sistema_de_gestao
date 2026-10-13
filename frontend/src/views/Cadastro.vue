<script setup>
import { computed, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { blockPasteOverLimit } from "../composables/usePasswordPasteLimit";
import { useAuth } from "../composables/useAuth";

const router = useRouter();
const { registrarUsuario } = useAuth();

const perfis = ["Solicitante", "Ferramentaria"];

const form = reactive({
  nome: "",
  email: "",
  tipoPerfil: "",
  senha: "",
  confirmarSenha: "",
});

const perfilQuery = ref("");
const perfilOpen = ref(false);
const emailTouched = ref(false);
const mostrarSenha = ref(false);
const mostrarConfirmarSenha = ref(false);
const submitting = ref(false);

const perfisFiltrados = computed(() => {
  const termo = perfilQuery.value.trim().toLowerCase();
  if (!termo) return perfis;
  return perfis.filter((perfil) => perfil.toLowerCase().includes(termo));
});

function selecionarPerfil(perfil) {
  form.tipoPerfil = perfil;
  perfilQuery.value = perfil;
  perfilOpen.value = false;
}

const emailValido = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email));

const errors = computed(() => ({
  nome: form.nome.trim() ? "" : "Informe seu nome completo.",
  email: emailValido.value ? "" : "Informe um e-mail válido.",
  tipoPerfil: form.tipoPerfil ? "" : "Selecione um tipo de perfil.",
  senha: form.senha.length === 8 ? "" : "A senha deve ter exatamente 8 caracteres.",
  confirmarSenha:
    form.confirmarSenha && form.confirmarSenha === form.senha
      ? ""
      : "As senhas não coincidem.",
}));

const isValid = computed(() => Object.values(errors.value).every((erro) => !erro));

function criarConta() {
  emailTouched.value = true;
  if (!isValid.value) return;
  submitting.value = true;
  registrarUsuario({
    nome: form.nome.trim(),
    email: form.email,
    tipoPerfil: form.tipoPerfil,
  });
  setTimeout(() => {
    submitting.value = false;
    router.push("/login");
  }, 600);
}
</script>

<template>
  <div class="bg-surface-authBg min-h-screen flex items-center justify-center p-4">
    <main class="mx-auto my-auto px-4 py-8 w-full max-w-md">
      <section class="bg-surface-dark rounded-xl m-4 p-8">
        <div class="flex items-center py-4 justify-center">
          <div class="bg-brand-mint p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold text-white">Jacto</p>
          <p class="text-brand-turquoise font-bold">Flow</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <h2 class="text-white font-bold text-xl">Criar conta no JactoFlow</h2>
          <p class="text-ink-mutedDark text-xs">
            Gestão de solicitações técnicas industriais
          </p>
        </div>

        <form @submit.prevent="criarConta">
          <div class="flex flex-col py-6">
            <label class="text-white font-semibold pb-2">Nome completo</label>
            <div class="relative">
              <input
                v-model="form.nome"
                type="text"
                name="nome"
                id="nome"
                placeholder="Digite seu nome completo"
                class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 pr-9 w-full border border-surface-border focus:outline-none focus:border-brand-mint"
              />
              <button
                v-if="form.nome"
                type="button"
                tabindex="-1"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-mutedDark cursor-pointer"
                @click="form.nome = ''"
              >
                <i class="fa-solid fa-xmark"></i>
              </button>
            </div>
          </div>

          <div class="flex flex-col py-2">
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
            <p v-if="emailTouched && errors.email" class="text-red-400 text-xs pt-1">
              {{ errors.email }}
            </p>
          </div>

          <div class="flex flex-col py-2 relative">
            <label class="text-white font-semibold pb-2">Tipo de perfil</label>
            <input
              v-model="perfilQuery"
              type="text"
              placeholder="Buscar perfil..."
              class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 pr-9 w-full border border-surface-border focus:outline-none focus:border-brand-mint"
              @focus="perfilOpen = true"
              @input="form.tipoPerfil = ''"
            />
            <button
              v-if="perfilQuery"
              type="button"
              tabindex="-1"
              class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-mutedDark cursor-pointer"
              @click="perfilQuery = ''; form.tipoPerfil = ''"
            >
              <i class="fa-solid fa-xmark"></i>
            </button>
            <ul
              v-if="perfilOpen"
              class="absolute top-full mt-1 left-0 right-0 bg-surface-authBg border border-surface-border rounded-lg overflow-hidden z-10"
            >
              <li
                v-for="perfil in perfisFiltrados"
                :key="perfil"
                class="px-3 py-2 text-sm cursor-pointer"
                :class="
                  form.tipoPerfil === perfil
                    ? 'bg-brand-mint/10 text-brand-mint'
                    : 'text-slate-300 hover:bg-surface-dark'
                "
                @mousedown.prevent="selecionarPerfil(perfil)"
              >
                {{ perfil }}
              </li>
              <li
                v-if="!perfisFiltrados.length"
                class="px-3 py-2 text-sm text-ink-mutedDark"
              >
                Nenhum perfil encontrado.
              </li>
            </ul>
          </div>

          <div class="flex flex-col py-2">
            <label class="text-white font-semibold pb-2">Senha</label>
            <div class="relative">
              <input
                v-model="form.senha"
                :type="mostrarSenha ? 'text' : 'password'"
                name="senha"
                id="senha"
                placeholder="*********"
                maxlength="8"
                minlength="8"
                @paste="blockPasteOverLimit"
                class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 pr-9 w-full border border-surface-border focus:outline-none focus:border-brand-mint"
              />
              <button
                type="button"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-mutedDark cursor-pointer"
                @click="mostrarSenha = !mostrarSenha"
              >
                <i :class="mostrarSenha ? 'fa-regular fa-eye-slash' : 'fa-regular fa-eye'"></i>
              </button>
            </div>
            <p class="text-ink-placeholder text-xs pt-1">
              Use exatamente 8 caracteres para sua senha.
            </p>
          </div>

          <div class="flex flex-col py-2">
            <label class="text-white font-semibold pb-2">Confirmar senha</label>
            <div class="relative">
              <input
                v-model="form.confirmarSenha"
                :type="mostrarConfirmarSenha ? 'text' : 'password'"
                name="confirmarSenha"
                id="confirmarSenha"
                placeholder="*********"
                maxlength="8"
                minlength="8"
                @paste="blockPasteOverLimit"
                class="bg-surface-authBg rounded-lg text-slate-300 text-sm py-2 px-3 pr-9 w-full border border-surface-border focus:outline-none focus:border-brand-mint"
              />
              <button
                type="button"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-mutedDark cursor-pointer"
                @click="mostrarConfirmarSenha = !mostrarConfirmarSenha"
              >
                <i
                  :class="
                    mostrarConfirmarSenha ? 'fa-regular fa-eye-slash' : 'fa-regular fa-eye'
                  "
                ></i>
              </button>
            </div>
          </div>

          <button
            type="submit"
            :disabled="!isValid || submitting"
            class="inline-block text-center bg-brand-mint text-white font-bold py-1.5 w-full rounded-lg cursor-pointer mt-4 hover:bg-brand-turquoise disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ submitting ? "Criando conta..." : "CRIAR CONTA" }}
          </button>

          <p class="text-center text-ink-mutedDark text-xs pt-4">
            Já tem uma conta?
            <router-link to="/login" class="text-brand-mint underline">Voltar ao login</router-link>
          </p>
        </form>
      </section>
    </main>
  </div>
</template>
