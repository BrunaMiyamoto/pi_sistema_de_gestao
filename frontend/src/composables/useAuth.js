import { reactive } from "vue";

const USERS_KEY = "jactoflow:users";
const SESSION_KEY = "jactoflow:currentUser";

function loadUsers() {
  try {
    const raw = localStorage.getItem(USERS_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function loadCurrentUser() {
  try {
    const raw = localStorage.getItem(SESSION_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

const state = reactive({
  users: loadUsers(),
  currentUser: loadCurrentUser(),
});

function persistUsers() {
  localStorage.setItem(USERS_KEY, JSON.stringify(state.users));
}

function persistSession() {
  if (state.currentUser) {
    localStorage.setItem(SESSION_KEY, JSON.stringify(state.currentUser));
  } else {
    localStorage.removeItem(SESSION_KEY);
  }
}

function registrarUsuario({ nome, email, tipoPerfil }) {
  const usuario = { nome, email, tipoPerfil };
  state.users = [...state.users.filter((u) => u.email !== email), usuario];
  persistUsers();
  return usuario;
}

function autenticar(email) {
  const usuario = state.users.find((u) => u.email === email) || null;
  state.currentUser = usuario;
  persistSession();
  return usuario;
}

function sair() {
  state.currentUser = null;
  persistSession();
}

export function useAuth() {
  return {
    state,
    registrarUsuario,
    autenticar,
    sair,
  };
}
