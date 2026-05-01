# Business Context - SILIN

## Nombre del producto
SILIN

## Qué es SILIN
SILIN no es solo un sistema para emitir facturas, sino un ecosistema tributario orientado a soportar el ciclo de vida del ingreso público de una entidad territorial. Su propósito es conectar, en una sola plataforma, los procesos necesarios para administrar obligaciones tributarias, generar documentos de cobro, recaudar pagos, aplicar esos pagos correctamente, consultar cartera, gestionar actos administrativos y habilitar la atención digital al contribuyente.

En términos ejecutivos, SILIN es una plataforma integral de administración tributaria para entidades territoriales que centraliza facturación, recaudo, cartera, expedientes y atención digital al contribuyente, conectando procesos normativos, financieros y operativos en un solo ecosistema.

## Propósito del producto
El propósito de SILIN es permitir que una entidad pública gestione de forma más ordenada, trazable, escalable y sostenible sus procesos tributarios, reduciendo dependencias de operación manual, mejorando el control sobre el ingreso público y fortaleciendo el servicio prestado al ciudadano.

SILIN busca convertirse en el núcleo operativo y transaccional desde el cual se articulan los principales procesos de gestión tributaria de la entidad, incluyendo liquidación, facturación, recaudo, cartera, fiscalización, determinación, cobro coactivo, consulta documental y relación digital con el contribuyente.

## Qué hace SILIN
A nivel funcional, SILIN permite que la entidad:

- gestione obligaciones tributarias y estado de cuenta,
- genere facturas y documentos de cobro,
- descargue reportes de liquidaciones oficiales,
- aplique pagos provenientes de múltiples canales,
- publique facturas y actos administrativos en un portal digital,
- organice información de cartera y cuentas por cobrar,
- habilite consulta por parte del ciudadano sobre sus obligaciones y documentos,
- soporte procesos relacionados con expedientes, notificaciones, recaudo y seguimiento tributario.

En pagos, la lógica del sistema contempla recaudos que llegan por múltiples canales, incluyendo Asobancaria, transferencias, consignaciones, pasarelas de pago, bancos y formatos especiales como FT-03. Esa lógica se aplica sobre distintos tipos de documentos, incluyendo facturas regulares, facturas a demanda, facturas liquidatorias y liquidaciones oficiales, buscando que el pago quede correctamente confirmado, registrado y reflejado en las cuentas por cobrar.

## Enfoque funcional de SILIN
El enfoque de SILIN es tributario, transaccional, documental y de servicio al ciudadano.

### Enfoque tributario
SILIN está construido alrededor de conceptos propios de la gestión tributaria pública, como:

- tributo,
- base gravable,
- liquidación,
- facturación,
- cartera,
- cobro coactivo,
- calendario tributario,
- actos administrativos,
- contribuyente,
- fiscalización,
- determinación,
- recaudo.

No es un producto genérico de billing ni un ERP tradicional; su lógica gira alrededor de la operación tributaria de entidades públicas y de las particularidades normativas y procedimentales de ese dominio.

### Enfoque transaccional
SILIN conecta procesos como facturación, recaudo, aplicación de pagos, cartera y pasarelas de pago para que el ciclo financiero quede consistente de extremo a extremo. La plataforma busca que lo que se factura, lo que se recauda y lo que se refleja en cartera mantenga trazabilidad, consistencia y capacidad de auditoría.

### Enfoque documental y procedimental
SILIN también opera como soporte para la gestión de documentos y actuaciones administrativas relevantes dentro del ciclo tributario. Por eso el acceso a facturas, liquidaciones oficiales, actos administrativos y expedientes forma parte del ecosistema funcional y no de una capacidad aislada.

### Enfoque de servicio al ciudadano
A través del Portal Contribuyentes, SILIN permite autenticarse, consultar facturas pendientes, filtrar información por tributo o identificadores como medidor, lote o NIT, y descargar tanto facturas como actos administrativos en PDF. Esto convierte a SILIN no solo en una plataforma interna para la entidad, sino también en un punto de contacto digital con el ciudadano.

## Usuarios y actores principales
SILIN sirve a varios tipos de actores dentro del ecosistema tributario:

### Usuarios institucionales
- equipos de hacienda y administración tributaria,
- equipos de facturación,
- equipos de recaudo,
- equipos de cartera,
- equipos de fiscalización y determinación,
- equipos de cobro coactivo,
- equipos de soporte y operación,
- usuarios encargados de parametrización y administración funcional.

### Usuarios externos
- contribuyentes,
- ciudadanos,
- empresas,
- terceros integrados al proceso de recaudo o intercambio de información,
- operadores o proveedores relacionados con pagos, recaudo o sistemas complementarios.

