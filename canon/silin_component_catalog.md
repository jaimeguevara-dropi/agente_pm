# Catálogo de Componentes Frontend - SILIN

Este documento contiene el inventario de componentes reutilizables detectados en el repositorio `silin_frontend_components`, agrupados por categoría, así como recomendaciones de componentes faltantes necesarios para la construcción de los prototipos del TO-BE de **Procesamiento inteligente FT**.

## 1. Inventario de Componentes Existentes (ui-components/material-ui)

### Layout
- `Paper`
- `Typography`

### Tablas
- `TableEnhanced`
- `TablePagination`

### Formularios
- `Autocomplete`
- `Button`
- `CheckBox`
- `CustomButton`
- `CustomMenuButtons`
- `SplitButton`
- `Input`
- `Select`
- `Switch`
- `DatePicker`
- `DateFinder`
- `DisableCopyAndPaste`

### Filtros
- `SearchBar`
- `DateFinder`
- `InitialSearchView`

### Modales
- `CommonModal`
- `Modal` (Incluye `ModalHeader` y `ModalFooter`)
- `ModalAlert`
- `ModalDialog`

### Badges / Estados
- `Badge`
- `Chip`
- `Avatar`
- `Tooltip`
- `Icon`
- `IconButton`
- `IconDownloadButton`

### Navegación
- `List`
- `ListItem`
- `MenuList`
- `Tabs` (Incluye `Tab`)

### Feedback / Alerts
- `Alert`
- `CustomSnackbar`
- `NotificationWrapper`
- `FeedbackView`
- `EmptyStateView`
- `NoDataView`
- `NotFoundView`
- `PageUnderConstruction`
- `ServerErrorView`
- `GatewayTimeoutView`
- `LinearLoading`
- `LinearProgress`
- `LoaderSpinner`
- `ProgressBar`
- `SilinLoader`

### Cards / Summaries
- *(No se detectaron componentes específicos de Cards abstractos más allá de `Paper`)*

---

## 2. Páginas o Módulos de Referencia

A través del archivo de registro del microfrontend (`jikkosoft-commons-taxpayer-app.tsx`), se identificaron varias "Vistas" (Views) exportadas que sirven como referencias visuales y funcionales para la gestión de estados globales y contenedores de páginas:

- **Estados Vacíos o Iniciales**: `EmptyStateView`, `InitialSearchView`, `NoDataView`
- **Estados de Error**: `NotFoundView`, `ServerErrorView`, `GatewayTimeoutView`
- **Feedback Genérico**: `FeedbackView`
- **Páginas de Construcción**: `PageUnderConstruction`

Estas vistas pueden reutilizarse para manejar escenarios del TO-BE como la ausencia de registros inválidos, errores de conexión en la validación estructural o la espera durante el procesamiento masivo de lotes.

---

## 3. Componentes Faltantes Recomendados para Prototipos TO-BE

Dado el TO-BE de **Procesamiento inteligente y parcial de archivos FT**, donde se requiere ingestar archivos, mapear columnas, evaluar reglas por registro y visualizar estados parciales (válidos vs. inválidos), se recomienda desarrollar o importar los siguientes componentes para los prototipos:

### Gestión de Archivos y Carga (Upload)
- **`DragAndDropZone`**: Para arrastrar y soltar el archivo FT inicial.
- **`FileUploader`**: Componente visual que muestre progreso de subida y estado del archivo en el lote.

### Dashboards y Summaries (Resumen de Lote)
- **`SummaryCard` / `StatCard`**: Tarjetas de resumen que indiquen la cantidad total de registros, válidos, inválidos y pendientes.
- **`DonutChart` / `ProgressBar` avanzada**: Para visualizar gráficamente la proporción de éxito/error del procesamiento parcial.

### Mapeo y Homologación (Layout Complejo)
- **`Stepper` / `Wizard`**: Para guiar al usuario en flujos donde se deba configurar el lote o realizar acciones en múltiples pasos.
- **`MappingTable` / `ColumnMatcher`**: Una variante de tabla o listado interactivo (drag-and-drop rows o selects emparejados) para homologar la estructura de archivos si aplica funcionalidad dinámica.

### Interacciones de Registros y Errores
- **`Drawer` / `SidePanel`**: Un panel lateral para ver el detalle de un "Registro Inválido" y su motivo de rechazo (campo afectado, tipo de error) sin perder el contexto de la tabla principal.
- **`Accordion` / `ExpandableRow`**: Para agrupar tipos de errores o mostrar detalles técnicos dentro de `TableEnhanced`.

### Visualización de Trazabilidad
- **`Timeline`**: Para mostrar el ciclo de vida del lote desde que se recibe, se valida estructuralmente, hasta la disponibilización (dispersión) y el cierre o rescate.
