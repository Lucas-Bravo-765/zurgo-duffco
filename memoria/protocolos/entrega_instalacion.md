# PROTOCOLO DE ENTREGA E INSTALACIÓN

Versión: 1.0 (Zurgo) | Fecha: 2026-11-16 | Base: protocolo de Dr. Sayin Duffco
Se lee antes de empaquetar, instalar, traspasar o mantener un agente entregado.

---

## 1. EL PAQUETE

Lo que se entrega no es un prompt: es infraestructura instalada en el computador de otra persona. Cada paquete contiene:

```
<nombre-agente>/
├── INSTRUCCION_INTERFAZ.txt     texto que se pega en Claude Desktop
├── README_USUARIO.md            guía simple para el usuario final
├── .gitignore
├── memoria/
│   ├── 00_NUCLEO.md             instrucciones del agente (bloqueadas para el agente)
│   ├── conocimiento/            conocimiento permanente con fuentes y fechas
│   ├── aprendizajes.md          único archivo que el agente puede editar
│   └── CHANGELOG.md
├── trabajo/                     documentos de sesión (excluido de git)
└── salidas/                     informes generados (excluido de git)
```

Antes de empaquetar, verifica:
- [ ] Pasó la puerta P2 (pruebas aprobadas por Lucas).
- [ ] `trabajo/` y `salidas/` vacíos (sin documentos de prueba).
- [ ] Ningún dato sensible en `memoria/`.
- [ ] Versión y fecha en el núcleo y en el changelog.
- [ ] `README_USUARIO.md` revisado con el perfil del usuario en mente.

---

## 2. REPOSITORIO DEL AGENTE

- Repositorio privado en la organización de GitHub de Duffco, con el nombre del agente en minúsculas y con guiones.
- El primer commit es la versión que pasó P2.
- Toda mantención posterior se hace en ese repositorio, con versión y changelog.

---

## 3. INSTALACIÓN (la hace Lucas, guiado por ti)

1. **Prerequisitos.** Claude Desktop instalado en el computador del usuario, sesión iniciada con su cuenta de Duffco.
2. **Copiar la carpeta** del agente a una ubicación estable del computador del usuario (ej. `Documentos/Agentes Duffco/<nombre>/`). Nunca en el Escritorio ni en Descargas.
3. **Configurar en Claude Desktop** un espacio de trabajo con esa carpeta conectada y pegar `INSTRUCCION_INTERFAZ.txt` como instrucción. Como la interfaz de Claude Desktop cambia, verifica los pasos exactos en la versión instalada.
4. **Configuración del modelo.** Extended Thinking apagado salvo que el diseño lo justifique.
5. **Prueba de humo** frente al usuario: el opener funciona, el agente lee su núcleo, procesa un documento de ejemplo y produce la salida esperada.
6. **Sesión de arranque** con el usuario (20 a 30 minutos): qué hace el agente, qué no hace, cómo cargar un documento, cómo leer la salida, qué hacer si algo falla.
7. **Registro.** Actualizar `registro_agentes.md`: estado "en producción", versión, usuario, fecha y ubicación.

---

## 4. TRASPASO

Al usuario le queda claro, por escrito en el README:
- Que el agente es un apoyo y que la decisión y la firma son siempre suyas.
- Dónde dejar los documentos y dónde encontrar las salidas.
- A quién avisar si algo no funciona (Lucas, por ahora).

---

## 5. MANTENCIÓN

- **Revisión a las 2 semanas** de la instalación: métricas reales contra la línea base, feedback del usuario, contenido de `aprendizajes.md`.
- **Cambios:** el usuario reporta, Lucas lo trae a esta carpeta, se diseña el cambio con el protocolo de auto-modificación del agente, se versiona en su repositorio y se reinstala.
- **Cambios normativos:** si cambia una norma que el agente usa, se marca el agente en `registro_agentes.md` como "requiere actualización" hasta corregirlo.
- **Retiro:** si un agente deja de usarse, se registra el motivo. Es información valiosa para el siguiente diseño.