## Tributos y realidades que soporta
Con la documentación y el trabajo realizado, SILIN está pensado para soportar diferentes tributos y contextos territoriales. Entre los tributos y casos visibles en el contexto actual se encuentran:

- Predial
- ICA
- Alumbrado Público

Además del tributo en sí, SILIN contempla procesos asociados como:

- liquidación,
- facturación,
- recaudo,
- aplicación de pagos,
- cartera,
- fiscalización,
- determinación,
- cobro coactivo,
- consulta de estado de cuenta,
- gestión y publicación documental,
- parametrización por entidad.

Esto sugiere que la plataforma está diseñada para operar en escenarios multitributo y multientidad, con diferencias normativas, operativas y de parametrización entre clientes.

## Capacidades funcionales visibles en el ecosistema SILIN
Dentro del contexto actual, SILIN se relaciona con capacidades y frentes como:

- Facturación
- Recaudo
- Cartera
- Expedientes
- Acuerdos de Pago
- Integraciones
- Portales
- Parametrización de entidades
- Gestión documental y actos administrativos
- Atención digital al contribuyente
- Soporte operativo
- Migración e incorporación de información desde legados

Estas capacidades no necesariamente están resueltas de forma homogénea ni con el mismo nivel de madurez, pero sí forman parte del alcance del ecosistema producto.

## Naturaleza del producto
SILIN debe entenderse como una plataforma de producto con fuerte componente de implementación. Esto significa que su valor no está solo en el software base, sino también en:

- la parametrización por entidad,
- la adaptación a tributos específicos,
- la integración con sistemas externos,
- la migración desde legados,
- el acompañamiento operativo,
- la evolución funcional continua.

Por esa razón, SILIN convive simultáneamente con lógica de producto, lógica contractual, necesidades de implementación y exigencias operativas de clientes reales.

## Arquitectura y enfoque tecnológico
En el contexto conocido, SILIN opera bajo una arquitectura moderna basada en microservicios desplegados en AWS, con componentes backend en Go, Python y Java. También se ha mencionado el uso de BPMN con Camunda, así como herramientas y prácticas asociadas a infraestructura y operación como Terraform, Docker, Azure DevOps y diversos servicios de monitoreo y seguridad en la nube.

Desde el punto de vista tecnológico, esto sugiere que SILIN no está concebido como una solución monolítica simple, sino como un ecosistema con múltiples componentes especializados, integraciones y responsabilidades distribuidas.

Adicionalmente, dentro de la visión del producto se espera que esta arquitectura siga evolucionando hacia un diseño más desacoplado, más robusto y mejor alineado con capacidades de negocio claramente delimitadas.

## Uso de datos e inteligencia
SILIN ya se ha relacionado con capacidades de datos e inteligencia artificial para fines como:

- análisis de datos tributarios,
- detección de morosos,
- predicción de comportamiento,
- apoyo a decisiones operativas,
- fortalecimiento de procesos de control y lucha contra la corrupción.

Esto indica que la plataforma no solo tiene un componente transaccional, sino también una aspiración analítica y predictiva, donde los datos operativos pueden convertirse en insumo para priorización, seguimiento, análisis de cartera y toma de decisiones institucionales.

## Valor que entrega a la entidad
SILIN entrega valor a las entidades al permitir:

- centralizar procesos tributarios que suelen estar fragmentados,
- reducir dependencia de sistemas legados dispersos,
- mejorar trazabilidad entre facturación, recaudo y cartera,
- facilitar el acceso digital del contribuyente a su información,
- estandarizar parte de la operación tributaria,
- soportar el crecimiento funcional y normativo de la entidad,
- crear bases para automatización y escalabilidad futura.

## Valor que entrega al contribuyente
Para el contribuyente, SILIN aporta principalmente:

- acceso digital a obligaciones y documentos,
- consulta de facturas y actos administrativos,
- facilidad para ubicar documentos por diferentes identificadores,
- mayor claridad sobre estado de cuenta y obligaciones,
- interacción más directa con el ecosistema tributario digital de la entidad.

## Retos estructurales observados alrededor de SILIN
En el contexto trabajado hasta ahora, alrededor de SILIN aparecen retos como:

- deuda técnica,
- presión operativa y contractual,
- coexistencia entre implementación y evolución de producto,
- necesidad de una visión más unificada del roadmap,
- complejidad de integraciones con terceros,
- dificultades de migración desde sistemas legados,
- diferencias entre entidades y tributos,
- necesidad de automatizar parametrización y operación,
- tensiones entre resolver urgencias de delivery y construir una arquitectura sostenible.

Estos retos son parte del contexto real del producto y deben ser considerados al analizar decisiones, priorizaciones y TO-BE de proyectos relacionados con SILIN.

