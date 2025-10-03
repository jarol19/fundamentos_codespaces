# fundamentos_codespaces

Este proyecto está configurado para trabajar con Python en un entorno virtual dentro de GitHub Codespaces. Incluye la extensión de Python y el paquete Streamlit para el desarrollo de aplicaciones web interactivas.

## Características principales

- Entorno virtual Python (`.venv`) configurado automáticamente.
- Streamlit instalado para crear dashboards y aplicaciones web.
- Listo para desarrollo en Codespaces.

## Cómo empezar

1. Activa el entorno virtual:
	```bash
	source .venv/bin/activate
	```
2. Instala dependencias adicionales si lo necesitas:
	```bash
	pip install <paquete>
	```
3. Ejecuta una app de Streamlit:
	```bash
	streamlit run app.py
	```

## Estructura del proyecto

- `README.md`: Documentación del proyecto.
- `.venv/`: Entorno virtual de Python.
- `app.py`: Archivo sugerido para tu aplicación Streamlit.

## Requisitos

- Python 3.12+
- GitHub Codespaces o entorno compatible con VS Code