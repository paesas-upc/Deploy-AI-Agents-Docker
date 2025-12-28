# Deploy AI Agents with Docker — FastAPI + Multi-Agent Supervisor

> **Credits / Attribution**
>
> This repository is a replication/adaptation of the original project:
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
This repository (**paesas-upc/Deploy-AI-Agents-Docker**) focuses on showing how a **multi-agent AI system** can be packaged and deployed as a real service using modern tooling. The key idea is to expose an agent pipeline through an HTTP API so it can be triggered remotely (not only from a local script).

At a high level, a client sends a request to the API, the backend runs the multi-agent workflow, and the system returns a structured response. A database can be used to persist messages/events.

### Tools used

#### Docker (Containerization)
**Docker** packages the application and its dependencies into a **container image** so it runs consistently across environments (local machine, cloud, CI/CD). This is especially helpful for multi-service setups where you want repeatable builds and predictable runtime behavior.

#### FastAPI (HTTP API Layer)
**FastAPI** is the Python web framework that exposes the project’s functionality as **HTTP endpoints** (for example, a `POST` endpoint to submit a user message). It acts as the “entry point” to trigger the agent pipeline from any client that can make HTTP requests.

#### Railway (Deployment Platform)
**Railway** is a hosting/deployment platform where we run our containerized application in the cloud. When deployed, requests from users are executed on **Railway’s infrastructure**, using the environment configuration defined in Railway, and the API response is returned to the user over HTTP.

#### LangChain + LangGraph (Agents + Orchestration)
- **LangChain** provides building blocks for LLM apps (models, tools, tool-calling patterns, prompt flows).
- **LangGraph** (and the supervisor pattern used here) helps orchestrate **multiple agents**: a “supervisor” routes tasks to specialized agents/tools to complete a request.

Together, they enable a system where different agents can cooperate (research + messaging/email actions) instead of using a single monolithic prompt.

#### PostgreSQL (Persistence)
**PostgreSQL** is used to persist chat messages or other events produced by the API. Storing messages in a database is useful for auditing, debugging, analytics, and building UI features like “recent conversations”.

### Architecture (High Level)
1. A user/client sends an HTTP request to the deployed API.
2. FastAPI receives and validates the request payload.
3. The message can be persisted to PostgreSQL.
4. A multi-agent supervisor runs and may delegate tasks to specialized agents/tools.
5. The final result is returned to the client as an HTTP response.

### Final behavior
Depending on the user prompt, this project can execute an end-to-end **agent pipeline** with real-world side effects:

- A **Research Agent** uses the LLM to gather/compose information about a topic requested by the user.
- An **Email Agent** can send the resulting summary as an email.
- A **Supervisor** (LangGraph) orchestrates and routes work between these agents.

All of this is exposed through a **FastAPI** HTTP endpoint, **containerized with Docker**, and **deployed on Railway** so that any client can trigger the workflow remotely via an HTTP request.

---

## Español

### Descripción general
Este repositorio (**paesas-upc/Deploy-AI-Agents-Docker**) se centra en mostrar cómo empaquetar y desplegar un **sistema multi-agente de IA** como un servicio real utilizando herramientas modernas. La idea clave es exponer el pipeline de agentes mediante una API HTTP para poder ejecutarlo remotamente (no solo como un script local).

A alto nivel, un cliente envía una petición a la API, el backend ejecuta el flujo multi-agente y el sistema devuelve una respuesta estructurada. También puede usarse una base de datos para persistir mensajes/eventos.

### Herramientas utilizadas

#### Docker (Contenerización)
**Docker** empaqueta la aplicación y sus dependencias en una **imagen de contenedor** para que se ejecute de forma consistente en distintos entornos (local, cloud, CI/CD). Esto es especialmente útil en arquitecturas con varios servicios, donde se busca reproducibilidad y comportamiento predecible.

#### FastAPI (Capa de API HTTP)
**FastAPI** es el framework web en Python que expone la funcionalidad del proyecto como **endpoints HTTP** (por ejemplo, un `POST` para enviar un mensaje del usuario). Actúa como “puerta de entrada” para disparar el pipeline de agentes desde cualquier cliente capaz de hacer peticiones HTTP.

#### Railway (Plataforma de despliegue)
**Railway** es una plataforma de hosting/despliegue donde ejecutamos nuestra aplicación contenerizada en la nube. Una vez desplegada, las peticiones de los usuarios se ejecutan en la **infraestructura de Railway**, utilizando la configuración de entorno definida en Railway, y la respuesta de la API se devuelve al usuario a través de HTTP.

#### LangChain + LangGraph (Agentes + Orquestación)
- **LangChain** aporta componentes para construir aplicaciones con LLM (modelos, herramientas, tool-calling, flujos de prompts).
- **LangGraph** (y el patrón de supervisor usado aquí) ayuda a orquestar **múltiples agentes**: un “supervisor” reparte tareas entre agentes/herramientas especializadas.

Juntos permiten que diferentes agentes cooperen (por ejemplo, investigación + acciones de mensajería/email) en lugar de depender de un único prompt monolítico.

#### PostgreSQL (Persistencia)
**PostgreSQL** se utiliza para persistir mensajes del chat u otros eventos generados por la API. Guardar mensajes en base de datos es útil para auditoría, depuración, analítica y para construir funcionalidades de UI como “conversaciones recientes”.

### Arquitectura (Alto nivel)
1. Un usuario/cliente envía una petición HTTP a la API desplegada.
2. FastAPI recibe y valida el payload.
3. El mensaje puede persistirse en PostgreSQL.
4. Se ejecuta un supervisor multi-agente que puede delegar tareas a agentes/herramientas especializadas.
5. El resultado final se devuelve al cliente como respuesta HTTP.

### Comportamiento final
Dependiendo del prompt del usuario, este proyecto puede ejecutar un **pipeline de agentes** de extremo a extremo con efectos reales:

- Un **Agente de investigación (Research Agent)** utiliza el LLM para recopilar/crear información sobre un tema solicitado por el usuario.
- Un **Agente de email (Email Agent)** puede enviar por correo electrónico el resumen resultante.
- Un **Supervisor** (LangGraph) orquesta y enruta el trabajo entre estos agentes.

Todo esto se expone mediante un endpoint HTTP de **FastAPI**, se **conteneriza con Docker** y se **despliega en Railway**, de modo que cualquier cliente pueda disparar el flujo de trabajo remotamente mediante una petición HTTP.

---

## Acknowledgements
- Original repository: https://github.com/codingforentrepreneurs/build-deploy-ai-agent-python-docker
- Tutorial: https://www.youtube.com/watch?v=KC8HT0eWSGk