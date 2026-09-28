from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Servidor Academico")


# =========================================================
# 1. HERRAMIENTA: consultar calificacion
# =========================================================

@mcp.tool()
def consultar_calificacion(
    estudiante_id: str,
    materia: str
) -> str:
    """Consulta una calificación académica de ejemplo."""

    calificaciones = {
        "12345": {
            "Inteligencia Artificial": 4.8,
            "Programacion": 4.6,
            "Bases de Datos": 4.7,
        },
        "67890": {
            "Inteligencia Artificial": 4.2,
            "Programacion": 4.5,
        },
    }

    estudiante = calificaciones.get(estudiante_id)

    if estudiante is None:
        return "No se encontró el estudiante."

    nota = estudiante.get(materia)

    if nota is None:
        return "No se encontró la materia solicitada."

    return f"La calificación de {materia} es {nota}."


# =========================================================
# 2. HERRAMIENTA: calcular promedio
# =========================================================

@mcp.tool()
def calcular_promedio(
    notas: list[float]
) -> float:
    """Calcula el promedio de una lista de notas."""

    if not notas:
        return 0.0

    return round(sum(notas) / len(notas), 2)


# =========================================================
# 3. HERRAMIENTA: validar estudiante
# =========================================================

@mcp.tool()
def validar_estudiante(
    estudiante_id: str
) -> dict:
    """Valida si un estudiante existe en la base de ejemplo."""

    estudiantes = {
        "12345": "Estudiante 1",
        "67890": "Estudiante 2",
    }

    if estudiante_id in estudiantes:
        return {
            "valido": True,
            "estudiante_id": estudiante_id,
            "mensaje": "El estudiante existe."
        }

    return {
        "valido": False,
        "estudiante_id": estudiante_id,
        "mensaje": "El estudiante no existe."
    }


# =========================================================
# 4. RECURSO MCP
# =========================================================

@mcp.resource("academico://reglas")
def reglas_academicas() -> str:
    """Reglas generales del sistema académico."""

    return """
Reglas académicas:

1. Las calificaciones pertenecen al estudiante correspondiente.
2. No se deben inventar calificaciones.
3. El promedio se calcula usando las notas disponibles.
4. No se deben revelar datos privados de otros estudiantes.
5. Las herramientas deben utilizarse para consultar información
   estructurada del sistema.
"""


# =========================================================
# 5. PROMPT MCP
# =========================================================

@mcp.prompt()
def analizar_rendimiento() -> str:
    """Prompt para analizar el rendimiento académico."""

    return """
Analiza el rendimiento académico del estudiante utilizando
la información disponible.

Explica:
- Las materias consultadas.
- Las calificaciones disponibles.
- El promedio.
- Una observación general sobre los resultados.

No inventes información que no esté disponible.
"""


# =========================================================
# 6. EJECUCIÓN DEL SERVIDOR
# =========================================================

if __name__ == "__main__":
    mcp.run()