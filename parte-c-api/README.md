# Parte C - Aplicación con Claude API

## Descripción

Esta parte contiene la preparación de una aplicación de apoyo para estudiantes de Ingeniería de Software.

La aplicación contempla:

- System prompt.
- Historial de conversación.
- Respuestas estructuradas.
- Dos herramientas definidas por el estudiante.
- Validación básica.
- Uso de variables de entorno para la API key.
- Manejo del caso en que no exista una API key.

## Seguridad

La clave de API no debe escribirse directamente en el código ni subirse al repositorio.

La aplicación espera la variable:

`ANTHROPIC_API_KEY`

El archivo `.env.example` solamente contiene el nombre de la variable y un valor de ejemplo.

## Ejecución local

Se puede ejecutar la demostración local con:

```bash
python app.py