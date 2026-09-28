# Plan de implementación – Nueva funcionalidad académica

## 1. Objetivo

Agregar al asistente académico una funcionalidad que permita generar un resumen de las calificaciones del estudiante autenticado.

El resumen deberá mostrar las materias disponibles y calcular el promedio académico utilizando únicamente las calificaciones autorizadas para ese estudiante.

La funcionalidad debe integrarse con el proyecto existente sin eliminar las funcionalidades actuales.

---

## 2. Situación actual

El proyecto actualmente:

- utiliza TypeScript y Node.js;
- utiliza Express para el servidor;
- contiene una base de datos simulada de calificaciones;
- permite consultar una calificación;
- posee protección básica contra prompt injection;
- tiene una interfaz web;
- utiliza respuestas progresivas;
- tiene una herramienta definida mediante el SDK de AI.

Sin embargo:

- no existen pruebas automatizadas configuradas;
- el script `npm test` todavía no ejecuta pruebas;
- la nueva funcionalidad de resumen académico todavía no existe;
- el historial del endpoint `/chat` no se conserva entre solicitudes;
- algunas funcionalidades relacionadas con IA están preparadas en el código, pero no están conectadas a una llamada real a un modelo.

---

## 3. Nueva funcionalidad

Se agregará una función:

`obtenerResumenAcademico(estudianteId)`

Esta función deberá:

1. Buscar al estudiante.
2. Verificar que exista.
3. Obtener sus calificaciones.
4. Calcular el promedio.
5. Devolver una estructura organizada con:
   - estudiante;
   - materias;
   - calificaciones;
   - promedio.

---

## 4. Validaciones

La función deberá manejar:

### Estudiante existente

Debe devolver correctamente sus materias y promedio.

### Estudiante inexistente

Debe devolver un resultado controlado indicando que no existe información autorizada.

### Estudiante sin materias

No se debe producir una división entre cero.

### Calificaciones

Las calificaciones deberán utilizar los datos existentes y no inventar valores.

---

## 5. Seguridad

La nueva funcionalidad deberá conservar el guardrail existente contra prompt injection.

También deberá evitar que un estudiante consulte información académica de otro estudiante.

El identificador del estudiante deberá utilizarse como dato de autorización y no únicamente como información proporcionada dentro de la pregunta.

---

## 6. Integración con el asistente

El endpoint `/chat` deberá reconocer solicitudes relacionadas con:

- promedio;
- resumen académico;
- materias;
- calificaciones generales.

Cuando corresponda, deberá utilizar la nueva función de resumen.

Las consultas normales que no correspondan al resumen deberán continuar funcionando.

---

## 7. Pruebas automatizadas

Se crearán pruebas para comprobar como mínimo:

1. estudiante existente;
2. cálculo correcto del promedio;
3. estudiante inexistente;
4. estudiante sin información;
5. protección de datos;
6. detección de prompt injection;
7. consulta de una calificación existente;
8. consulta de una calificación inexistente.

---

## 8. Cambios previstos

Archivos que podrían modificarse:

- `index.ts`
- `package.json`

Archivos nuevos:

- `tests/academico.test.ts`

Opcionalmente se podrán agregar funciones auxiliares en archivos separados si ayudan a mantener el código organizado.

---

## 9. Scripts de pruebas

Se configurará `package.json` para permitir ejecutar las pruebas mediante:

`npm test`

El comando deberá finalizar correctamente cuando todas las pruebas pasen.

---

## 10. Compatibilidad

La nueva funcionalidad no debe eliminar:

- el endpoint `/chat`;
- la interfaz web;
- la consulta individual de calificaciones;
- el guardrail de seguridad;
- el comportamiento de respuestas progresivas.

---

## 11. Criterios de aceptación

La funcionalidad se considerará terminada cuando:

- el resumen académico funcione;
- el promedio sea calculado correctamente;
- no se expongan datos de otro estudiante;
- las entradas inválidas sean controladas;
- las pruebas automatizadas pasen;
- las funcionalidades existentes continúen funcionando;
- exista un commit descriptivo del cambio.

---

## 12. Revisión del plan

Antes de programar se debe revisar este plan y verificar que:

- la funcionalidad propuesta es compatible con el proyecto;
- los cambios están limitados al objetivo;
- las pruebas cubren los casos principales;
- no se introducen credenciales o información sensible;
- no se eliminan funcionalidades existentes.

### Observación sobre el acceso a Claude Code

Este plan se ha preparado manualmente debido a que actualmente no se dispone de acceso autorizado a Claude Code.

Cuando se obtenga acceso, el plan deberá ser revisado con Claude Code como parte del flujo académico solicitado:

Explorar → Planificar → Programar → Commit.