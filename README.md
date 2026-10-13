# pi_sistema_de_gest-o
Sistema de gestão desenvolvido como projeto integrador da UNIVESP

## Estrutura

- `frontend/` — aplicação Vue 3 (Composition API) com Vite, Vue Router e Tailwind CSS.
- `backend/` — API em FastAPI.

## Como executar

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
