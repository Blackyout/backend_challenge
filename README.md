# Desafío: Microservicio Django + Postgres

Este proyecto es una API RESTful lista para producción construida con **Django** y **Django REST Framework**. Permite la gestión de **Personas** y **Productos**, siguiendo las mejores prácticas de la industria: contenedorización con Docker, configuración de 12-factor app, logs estructurados y documentación automática.

## 📋 Características

*   **API REST:** Endpoints CRUD completos para `Persons` y `Products`.
*   **Base de Datos:** Persistencia en PostgreSQL (conectado a Render).
*   **Filtros Avanzados:** Búsqueda, filtrado por rangos (precios), ordenamiento y paginación.
*   **Docker:** `Dockerfile` multi-stage optimizado y `docker-compose` para orquestación.
*   **Producción:** Servidor WSGI Gunicorn, gestión de archivos estáticos con WhiteNoise y cabeceras de seguridad.
*   **Observabilidad:** Logs en formato JSON y Health Checks (`/healthz`, `/readyz`).
*   **Documentación:** Swagger/OpenAPI auto-generado.

## 🛠 Tech Stack

*   **Lenguaje:** Python 3.11+
*   **Framework:** Django 4.2+, Django REST Framework
*   **Base de Datos:** PostgreSQL
*   **Servidor:** Gunicorn
*   **Infraestructura:** Docker, Docker Compose, AWS EC2 (Deploy target)

---

## 🚀 Guía de Inicio Rápido

### Prerrequisitos

*   [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/) instalados.
*   (Opcional) Python 3.11 si deseas ejecutarlo localmente sin Docker.

### 1. Configuración de Variables de Entorno

El proyecto utiliza `django-environ`. Debes crear un archivo `.env` en la raíz del proyecto.

```bash
cp .env.example .env
