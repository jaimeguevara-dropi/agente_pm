# Reglas del Sistema de Prototipado TO-BE para SILIN

Este documento define los principios, restricciones y flujos de trabajo para la construcción de prototipos interactivos en React orientados a validar el estado futuro (TO-BE) de SILIN, específicamente para el proyecto de **Procesamiento inteligente FT**.

## 1. Objetivo del Prototipado

- **Validación Ágil:** Convertir *Capabilities* y *Historias de Usuario (HUs)* del TO-BE en prototipos navegables construidos directamente en React.
- **Realismo Técnico:** Usar componentes reales del repositorio (`silin_frontend_components`) antes de proponer componentes nuevos, garantizando que lo que se diseña es viable de construir rápidamente.
- **Foco en Decisión:** Construir prototipos aprobables para validar flujos de usuario, interacciones y arquitectura de información; no pantallas finales listas para producción.

## 2. Principios de Diseño para SILIN

- **Trazabilidad y Claridad Operativa:** El usuario siempre debe saber qué está mirando, de dónde viene la información y cuál es el estado técnico y de negocio.
- **Estados Visibles y Comprensibles:** Uso intensivo de *badges*, alertas y retroalimentación visual para distinguir lo válido, lo inválido y lo procesado.
- **Errores Accionables:** Si algo falla o es inválido, el sistema debe exponer claramente *por qué* y *qué se debe hacer*.
- **Consistencia:** Mantener uniformidad visual y funcional entre tablas, filtros, vistas de resumen y paneles de detalle.
- **Lenguaje Claro:** Utilizar terminología adecuada para los diferentes perfiles que operan el sistema (tributaria, soporte y producto).
- **Funcionalidad sobre Estética:** Reutilizar elementos estándar antes de aplicar creatividad visual innecesaria que no aporte valor al negocio.

## 3. Reglas de Reutilización de Componentes

- **Prioridad #1:** Primero reutilizar componentes existentes catalogados en el repositorio base.
- **Prioridad #2:** Si no existe un componente exacto, intentar componer la solución combinando componentes existentes (ej. usar `Paper` + `Typography` + `TableEnhanced` para simular una tarjeta de detalles complejos).
- **Prioridad #3 (Excepción):** Solo proponer un componente nuevo si la necesidad no se resuelve bien con la reutilización o composición.
- **Documentación de Nuevos Componentes:** Cada vez que se proponga un componente nuevo, la propuesta debe documentar estrictamente:
  - **Nombre propuesto:** (ej. `DragAndDropZone`)
  - **Propósito:** (ej. Permitir la carga visual del archivo FT original)
  - **Props mínimas:** (ej. `onUpload`, `acceptedFormats`)
  - **Estados:** (ej. `idle`, `dragging`, `uploading`, `success`, `error`)
  - **Justificación:** (Por qué los componentes actuales no son suficientes)

## 4. Reglas de Mock Data

- **Contexto de Dominio:** Usar nombres y estados realistas del dominio de SILIN y del negocio tributario.
- **Coherencia de Datos:** Emplear entidades, periodos, lotes, comercializadoras y estados coherentes exclusivamente con el proyecto FT.
- **Variabilidad Realista:** Los datos falsos deben incluir escenarios reales: registros *válidos*, *inválidos*, *rechazados*, *disponibilizados* y *procesados parcialmente*.
- **Cero Datos Genéricos:** Queda estrictamente prohibido usar datos absurdos o de relleno ("Lorem ipsum", "Test 1", "John Doe") que carezcan de sentido operativo.

## 5. Reglas de Construcción

- **Aislamiento Total:** Construir siempre en una "zona aislada" o carpeta específica de prototipos (`/prototypes`, `/playground`, etc.).
- **Seguridad Productiva:** No tocar bajo ninguna circunstancia pantallas, flujos o rutas productivas existentes en una primera fase.
- **Preservación de Rutas:** No romper ni modificar el enrutamiento (`react-router` o similar) del aplicativo principal.
- **Inmutabilidad Base:** No modificar componentes base de `ui-components` sin aprobación explícita del usuario.
- **Aprobación Previa:** Primero proponer la experiencia y estructura (por texto/conversación); solo proceder a codificar tras obtener validación.

## 6. Relación con Figma

- **Código como Fuente de Verdad:** Figma *no* es la fuente principal para el diseño TO-BE en SILIN.
- **Prototipado en Código:** La fuente principal es React + los componentes reales + este contexto canónico.
- **Salida Opcional:** Figma puede ser utilizado como una salida opcional o como un espejo visual *posterior* a la validación del prototipo funcional, si el equipo de diseño lo requiere.

## 7. Relación con el Canon

- **Separación de Responsabilidades:** El prototipado en código no actualiza automáticamente los documentos canónicos de TO-BE, Capabilities ni HUs.
- **Promoción a Canon:** Cuando un prototipo sea validado y aprobado formalmente, su diseño y decisiones técnicas pueden guardarse como un *Prototype TO-BE canónico*.
- **Trazabilidad Inversa:** Toda propuesta de prototipo debe relacionarse, mencionar y estar diseñada para resolver una *Capability* y *HUs* específicas documentadas en el canon.

## 8. Flujo Conversacional Recomendado

Para solicitar y construir un nuevo prototipo, se debe seguir estrictamente este flujo:
1. **Capability / HU Objetivo:** Definir qué se va a prototipar.
2. **Propuesta de Experiencia:** Describir verbalmente cómo funcionará el flujo.
3. **Propuesta de Pantallas:** Listar las vistas y estados involucrados.
4. **Propuesta de Componentes:** Identificar qué componentes existentes se usarán y cuáles nuevos se requieren.
5. **Propuesta de Mock Data:** Definir el set de datos realistas para el estado.
6. **Aprobación:** Esperar validación explícita del usuario.
7. **Construcción en Zona Aislada:** Codificar el prototipo usando React.
8. **Revisión:** Mostrar el resultado funcional.
9. **Canonización:** Si se aprueba, registrar el diseño técnico en el canon.
