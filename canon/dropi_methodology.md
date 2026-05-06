# Metodología de producto — Dropi

## Jerarquía de incidencias (Jira)

```
Épica
  → Historia (UX / UI / Frontend / Backend / DBA / QA / Legal / Lanzamiento)
      → Subtarea
  → Incidencia de Producto
      → Subtarea
  → Subtarea (directa de épica)
```

---

## Siglas de producto

| Sigla | Aplica a |
|---|---|
| `DROPI` | Core de la plataforma web (lo que ven los usuarios) |
| `DROPI APP` | Proyecto DROPI APP |
| `ADMIN` | Funcionalidades administrativas |
| `CAS` | Proyecto CAS |

---

## Épica

### Formato del título
`[Sigla del producto]: [Nombre de la épica]_[País]_[Usuarios afectados]`

**Ejemplo:** `DROPI: Validación de cuentas bancarias_Colombia_Todos los usuarios`

### Descripción de la épica

**Contexto**
- Descripción del problema:
  - ¿Qué problema estamos resolviendo?
  - ¿Por qué es importante?
  - ¿A qué usuarios afecta?
  - Datos relevantes que justifiquen la solución

**¿Qué buscamos?**
- Detalle de lo que vamos a lograr
- ¿Qué vamos a hacer?
- Fases del proceso (con posibles bloqueantes y entregable esperado por fase)

**Criterios de éxito**
- Métricas a impactar
- Público objetivo (tipos de usuario, países, marcas blancas)

**Documentación**
- Kickoff (link)
- Flujo general
- Figma / FigJam
- Documentos relacionados

---

## Historia

### Formato del título
`[Etiqueta] [Sigla del producto]: [Nombre descriptivo]`

**Ejemplo:** `[UX] DROPI Informe general de productos para Dropshippers`

### Etiquetas y su contenido esperado

| Etiqueta | Contenido esperado en la historia |
|---|---|
| `UX` | Flujo de interacción, wireframes en baja, investigaciones, benchmarks, pruebas de usuarios |
| `UI` | Benchmarks visuales, diseños en alta con especificaciones para handoff, prototipos en alta |
| `Frontend` | Componentes visuales requeridos, conexión con APIs backend, endpoints |
| `Backend` | APIs necesarias, esquema de datos, procesos automatizados |
| `DBA` | Estructura de tablas, validaciones y restricciones |
| `QA` | Procesos a validar, revisión de flujos |
| `Legal` | Revisión de requerimientos, adiciones a términos y condiciones |
| `Lanzamiento` | Beneficios por tipo de usuario, video Tango de las funcionalidades |

### Descripción de la historia

**Historia (formato)**
```
Como [tipo de usuario],
Puedo [acción],
Para [resultado].
```

Tipos de usuario válidos: Dropshipper, Proveedor, Emprendedor, Marca Blanca, Seller, Administrador, Super Administrador.

**Descripción del proceso**
Detalle de cómo se realizaría el proceso: documentación, flujos, paso a paso y detalles relevantes.

**Flujo del usuario (user flow)**
Paso a paso que debe realizar el usuario para completar la tarea.
- Separado por viñetas o números
- Incluir diagrama UML si aplica

**Criterios de aceptación (formato Gherkin)**
```
Escenario: [Nombre del escenario]
  Dado que [precondición / escenario inicial]
  Cuando [acción que ejecuta el usuario]
  Entonces [resultado esperado / validación]
```

**Condiciones adicionales**
- Versión del sistema de diseño (1.0 = componentes actuales; 2.0 = sistema de diseño nuevo)
- Es nuevo o rediseño
- Resoluciones: Desktop, tablet, laptop, responsive (móvil)

**Definición de Hecho (DoD)**
Resultados esperados para cada acción o requerimiento.

---

## Subtarea

### Formato del título
`[Etiqueta] [Sigla del producto]: [Nombre descriptivo]`

**Ejemplo:** `[UX] DROPI APP Diseño del nuevo flujo de pantalla favoritos Dropi app`

### Descripción de la subtarea
Pasos a seguir para completar la tarea:
- Actividades concretas (investigaciones, benchmarking, definiciones de épica, sesiones de ideación, etc.)

---

## Incidencia de Producto

Va dentro de una épica. Agrupa actividades que desarrolla el equipo de producto para el avance de la épica.

---

## Tipos de usuarios en Dropi

- Dropshipper
- Proveedor
- Emprendedor
- Marca Blanca
- Seller
- Administrador
- Super Administrador
