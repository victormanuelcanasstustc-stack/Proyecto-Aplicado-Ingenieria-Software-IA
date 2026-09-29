Proyecto Aplicado -- Ingeniería de Software con IA
Descripción
Este repositorio contiene el desarrollo del Proyecto Aplicado de
Ingeniería de Software con IA. El proyecto integra documentación de
Claude Code, una aplicación Python preparada para Claude API y un
servidor propio basado en Model Context Protocol (MCP).
Estructura
/
├── CLAUDE.md
├── bitacora.md
├── plan.md
├── index.ts
├── public/
├── src/
│   └── academico.ts
├── tests/
│   └── academico.test.ts
├── parte-c-api/
│   ├── README.md
│   ├── app.py
│   ├── evaluacion.md
│   └── .env.example
├── parte-d-mcp/
│   ├── README.md
│   ├── server.py
│   └── requirements.txt
├── certificados/
├── evidencias/
└── informe.pdf
Parte B -- Claude Code
La Parte B documenta el flujo:
Explorar → Planificar → Programar → Probar → Revisar → Commit
CLAUDE.md contiene el contexto, las convenciones, los comandos de
prueba y las restricciones del proyecto.
bitacora.md registra decisiones, propuestas, limitaciones y
actividades relevantes.
Importante
Durante el desarrollo no se contó con acceso autorizado a Claude Code.
Por integridad académica, no se presentan como reales interacciones del
agente que no hayan ocurrido. La preparación técnica y los cambios
locales sí se documentan.
Parte C -- Claude API
La carpeta parte-c-api/ contiene:
- system prompt para un asistente académico;
- historial multi-turno;
- respuesta estructurada en JSON;
- dos herramientas definidas por el estudiante;
- validaciones locales;
- .env.example para configurar ANTHROPIC_API_KEY;
- conjunto de evaluación de 10 casos.
La llamada real a Claude requiere una API key autorizada. No se incluye
ninguna clave en el repositorio.
Ejecutar la demostración local:
cd parte-c-api
python app.py
Parte D -- MCP
La carpeta parte-d-mcp/ contiene un servidor MCP en Python.
Herramientas
1. consultar_calificacion
2. calcular_promedio
3. validar_estudiante
Recurso
academico://reglas
Prompt
analizar_rendimiento
Instalación:
python -m pip install -r parte-d-mcp/requirements.txt
Comprobación de sintaxis:
python -m py_compile parte-d-mcp/server.py
Ejecución:
python parte-d-mcp/server.py
Para la validación con MCP Inspector se deben conservar capturas reales
en evidencias/.
Pruebas del proyecto base
Las pruebas del resumen académico se ejecutan con:
npm test
La prueba valida estudiantes existentes, materias, promedio y estudiante
inexistente.
Seguridad
- No subir claves API.
- No subir archivos .env.
- No incluir node_modules en Git.
- No utilizar datos académicos reales.
- Validar entradas y respuestas.
- No inventar resultados de API o herramientas.
Evidencias
Las capturas deben corresponder a ejecuciones reales. Se recomienda
organizar:
evidencias/
├── claude-code/
├── api/
└── mcp/
Estado de la entrega
El proyecto está preparado y documentado. Las actividades que requieren
acceso externo a Claude Code o a la API quedan identificadas como
pendientes cuando no pueden ejecutarse.
Informe técnico
El informe técnico completo se encuentra en informe.pdf y describe la
arquitectura, metodología, implementación, pruebas, limitaciones,
lecciones aprendidas y preguntas conceptuales.