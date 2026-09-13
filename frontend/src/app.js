const modal = document.getElementById("modal");
const abreBtn = document.getElementById("abreModal");
const fechaBtn = document.getElementById("fechaModal");

abreBtn.addEventListener("click", () => {
  modal.classList.remove("hidden");
});

fechaBtn.addEventListener("click", () => {
  modal.classList.add("hidden");
});

modal.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.classList.add("hidden");
  }
});

const modalServicos = document.getElementById("modalServicos");
const abreModalServicos = document.querySelectorAll(".abreModalServicos");
const fechaModalServicos = document.getElementById("fechaModalServicos");

abreModalServicos.forEach(botao => {botao.addEventListener("click", () => {
  modalServicos.classList.remove("hidden");
  });
});

fechaModalServicos.addEventListener("click", () => {
  modalServicos.classList.add("hidden");
});

modalServicos.addEventListener("click", (e) => {
  if (e.target === modalServicos) {
    modalServicos.classList.add("hidden");
  }
});

