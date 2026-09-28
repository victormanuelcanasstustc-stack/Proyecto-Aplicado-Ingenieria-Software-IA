# Parte D - Servidor MCP

## Descripción

Servidor MCP desarrollado en Python utilizando el SDK oficial de
Model Context Protocol.

El servidor proporciona herramientas y recursos relacionados con
un sistema académico de ejemplo.

## Componentes

### Herramientas

1. `consultar_calificacion`
   - Consulta la calificación de una materia.

2. `calcular_promedio`
   - Calcula el promedio de una lista de notas.

3. `validar_estudiante`
   - Comprueba si un estudiante existe.

### Recurso

`academico://reglas`

Contiene las reglas generales del sistema académico.

### Prompt

`analizar_rendimiento`

Permite solicitar un análisis del rendimiento académico utilizando
la información disponible.

## Instalación

Instalar las dependencias mediante:

```bash
python -m pip install -r requirements.txt