import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Cadastro from "../views/Cadastro.vue";
import RecuperacaoSenha from "../views/RecuperacaoSenha.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: Home },
    { path: "/login", name: "login", component: Login },
    { path: "/dashboard", name: "dashboard", component: Dashboard },
    { path: "/cadastro", name: "cadastro", component: Cadastro },
    {
      path: "/recuperar-senha",
      name: "recuperar-senha",
      component: RecuperacaoSenha,
    },
  ],
});

export default router;
