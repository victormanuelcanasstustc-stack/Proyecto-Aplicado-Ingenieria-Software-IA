import json
import os
from typing import Any


SYSTEM_PROMPT = """
Eres un asistente de apoyo para un estudiante de Ingeniería de Software.

Tus funciones principales son:
1. Ayudar a comprender conceptos de programación y software.
2. Explicar errores técnicos de manera clara.
3. Proponer soluciones razonadas sin inventar información.
4. Respetar la privacidad y no solicitar claves, contraseñas ni información sensible.
5. Cuando se solicite una respuesta estructurada, devolver únicamente el formato solicitado.
"""


class AsistenteAcademico:
    def __init__(self) -> None:
        self.history: list[dict[str, str]] = []

    def agregar_mensaje(self, role: str, content: str) -> None:
        self.history.append({
            "role": role,
            "content": content
        })

    def obtener_historial(self) -> list[dict[str, str]]:
        return self.history.copy()


def respuesta_json(
    concepto: str,
    explicacion: str,
    recomendacion: str
) -> dict[str, str]:
    """
    Genera una estructura JSON validable para una respuesta académica.
    """
    resultado: dict[str, str] = {
        "concepto": concepto,
        "explicacion": explicacion,
        "recomendacion": recomendacion
    }

    # Validación básica del esquema.
    required = {"concepto", "explicacion", "recomendacion"}

    if set(resultado.keys()) != required:
        raise ValueError("La respuesta no cumple el esquema requerido.")

    return resultado


def herramienta_buscar_archivo(nombre: str) -> dict[str, Any]:
    """
    Herramienta definida por el estudiante.
    Simula la consulta de un archivo local.
    """
    if not nombre.strip():
        return {
            "encontrado": False,
            "mensaje": "Debe proporcionar un nombre de archivo."
        }

    return {
        "encontrado": True,
        "archivo": nombre,
        "mensaje": "Consulta local preparada correctamente."
    }


def herramienta_resumir_codigo(codigo: str) -> dict[str, Any]:
    """
    Segunda herramienta definida por el estudiante.
    Analiza de manera básica un fragmento de código.
    """
    if not codigo.strip():
        return {
            "valido": False,
            "mensaje": "No se proporcionó código."
        }

    return {
        "valido": True,
        "longitud": len(codigo),
        "mensaje": "Código recibido para análisis."
    }


def verificar_configuracion() -> bool:
    """
    Comprueba que exista la variable de entorno requerida.
    No muestra ni imprime la clave.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        return False

    return True


def demostracion_local() -> None:
    """
    Demostración que puede ejecutarse sin una llamada real a Claude.
    """
    asistente = AsistenteAcademico()

    asistente.agregar_mensaje(
        "user",
        "¿Qué diferencia existe entre una función y una clase?"
    )

    asistente.agregar_mensaje(
        "assistant",
        "Una función realiza una tarea; una clase define una estructura "
        "que puede contener datos y comportamientos."
    )

    resultado = respuesta_json(
        "Función vs clase",
        "Una función encapsula una operación. Una clase permite modelar "
        "objetos con atributos y métodos.",
        "Usar funciones para operaciones concretas y clases cuando se "
        "necesite modelar entidades con estado y comportamiento."
    )

    print("=== DEMOSTRACIÓN LOCAL ===")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    print()
    print("Historial:")
    print(json.dumps(asistente.obtener_historial(), indent=2, ensure_ascii=False))

    print()
    print("Herramienta 1:")
    print(json.dumps(
        herramienta_buscar_archivo("index.ts"),
        indent=2,
        ensure_ascii=False
    ))

    print()
    print("Herramienta 2:")
    print(json.dumps(
        herramienta_resumir_codigo("const suma = (a, b) => a + b;"),
        indent=2,
        ensure_ascii=False
    ))

    print()
    if verificar_configuracion():
        print("ANTHROPIC_API_KEY configurada.")
    else:
        print(
            "ANTHROPIC_API_KEY no configurada. "
            "La llamada real a Claude queda pendiente."
        )


if __name__ == "__main__":
    demostracion_local()