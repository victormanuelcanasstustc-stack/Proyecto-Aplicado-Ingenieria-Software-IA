export type Calificaciones = Record<string, number>;

export type ResumenAcademico = {
  estudianteId: string;
  materias: Calificaciones;
  promedio: number;
};

export function obtenerResumenAcademico(
  estudianteId: string,
  calificaciones: Record<string, Calificaciones>
): ResumenAcademico | null {
  const estudiante = calificaciones[estudianteId];

  if (!estudiante) {
    return null;
  }

  const notas = Object.values(estudiante);

  if (notas.length === 0) {
    return {
      estudianteId,
      materias: {},
      promedio: 0
    };
  }

  const suma = notas.reduce(
    (total, nota) => total + nota,
    0
  );

  const promedio = Number(
    (suma / notas.length).toFixed(2)
  );

  return {
    estudianteId,
    materias: estudiante,
    promedio
  };
}