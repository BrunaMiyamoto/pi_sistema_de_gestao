<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const form = reactive({
  email: "",
  senha: "",
});

function entrar() {
  router.push("/dashboard");
}
</script>

<template>
  <div
    class="bg-[#111826] min-h-screen flex items-center justify-center p-4"
  >
    <main class="mx-auto my-auto px-4 py-8 w-full max-w-sm">
      <section class="bg-[#1D242F] rounded-xl m-4 p-8">
        <div class="flex items-center py-4 justify-center">
          <div class="bg-[#E19047] p-0.5 rounded-sm m-2">
            <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
          </div>
          <p class="font-bold text-white">Jacto</p>
          <p class="text-[#E19047] font-bold">Flow</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <h2 class="text-white font-bold text-xl">Acessar JactoFlow</h2>
          <p class="text-slate-500 text-xs">
            Gestão de solicitações técnicas industriais
          </p>
        </div>

        <form @submit.prevent="entrar">
          <div class="flex flex-col py-4">
            <label class="text-white font-semibold pb-2">E-mail</label>
            <input
              v-model="form.email"
              type="email"
              name="email"
              id="email"
              placeholder="usuario@jacto.com.br"
              class="bg-[#111826] rounded-lg text-slate-300 text-sm py-2 px-3 border border-slate-700 focus:outline-none focus:border-[#E19047]"
            />
          </div>

          <div class="flex flex-col py-1">
            <label class="text-white font-semibold pb-2">Senha</label>
            <input
              v-model="form.senha"
              type="password"
              name="senha"
              id="senha"
              placeholder="*********"
              class="bg-[#111826] rounded-lg text-slate-300 text-sm py-2 px-3 border border-slate-700 focus:outline-none focus:border-[#E19047]"
            />
          </div>

          <div
            class="flex justify-end underline text-[#E19047] text-xs py-2 cursor-pointer"
          >
            <a>Esqueceu sua senha?</a>
          </div>

          <button
            type="submit"
            class="inline-block text-center bg-[#E19047] font-bold py-1.5 w-full rounded-lg cursor-pointer mt-4 hover:bg-[#F29949] hover:text-slate-700"
          >
            Entrar no Sistema
          </button>
        </form>
      </section>
    </main>
    <footer></footer>
  </div>
</template>
