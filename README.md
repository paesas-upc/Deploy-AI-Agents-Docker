````markdown name=README.md
# AI Agents (Docker) — FastAPI + Multi-Agent Supervisor (EN/ES)

> **Credits / Attribution (Very Important)**
>
> This repository (**paesas-upc/AI-agents-docker**) is a replication/adaptation of the original project:
> **@codingforentrepreneurs/build-deploy-ai-agent-python-docker**  
> https://github.com/codingforentrepreneurs/build-deploy-ai-agent-python-docker
>
> I replicated it by following the YouTube tutorial:  
> **“Complete Guide to Build and Deploy an AI Agent with Docker Containers and Python”** by CodingEntrepreneurs  
> https://www.youtube.com/watch?v=KC8HT0eWSGk
>
> All credit for the original idea/structure goes to **CodingEntrepreneurs**. This repo is for learning and experimentation.

---

## English

### Overview
This project demonstrates how to build and run a **multi-agent AI system** behind a **FastAPI** web API, packaged with **Docker** and orchestrated with **Docker Compose**.

Main components:
- **FastAPI** backend exposing endpoints like `POST /api/chats/`
- **Multi-agent supervisor** (LangGraph/LangChain style) that can route tasks to specialized agents
- **Email tools** (send an email to the configured address; read inbox)
- **PostgreSQL** database to store chat messages

### Architecture (High Level)
1. A client sends an HTTP request to the backend (e.g., using `curl`).
2. FastAPI validates the request payload.
3. The message is stored in Postgres.
4. The supervisor agent runs and may call tools (research, send email, read inbox).
5. The final response is returned as JSON.

### Requirements
- Docker + Docker Compose
- An OpenAI-compatible API key (or a compatible LLM endpoint, depending on your configuration)
- (Optional) Email credentials (app password recommended if using Gmail)

### Environment variables
This repo uses environment variables for configuration (API keys, DB URL, email settings). A template file exists:

- `.env.sample` (template)

**Important note:** In `compose.yaml`, the backend currently loads environment variables from `.env.sample` via `env_file`.  
For real usage, it’s recommended to create your own `.env` (not committed) and point Compose to that instead.

Typical variables used:
- `OPENAI_API_KEY`
- `OPENAI_MODEL_NAME`
- `DATABASE_URL`
- `EMAIL_ADDRESS`
- `EMAIL_PASSWORD` (use an app password; do not use your real password)
- `EMAIL_HOST`
- `EMAIL_PORT`

### Run locally (Docker Compose)
From the repo root:

```bash
docker compose up --build
```

Backend will be available at:
- http://localhost:8080

### Test the API
Health check:
```bash
curl http://localhost:8080/api/chats/
```

Create a message (triggers the agent supervisor):
```bash
curl -X POST -H "Content-Type: application/json" \
  -d "{\"message\": \"Hello world\"}" \
  http://localhost:8080/api/chats/
```

Recent messages:
```bash
curl http://localhost:8080/api/chats/recent/
```

### About the “email me the results” behavior
The “send email” tool sends to the configured environment variable `EMAIL_ADDRESS` by default (i.e., “send to myself” behavior).  
If you deploy this publicly, add authentication/rate-limiting to prevent abuse and unexpected costs.

### Deployment (Concept)
This project is designed to be deployable on platforms that support Docker-based deployments (e.g., Railway). In a hosted deployment:
- The code runs on the platform’s infrastructure
- Requests hit the public URL
- Environment variables are set on the platform (not on the user’s computer)

---

## Español

### Descripción general
Este proyecto demuestra cómo construir y ejecutar un **sistema multi-agente de IA** detrás de una API web con **FastAPI**, empaquetado con **Docker** y orquestado con **Docker Compose**.

Componentes principales:
- Backend **FastAPI** que expone endpoints como `POST /api/chats/`
- **Supervisor multi-agente** (estilo LangGraph/LangChain) que delega tareas en agentes especializados
- **Herramientas de email** (enviar un email a la dirección configurada; leer la bandeja de entrada)
- Base de datos **PostgreSQL** para almacenar mensajes del chat

### Arquitectura (Alto nivel)
1. Un cliente envía una petición HTTP al backend (por ejemplo con `curl`).
2. FastAPI valida el payload de entrada.
3. El mensaje se guarda en Postgres.
4. El supervisor ejecuta el flujo multi-agente y puede llamar herramientas (investigación, enviar email, leer inbox).
5. Se devuelve la respuesta final en JSON.

### Requisitos
- Docker + Docker Compose
- Una API key compatible con OpenAI (o un endpoint LLM compatible, según tu configuración)
- (Opcional) Credenciales de email (se recomienda app password si usas Gmail)

### Variables de entorno
Este repo usa variables de entorno para configuración (API keys, DB URL, email). Existe un archivo plantilla:

- `.env.sample` (plantilla)

**Nota importante:** En `compose.yaml`, el backend carga variables desde `.env.sample` mediante `env_file`.  
Para uso real, se recomienda crear tu propio `.env` (no versionado) y apuntar Compose a ese archivo.

Variables típicas:
- `OPENAI_API_KEY`
- `OPENAI_MODEL_NAME`
- `DATABASE_URL`
- `EMAIL_ADDRESS`
- `EMAIL_PASSWORD` (usa app password; no uses tu contraseña real)
- `EMAIL_HOST`
- `EMAIL_PORT`

### Ejecutar en local (Docker Compose)
Desde la raíz del repo:

```bash
docker compose up --build
```

El backend estará disponible en:
- http://localhost:8080

### Probar la API
Health check:
```bash
curl http://localhost:8080/api/chats/
```

Crear un mensaje (dispara el supervisor multi-agente):
```bash
curl -X POST -H "Content-Type: application/json" \
  -d "{\"message\": \"Hola mundo\"}" \
  http://localhost:8080/api/chats/
```

Mensajes recientes:
```bash
curl http://localhost:8080/api/chats/recent/
```

### Sobre el comportamiento “envíame un email con los resultados”
La herramienta de envío de email envía por defecto a la variable `EMAIL_ADDRESS` (comportamiento tipo “enviarme a mí mismo”).  
Si despliegas esto públicamente, añade autenticación y/o rate-limiting para evitar abusos y costes inesperados.

### Despliegue (Concepto)
Este proyecto está pensado para desplegarse en plataformas que soporten Docker (por ejemplo Railway). En un despliegue hospedado:
- El código se ejecuta en la infraestructura de la plataforma
- Las peticiones van a una URL pública
- Las variables de entorno se configuran en la plataforma (no en el ordenador del usuario)

---

## License
Check this repository’s license (if present). If no license is included, assume default copyright rules apply.

## Acknowledgements
- Original repository: https://github.com/codingforentrepreneurs/build-deploy-ai-agent-python-docker
- Tutorial: https://www.youtube.com/watch?v=KC8HT0eWSGk
````