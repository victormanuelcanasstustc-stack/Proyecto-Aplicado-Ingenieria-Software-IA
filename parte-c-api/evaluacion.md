# Evaluación de la Parte C

## Objetivo

Evaluar el comportamiento esperado de un asistente de apoyo para Ingeniería de Software mediante diferentes casos de uso.

## Casos de evaluación

| # | Caso | Resultado esperado |
|---|---|---|
| 1 | Explicar una función | Explicación clara |
| 2 | Explicar una clase | Explicación clara |
| 3 | Comparar función y clase | Comparación correcta |
| 4 | Explicar una excepción | Explicación técnica comprensible |
| 5 | Explicar una API REST | Conceptos correctos |
| 6 | Analizar un fragmento de código | Identificación de elementos relevantes |
| 7 | Solicitar formato JSON | Respuesta estructurada |
| 8 | Mantener contexto de conversación | Utilizar historial disponible |
| 9 | Buscar un archivo | Utilizar la herramienta definida |
| 10 | Resumir código | Utilizar la herramienta definida |

## Estado de ejecución

Los casos fueron preparados como conjunto de evaluación.

La ejecución real contra Claude API no pudo completarse debido a la ausencia de una clave de API disponible para el estudiante.

Por esta razón no se presentan resultados inventados como si hubieran sido obtenidos mediante una llamada real a Claude.

## Análisis

La aplicación incluye una estructura para:

- Prompt de sistema.
- Historial de conversación.
- Respuesta estructurada en JSON.
- Dos herramientas definidas por el estudiante.
- Validaciones básicas.
- Lectura de la clave mediante variable de entorno.
- Manejo del caso en que la clave no esté configurada.

Queda pendiente la integración y evaluación real mediante la API de Claude cuando se disponga de las credenciales correspondientes.