## Visión global de futuro de SILIN
SILIN evoluciona hacia una plataforma tributaria pública altamente automatizada, escalable e inteligente, capaz de ejecutar de extremo a extremo los procesos críticos de gestión tributaria con mínima intervención humana, reservando la participación de los usuarios únicamente para decisiones de control, validación excepcional o aprobación final cuando el proceso lo requiera.

La visión de futuro de SILIN no es solo digitalizar tareas existentes, sino transformar profundamente la operación tributaria de las entidades, eliminando dependencias manuales, reduciendo reprocesos, disminuyendo tiempos operativos y aumentando la capacidad institucional para gestionar grandes volúmenes de información de manera confiable, trazable y sostenible.

## Principios de la visión futura
En el escenario objetivo, los procesos que hoy requieren soporte humano intensivo —como validación de información, interpretación normativa, parametrización, liquidación, análisis de cartera, clasificación financiera, preparación de resultados, seguimiento operativo y atención sobre excepciones— deben migrar progresivamente a flujos automatizados, orquestados y monitoreables.

Estos flujos deben estar soportados por:

- reglas de negocio claras,
- modelos de decisión,
- componentes desacoplados,
- parametrización evolutiva,
- trazabilidad operativa,
- capacidades de inteligencia artificial donde agreguen valor real.

## Enfoque tecnológico de futuro
Desde el punto de vista tecnológico, SILIN debe consolidarse sobre una arquitectura robusta y estable, diseñada para procesar grandes cantidades de datos tributarios y transaccionales de forma eficiente, concurrente y resiliente.

La plataforma debe estar preparada para operar con:

- altos volúmenes de registros,
- múltiples entidades,
- múltiples tributos,
- variaciones normativas en el tiempo,
- alta exigencia de trazabilidad,
- necesidad de mantenibilidad y evolución continua.

La ambición no es solo soportar más carga, sino hacerlo sin comprometer desempeño, gobernabilidad, mantenibilidad ni claridad del dominio.

## Diseño empresarial objetivo
La evolución de SILIN debe alinearse con el framework BIAN, de manera que la plataforma organice su arquitectura alrededor de capacidades claras, dominios bien delimitados, servicios desacoplados y flujos interoperables.

Este enfoque busca:

- crecimiento ordenado,
- reutilización de capacidades,
- sostenibilidad arquitectónica,
- menor dependencia entre componentes,
- mayor facilidad de integración,
- una evolución funcional más controlada.

## Estado objetivo del producto
La visión final es que SILIN funcione como un núcleo transaccional y analítico moderno para la gestión tributaria pública, donde:

- la operación repetitiva y masiva esté automatizada,
- la lógica de negocio sea parametrizable y evolutiva,
- la infraestructura soporte crecimiento y complejidad,
- la intervención humana se concentre en ejercer criterio, supervisión y toma de decisiones,
- y no en ejecutar tareas manuales operativas.

En otras palabras, el futuro de SILIN es convertirse en una plataforma que permita a las entidades públicas pasar de una gestión tributaria reactiva, fragmentada y dependiente del esfuerzo humano, a una gestión proactiva, automatizada, escalable e inteligente, preparada para operar con volumen, complejidad normativa y exigencia institucional real.

## Qué significa SILIN dentro de Jikkosoft
Dentro del contexto de Jikkosoft, SILIN representa un núcleo estratégico de producto y operación. No solo concentra capacidades tributarias críticas, sino que también actúa como vehículo para:

- consolidar visión de producto,
- estructurar capacidades reutilizables,
- fortalecer implementación multientidad,
- impulsar automatización,
- habilitar canales digitales,
- y crear bases para decisiones más inteligentes apoyadas en datos.

## Criterios de éxito para SILIN
SILIN se considera exitoso cuando logra, de forma sostenible:

- reducir intervención manual en procesos críticos,
- soportar múltiples entidades y tributos con menor fricción,
- mejorar trazabilidad entre procesos financieros y operativos,
- acelerar implementación y parametrización,
- fortalecer la atención digital al contribuyente,
- operar con mayor estabilidad y menor deuda estructural,
- habilitar una evolución arquitectónica ordenada,
- convertirse en una plataforma más inteligente, automatizada y escalable.

## Notas de uso para este contexto
Este documento representa el contexto de producto de SILIN y no sustituye:
- el Business Context global de Jikkosoft,
- el AS-IS de un proyecto específico,
- el TO-BE de un proyecto específico.

Debe usarse como contexto base del producto para interpretar iniciativas, decisiones, AS-IS, TO-BE, capacidades, features y seguimientos relacionados con SILIN.
