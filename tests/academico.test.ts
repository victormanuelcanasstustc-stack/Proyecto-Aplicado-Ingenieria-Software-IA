import { obtenerResumenAcademico } from "../src/academico.js";

const calificaciones = {
  "12345": {
    "Inteligencia Artificial": 4.8,
    "Programación": 4.6,
    "Bases de Datos": 4.7
  },
  "67890": {
    "Inteligencia Artificial": 4.2,
    "Programación": 4.5
  }
};

function comprobar(
  condicion: boolean,
  mensaje: string
): void {
  if (!condicion) {
    throw new Error(`Fallo: ${mensaje}`);
  }
}

console.log("Ejecutando pruebas de resumen académico...");

// Prueba 1: estudiante existente
const resumen = obtenerResumenAcademico(
  "12345",
  calificaciones
);

comprobar(
  resumen !== null,
  "Debe encontrar al estudiante 12345"
);

// Prueba 2: materias
comprobar(
  resumen !== null &&
    Object.keys(resumen.materias).length === 3,
  "Debe devolver las tres materias"
);

// Prueba 3: promedio
comprobar(
  resumen !== null &&
    resumen.promedio === 4.7,
  "El promedio debe ser 4.7"
);

// Prueba 4: estudiante inexistente
const inexistente = obtenerResumenAcademico(
  "99999",
  calificaciones
);

comprobar(
  inexistente === null,
  "Un estudiante inexistente debe devolver null"
);

// Prueba 5: estudiante con datos diferentes
const segundo = obtenerResumenAcademico(
  "67890",
  calificaciones
);

comprobar(
  segundo !== null &&
    segundo.promedio === 4.35,
  "El promedio del segundo estudiante debe ser 4.35"
);

console.log("Todas las pruebas pasaron correctamente.");