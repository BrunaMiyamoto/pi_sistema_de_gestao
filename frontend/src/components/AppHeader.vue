<script setup>
defineProps({
  loggedIn: {
    type: Boolean,
    default: false,
  },
});
</script>

<template>
  <header class="bg-[#1D242F] text-white p-2">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <div class="flex items-center">
        <div class="bg-[#E19047] p-0.5 rounded-sm m-2">
          <i class="fa-solid fa-gear" style="color: rgb(30, 48, 80)"></i>
        </div>
        <p class="font-bold">Jacto</p>
        <p class="text-[#E19047] font-bold">Flow</p>
      </div>

      <nav v-if="!loggedIn" class="flex gap-1">
        <div class="pb-3">
          <i
            class="fa-regular fa-circle-user fa-xl pt-6 m-2"
            style="color: #ffffff"
          ></i>
          <router-link
            to="/login"
            class="cursor-pointer hover:text-[#E19047] font-bold"
            >Login</router-link
          >
        </div>
      </nav>

      <nav v-else class="flex gap-1">
        <div>
          <i
            class="fa-regular fa-circle-user fa-xl pt-6 m-2"
            style="color: #ffffff"
          ></i>
        </div>

        <div class="relative group py-2 text-sm">
          <p class="text-slate-600">USER</p>
          <button class="peer cursor-pointer hover:text-slate-500">
            Equipe Ferramentaria<i
              class="fa solid fa-chevron-down ml-1 fa-xs"
            ></i>
          </button>
          <div
            class="peer-focus:opacity-100 peer-focus:visible transition-all bg-[#1D242F] p-2 border border-slate-200 rounded-lg w-40 shadow-lg absolute left-0 top-full pt-1 opacity-0 invisible group-hover:opacity-100 group-hover:visible"
          >
            <a href="#" class="block py-1 hover:text-slate-500">Perfil</a>
            <router-link to="/" class="block py-1 hover:text-slate-500"
              >Sair</router-link
            >
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>
