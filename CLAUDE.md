# CLAUDE.md

## Descripción del proyecto

Este proyecto es una aplicación web académica desarrollada con Node.js y TypeScript. Su propósito es funcionar como un asistente académico que permite consultar información relacionada con estudiantes y calificaciones.

El proyecto forma parte de un ejercicio académico de Ingeniería de Software con IA. La aplicación debe mantenerse funcional mientras se incorporan nuevas funcionalidades relacionadas con el uso de inteligencia artificial.

## Tecnologías principales

- Node.js
- TypeScript
- Express
- HTML, CSS y JavaScript para la interfaz
- npm
- Git y GitHub

## Estructura general

- `index.ts`: lógica principal de la aplicación.
- `public/`: archivos relacionados con la interfaz web.
- `package.json`: dependencias y scripts del proyecto.
- `package-lock.json`: versiones exactas de las dependencias instaladas.
- `tsconfig.json`: configuración de TypeScript.
- `CLAUDE.md`: instrucciones y contexto del proyecto.
- `bitacora.md`: registro del trabajo realizado durante el proyecto.

## Convenciones de código

- Mantener el código organizado y fácil de leer.
- Utilizar nombres descriptivos para variables y funciones.
- Evitar duplicar lógica cuando pueda reutilizarse.
- Mantener las funciones con responsabilidades claras.
- No realizar cambios innecesarios en funcionalidades existentes.
- Mantener compatibilidad con TypeScript y la configuración actual del proyecto.
- Comentar únicamente cuando el comentario ayude a comprender una decisión técnica.

## Pruebas

Antes de considerar terminada una modificación se deben ejecutar las pruebas disponibles del proyecto.

Comandos principales:

```bash
npm install
npm run build
npm test