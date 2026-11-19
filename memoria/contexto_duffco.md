# CONTEXTO DUFFCO

Archivo de conocimiento permanente de Dr. Sayin Duffco (copia para Zurgo al 2026-11-16; las novedades llegan por los reportes de Santi en Sandia).
Versión: 1.4 | Fecha: 2026-11-18 | Autor: Sayin (base) + Santi (validación pendiente)

---

## 0. CÓMO USAR ESTE ARCHIVO

- Este archivo describe el negocio de Duffco y el entorno regulatorio en que opera. Es contexto, no instrucciones.
- Etiquetas de confianza, obligatorias en cada dato:
  - **[V]** Verificado contra fuente pública (ver sección 11).
  - **[P]** Por confirmar con Santi o con Duffco. No usar como hecho en un agente entregado hasta confirmarlo.
  - **[H]** Hipótesis de Sayin. Sirve para orientar preguntas, nunca para diseñar sin validación.
- Regla anti-fabricación: si un agente necesita un dato que aquí aparece como [P] o [H], el agente pregunta. No asume.
- Normativa: los textos legales cambian. Antes de embeber un requisito normativo en un agente de producción, verificar el texto vigente en la Biblioteca del Congreso (bcn.cl/leychile) o en la Biblioteca DGOP. Especial atención a las modificaciones del D.S. MOP N° 150 de 2024 al RCOP (ver sección 5).
- Actualización: cuando Santi entregue información nueva de Duffco, se actualiza este archivo siguiendo el protocolo de auto-modificación y se registra en el changelog (sección 12).

---

## 1. FICHA DE LA EMPRESA

| Campo | Dato | Conf. |
|---|---|---|
| Razón social | DUFFCO INGENIERÍA Y CONSTRUCCIÓN SpA | [V] |
| RUT | 77.119.761-2 | [V] |
| Origen | Constituida como "Duffco Ingeniería y Construcción Limitada" (nombre de fantasía Duffco Ltda.), extracto publicado en Diario Oficial el 31-01-2020. Luego transformada a SpA; estatutos refundidos publicados el 09-05-2025 | [V] |
| Inicio de actividades | 03-02-2020 | [V] |
| Capital | $1.500.000.000, dividido en mil acciones | [V] |
| Socios fundadores | Julio Francisco Dufflocq Urmeneta (10% del capital en la constitución) e Inversiones y Asesorías Duffco como segundo aportante (porcentaje no visible en la fuente). Estructura actual de propiedad y directorio | [V] fundación / [P] porcentajes y actual |
| Domicilio | Av. Américo Vespucio Sur 700, Of. 601, Las Condes, Santiago | [V] |
| Giro principal (SII) | Construcción de carreteras y líneas de ferrocarril. Giros secundarios: demolición, preparación del terreno, otras obras de ingeniería civil, proyectos de servicio público, edificios residenciales y no residenciales | [V] |
| Tamaño | Clasificada como empresa grande; media de 344 empleados entre 2020 y 2023, con alta variabilidad (operación por proyecto). LinkedIn muestra 46 perfiles asociados | [V] dotación / [H] que los 46 de LinkedIn sean mayoritariamente personal de oficina |
| Autodefinición pública | "Empresa de construcción con la misión de realizar obras públicas para la comunidad" (LinkedIn); "obras civiles y viales que mejoran Chile" (avisos laborales) | [V] |
| Objeto social | Obras de ingeniería y construcción públicas o privadas, explícitamente mandatadas por MOP (cualquiera de sus Direcciones), MINVU, SERVIU, municipalidades u otros organismos públicos: obras civiles, viales, industriales, navales, mineras, hidráulicas, portuarias, marítimas; loteos y urbanizaciones; desarrollo inmobiliario | [V] |
| Flota | Opera maquinaria propia con talleres y plan de mantención (aviso de "Planificador de Mantenimiento Maquinaria"; técnicos mecánicos en Chillán) | [V] |

### Personas de contacto del proyecto
| Persona | Rol en el proyecto | Conf. |
|---|---|---|
| Fabiana Pañella | Gerente de Administración. Lleva el proceso de pólizas de garantía, desde la adjudicación hasta la entrega al MOP; más de 4 años en la empresa. Usuaria del primer agente. Perfil en `usuarios/fabiana.md` | [V] |
| Catalina | Trabaja frecuentemente con Santi; fuente sobre licitaciones y Mercado Público | [V] |
| Nicolás Paredes | Arma la propuesta económica de las licitaciones (APU, formulario de presupuesto, E.2) en CTBudget; usuario del proceso 2 de Santi. Figura como responsable en CTBudget. Cargo, fluencia en IA, equipo y asiento Team: [P] | [V] nombre y rol (reporte de Santi, 16-11) |
| Julio Dufflocq | Define el precio de cada oferta: entrega un Excel con las partidas del itemizado oficial, una columna de costo estimado y otra de precio de venta unitario objetivo, del que parte la propuesta económica. Cargo: [P] | [V] rol (reporte de Santi, 16-11) |

### Equipo de implementación (no es personal de Duffco)
| Persona | Rol | Conf. |
|---|---|---|
| Lucas | Colaborador de Santi desde 2026-11-12; trabaja procesos distintos a los de Santi con su propio agente constructor. Coordinación solo por el repo `Sandia`. Puede ver todo lo que ve Santi; usa su cuenta personal de Claude (asiento en el plan Team de Duffco por evaluar). Catalina autorizó su acceso a documentos de Duffco mientras se prueba esta forma de trabajo | [V] (según Santi, 2026-11-16) |

- GitHub de Duffco: organización `duffco-spa` (owner Santi), un repositorio privado por agente entregado [V, bienvenida de Santi, 16-11].

**Lectura de Sayin:** empresa joven (6 años) con crecimiento rápido, dependencia casi total del MOP como mandante, y operación descentralizada (oficina central en Santiago, obras en el norte grande, centro y sur). Esto implica que los procesos administrativos y documentales se coordinan a distancia entre oficina central y faenas. [H]

---

## 2. MODELO DE NEGOCIO Y CARTERA

### 2.1 Perfil comercial [V]

- Cliente dominante: Ministerio de Obras Públicas.
- Licitaciones adjudicadas registradas en Mercado Público: **17**, por un total aproximado de **$72.495 millones**.
  - Dirección de Vialidad: 14 licitaciones, ~$59.732 millones.
  - Dirección de Obras Hidráulicas (DOH): 3 licitaciones, ~$12.763 millones.
- Además aparece en el registro de contratos MOP iniciados en marzo de 2025 (DOH, conservación de obras de riego fiscales, bocatomas). [V]
- Nota: estas cifras provienen de un agregador (todolicitaciones.cl) que lee Mercado Público. Pueden no incluir contratos licitados fuera del portal antes de que su uso fuera obligatorio para obras MOP (ver sección 5). Cartera real completa: [P].

### 2.2 Contratos adjudicados conocidos [V]

| Adjudicación | Contrato | Mandante | Región (según nombre) |
|---|---|---|---|
| 02-09-2020 | OCA Quebrada El Toro II, Antofagasta | DOH | Antofagasta |
| 21-10-2020 | Conservación saneamiento Ruta A-315 y A-345 | Vialidad | Arica y Parinacota |
| 30-03-2021 | Obras de mejoramiento Ruta C-495, La Fragua Tramo 1 | Vialidad | Atacama |
| 25-08-2021 | Reposición Puente El Rosario y accesos (3er llamado) | Vialidad | La Araucanía |
| 30-03-2022 | Camino básico por conservación Ruta A-485, sector cruce A-487 | Vialidad | Tarapacá |
| 30-03-2022 | Conservación red vial Ruta A-535 km 0,0 al 6,0 | Vialidad | Tarapacá |
| 21-07-2023 | CCB B-245 (cuarto llamado) | Vialidad | Antofagasta |
| 14-11-2023 | Conservación por emergencia Ruta A-13 km 70 al 75 | Vialidad | Arica y Parinacota |
| 14-11-2023 | Conservación red vial Ruta A-191 | Vialidad | Arica y Parinacota |
| 09-01-2024 | Construcción obras fluviales Río Salado Etapa I | DOH | Atacama (Chañaral) |
| 20-01-2025 | Construcción obras fluviales Río Salado Chañaral Etapa 2 | DOH | Atacama (Chañaral) |
| 10-04-2025 | Camino básico Ruta B-12 | Vialidad | Antofagasta |
| 20-08-2025 | Conservación camino básico Ruta B-115-C | Vialidad | Antofagasta |
| 12-09-2025 | Camino básico por conservación E-315 y E-287, Petorca | Vialidad | Valparaíso |
| 09-10-2025 | Conservación red vial rutas San Pedro de Atacama | Vialidad | Antofagasta |
| 17-04-2026 | Reposición Ruta 5, sector Cuesta Chaca Sur (2do llamado) | Vialidad | Arica y Parinacota |
| 04-08-2026 | Conservación caminos básicos, calles periferia poniente Calama | Vialidad | Antofagasta |

Notas:
- El agregador etiqueta algunas regiones por el código del organismo y no por la ubicación real. La columna región se infirió del nombre de la obra.
- Cuesta Chaca Sur: el plan de licitaciones 2025 de Vialidad describe el proyecto como reposición de un tramo de la Ruta 5 entre los km 2.009 y 2.023. [V] Es probablemente el contrato más grande y más reciente de la cartera. Monto: [P].
- Río Salado (Chañaral): obras de control aluvional. La primera etapa partió en 2023, consistió en la canalización del río en el sector urbano de Chañaral, con inversión de $4.700 millones, y fue inaugurada por el MOP en mayo de 2025. El conjunto de obras debería concluir en 2027. [V] Que Duffco haya ejecutado esa etapa se infiere del registro de adjudicación. [V]

### 2.3 Tipos de trabajo predominantes [V]

1. **Conservación vial y caminos básicos** (la mayoría de la cartera): mejoramiento de caminos de bajo tránsito, saneamiento, conservación de red vial.
2. **Reposición de pavimentos y puentes** (Ruta 5 Cuesta Chaca Sur, Puente El Rosario).
3. **Obras hidráulicas y fluviales** (Río Salado, Quebrada El Toro, bocatomas de riego).
4. **Obras de emergencia** (Ruta A-13).

### 2.4 Huella geográfica [V]

- Concentración fuerte en el **norte grande**: Arica y Parinacota, Tarapacá, Antofagasta, Atacama.
- Presencia puntual en Valparaíso (Petorca) y La Araucanía.
- Operación logística: oficina en Las Condes, faenas a más de 1.000 km. [H] Implica alta carga de coordinación documental remota (estados de pago, libro de obras, garantías, rendiciones).

---

## 3. EL CLIENTE: ESTRUCTURA DEL MOP RELEVANTE PARA DUFFCO

### 3.1 Actores institucionales

| Actor | Rol para Duffco |
|---|---|
| Dirección General de Obras Públicas (DGOP) | Emite instructivos sobre contratación; administra el Registro de Contratistas | [V] |
| Dirección de Vialidad | Principal mandante (caminos, conservación, Ruta 5) | [V] |
| Dirección de Obras Hidráulicas (DOH) | Mandante en obras fluviales y de riego | [V] |
| Dirección de Contabilidad y Finanzas (DCyF) | Registro de contratos, garantías y pagos | [V] |
| Fiscalía MOP (nacional y regionales) | Aprueba pólizas de garantía (V°B° previo para fiel cumplimiento, garantía adicional, anticipo y canje de retenciones) | [V] |
| SEREMI MOP regionales | Las garantías se emiten a la orden del Director o del Secretario Regional, según si el contrato se adjudica a nivel nacional o regional | [V] |
| Inspector Fiscal (IF) y Asesoría a la Inspección Fiscal (AIF) | Contraparte técnica diaria en obra; registra en el Libro de Obras Digital | [V] |
| Contraloría General de la República | Toma de razón y control de juridicidad de resoluciones y convenios | [V] |

### 3.2 Autoridades vigentes (al 2026-10-12) [V]

- Gobierno del Presidente José Antonio Kast, desde el 11 de marzo de 2026.
- Ministro de Obras Públicas: Martín Arrau García-Huidobro.
- Subsecretario de Obras Públicas: Nicolás Balmaceda Jimeno.
- Director General de Obras Públicas: Joaquín Dagá Kunze (firma el Oficio DGOP N° 374 de abril de 2026).
- Estas autoridades cambian. Verificar antes de usar en documentos formales.

### 3.3 Señales de política 2026 [V]

- El nuevo gobierno pone énfasis en concesiones y en "sentido de urgencia" en infraestructura.
- La DGOP dejó en suspenso, mediante el Oficio N° 374 de 2026, la aplicación del Oficio DGOP N° 911 de 2023 sobre anticipos en contratos de obras, hasta nuevas directrices. Los anticipos no quedan prohibidos, pero la Dirección debe informar previamente a la DGOP.
- Vialidad está licitando contratos de conservación global en varias regiones (ej. siete contratos globales mixtos en Atacama en mayo de 2026). Es el tipo de contrato del segmento de Duffco. [V]

---

## 4. CÓMO GANA Y EJECUTA CONTRATOS UNA CONSTRUCTORA MOP

Ciclo de vida típico de un contrato (fuentes: RCOP, Oficio DGOP 374/2026). Los pasos internos de Duffco son [P].

1. **Inscripción y vigencia en el Registro de Contratistas MOP.** Para participar y ser adjudicado, el contratista debe estar inscrito en el registro y categoría que fijen las bases. El registro se divide en Obras Mayores y Obras Menores, con especialidades y categorías según capacidad económica, experiencia y personal profesional. [V] Registros y categorías de Duffco: [P].
2. **Licitación.** Desde la Ley N° 21.634 (que modificó la Ley N° 19.886 de Compras Públicas), el MOP usa obligatoriamente el portal Mercado Público para obras y consultorías, con exigencias reforzadas de probidad: declaraciones juradas de ausencia de conflicto de interés, prohibición de comunicaciones y un "Pacto de Integridad" que firman los oferentes. [V]
3. **Estudio de bases y armado de oferta.** Bases Administrativas Generales, Especiales, Anexo Complementario, especificaciones técnicas, presupuesto oficial. [V] Proceso interno de Duffco: [P].
4. **Adjudicación y constitución de garantías** (ver sección 6).
5. **Ejecución.** Libro de Obras Digital (LOD), estados de pago, modificaciones de contrato, aumentos de obra, valores proforma, subcontratos. [V]
6. **Recepción** provisional (puede ser parcial desde la reforma DS 150/2024) y definitiva. [V]
7. **Liquidación** del contrato, devolución de retenciones y de garantías. [V]

---

## 5. MARCO NORMATIVO CLAVE

| Norma | Qué regula | Relevancia | Conf. |
|---|---|---|---|
| D.F.L. MOP N° 850 de 1997 | Ley orgánica del MOP (texto refundido de la Ley 15.840). Su art. 109 habilita pólizas de seguro como garantía | Base legal de las pólizas | [V] |
| D.S. MOP N° 75 de 2004 (RCOP) | Reglamento para Contratos de Obras Públicas. Forma parte integrante de todos los contratos de obra MOP | Norma central | [V] |
| D.S. MOP N° 150 de 2024 | Reforma amplia al RCOP, difundida por Oficio DGOP N° 205 de marzo de 2026. Subcontratación hasta 50% del valor del contrato, flexibiliza subcontratistas no inscritos, permite empresas relacionadas en una misma licitación, elimina el registro especial por monto, permite modificaciones de hasta 50% en casos calificados, recepción provisional parcial, nuevo procedimiento de liquidación. Aplica a nuevas licitaciones y, si el contratista acepta, a contratos en ejecución | Cambia reglas que los agentes deben conocer. Verificar textos de artículos afectados | [V] |
| D.S. MOP N° 88 de 2025 | Nuevo Reglamento de Montos (reemplaza DS 1093 de 2003). Redistribuye competencias de aprobación hacia direcciones regionales, fija montos para modificaciones y tratos directos | Define quién aprueba qué en el MOP | [V] |
| D.S. MOP N° 108 de 2009 | Aprueba Bases Administrativas Generales para un tipo de contratos de obra (alcance exacto a verificar). Modificado por D.S. MOP N° 27 de 2024 para permitir anticipos de hasta 50% del contrato primitivo en contratos de ejecución de obras por sistema de pago contra recepción | Aplicabilidad exacta a los contratos de conservación de Duffco: [P] | [V] modificación / [P] alcance |
| Ley N° 19.886 modificada por Ley N° 21.634 | Compras públicas; ahora aplica a contratación de obras MOP (Oficio DGOP N° 1023 de 2025) | Uso de Mercado Público, probidad | [V] |
| Registro de Contratistas: Categorías y Especialidades | Documento aprobado por resolución MOP (Res. Ex. 905 de 2008 y modificaciones). Especialidades O.C. (ej. 13.O.C. Obras de Defensas Fluviales) | Determina en qué licitaciones puede participar Duffco | [V] |
| Oficio DGOP N° 374 de 2026 ("Instructivo de instructivos") | Compila las instrucciones vigentes de gestión contractual. Documento de referencia obligatorio para cualquier agente de procesos MOP | Fuente maestra | [V] |
| Bases de Prevención de Riesgos para Contratos de Obras MOP (con perspectiva de género) | Exigencias de prevención en obras | Posible proceso a automatizar (reportabilidad) | [V] |

Biblioteca DGOP: los instructivos se reúnen en bibliotecadgop.mop.gob.cl, con acceso mediante usuario de sistemas MOP. Duffco probablemente tiene credenciales. [V] plataforma / [P] acceso de Duffco.

---

## 6. GARANTÍAS Y PÓLIZAS: REGLAS DURAS

Este es el dominio del primer caso de uso discutido (revisión de pólizas antes de entregarlas al MOP). Las reglas generales vienen del RCOP. **Las bases de cada licitación pueden aumentar montos y plazos, por lo que siempre mandan las bases del contrato específico.**

### 6.1 Garantía de fiel cumplimiento (RCOP art. 96) [V, verificar vigencia post DS 150/2024]

- Instrumento: boleta bancaria o póliza de seguro.
- Monto:
  - Obras Mayores: 3% del valor del contrato.
  - Obras Menores: 5% del valor del contrato.
- Vigencia:
  - Obras Mayores: plazo del contrato + 24 meses.
  - Obras Menores: plazo del contrato + 18 meses.
- Expresada en Unidades de Fomento.
- A la orden del Director o del Secretario Regional, según el nivel de adjudicación.
- Si es póliza: debe ser la inscrita en el Registro de Pólizas de la Superintendencia de Valores y Seguros (hoy CMF) como "Póliza de Seguro de Garantía de Obras Públicas", aprobada por el MOP, y **no puede contener cláusula, endoso ni adición que limite las atribuciones que el texto original confiere al MOP**.
- Aumentos de obra u obras extraordinarias: requieren garantías adicionales en el mismo porcentaje y plazo. Si hay aumento de plazo, todas las garantías deben quedar con idéntica fecha de vencimiento.
- Renovación: responsabilidad del contratista. Si no se renueva antes de 30 días del vencimiento, el MOP puede hacerla efectiva; la no renovación es falta grave.
- Las bases pueden aumentar el monto y ampliar el plazo.

### 6.2 Garantía de anticipo (contratos bajo DS 108 de 2009, modificado por DS 27 de 2024) [V]

- Anticipo de hasta 50% del contrato primitivo, descontados los valores proforma, si las bases lo contemplan.
- Garantía: boleta bancaria o póliza (cuando las bases lo autoricen) por el total anticipado, en UF, con vigencia igual al plazo del contrato + 6 meses.
- Recordar que la DGOP dejó en suspenso las directrices generales de anticipos (Oficio 374/2026).

### 6.3 Aprobación por Fiscalía [V]

- Requieren **aprobación previa de Fiscalía** para cursar estados de pago: pólizas de fiel cumplimiento del contrato y de canje de retenciones.
- Pueden estar **en trámite de aprobación** sin bloquear el estado de pago: póliza de responsabilidad civil y póliza todo riesgo de construcción.
- El Manual de Contratos MOP indica V°B° de Fiscalía para garantía de fiel cumplimiento, garantía adicional y garantía por anticipo.
- Las licitaciones de obras deben incluir obligatoriamente la opción de garantizar el fiel cumplimiento con boleta bancaria o con póliza de seguro (Oficio DGOP N° 337 de 2020).

### 6.4 Riesgo de aseguradora [V]

- Precedente: en el caso de la ampliación del GAM, el MOP intentó cobrar pólizas por cerca de $1.195 millones y la aseguradora se negó, alegando falta de liquidación del contrato, reclamo extemporáneo y agravación de riesgo. El Consejo de Autorregulación de seguros resolvió que debía pagar. El MOP llegó a restringir pólizas de esa aseguradora y una Corte acogió un recurso de protección en su contra (2021).
- Implicancia para agentes: la revisión de una póliza no es solo formal. Hay que verificar la compañía emisora, el código de registro CMF del texto y la ausencia de condiciones que limiten el cobro "a primer requerimiento".

### 6.5 Checklist mínimo derivado (para el futuro agente de pólizas) [H, validar con Duffco y con una póliza real]

1. Tipo de garantía correcta para el hito (fiel cumplimiento, adicional, anticipo, canje de retenciones, RC, todo riesgo).
2. Beneficiario correcto: Director o SEREMI según nivel de adjudicación; nombre exacto del contrato y su código.
3. Monto en UF igual o mayor al exigido (RCOP o bases, el que sea mayor).
4. Vigencia igual o mayor a la exigida; coherencia con aumentos de plazo y otras garantías vigentes.
5. Texto de condiciones generales con código de registro CMF correspondiente a "Póliza de Seguro de Garantía de Obras Públicas".
6. Ausencia de cláusulas, endosos o adiciones que limiten las atribuciones del MOP.
7. Identificación correcta del tomador (Duffco, RUT 77.119.761-2) y, si aplica, consorcio.
8. Firmas y formalidades de la aseguradora (electrónica o física, según exija el MOP).
9. Coherencia con las bases específicas de esa licitación (las bases pueden subir monto y plazo).
10. Cada hallazgo con cita a página y cláusula de la póliza y a la norma o base que lo exige. Sin cita, el resultado es "no verificado".

---

## 7. SISTEMAS Y PLATAFORMAS DEL ECOSISTEMA MOP [V]

| Sistema | Uso |
|---|---|
| Mercado Público | Portal obligatorio para licitaciones de obras MOP. Según Catalina, es la fuente principal de documentación de licitaciones de Duffco (un proyecto puede tener unos 70 documentos). Tiene API pública y gratuita con ticket personal (ClaveÚnica, 10.000 consultas diarias); candidata para el proceso 2. Que la API entregue los adjuntos: [P] |
| Libro de Obras Digital (LOD) | Registro oficial de la obra; incluye el estado operativo del contrato (adjudicación, ejecución, recepción, paralización, término) |
| Carpeta Digital de liquidación | Repositorio obligatorio con la documentación necesaria para liquidar el contrato |
| SICOF / SAFI | Sistemas financiero-contables del MOP donde se registran contratos, recepciones y pagos |
| SIEMOP-FEMN | Sistema MOP de uso obligatorio en licitaciones privadas y tratos directos |
| Registro de Contratistas MOP (en línea) | Inscripción, renovación, certificado de inscripción vigente |
| Biblioteca DGOP | Repositorio de instructivos vigentes |
| Confirming BancoEstado | Herramienta de financiamiento difundida por la DGOP como alternativa al factoring |

### 7.1 Sistemas internos de Duffco

**CTBudget (software de presupuestos)** [V, reportes de Santi del 16 al 18-11]
- CTBudget para Windows, versión 21.xx, sobre el OneDrive empresarial de Duffco. Lo usa Nicolás Paredes para los APU de las ofertas.
- Su base nativa es un archivo `.CTBX` de texto plano, legible sin el programa: unos 1.349 registros entre insumos (código, unidad, precio, fecha) y APU (lista de insumos con cantidad por unidad de obra). Coma decimal, fechas en serial de Excel, algunas cantidades escritas como expresiones (`1/500`), APU anidados (el CD se calcula de forma recursiva). Prefijos de insumos: `1O` mano de obra, `2M` materiales, `3E` equipos.
- La biblioteca está sucia: 722 códigos de APU con duplicados en formatos distintos, un mismo código usado para trabajos distintos, APU cuyo material no calza con el nombre, plantillas con precio 0 y registros de prueba. Precios de insumos mayoritariamente de 2021 a 2023. Faltan APU para algunos trabajos (retiro manual de basuras, reciclado de carpetas granulares, hormigón G40, emulsión con polímeros). Cualquier agente que la use necesita normalizar códigos y una regla de selección [P].
- Decisión de Santi (18-11) para su proceso 2: la biblioteca la mantiene CTBudget y el agente solo lee el `.CTBX`, nunca lo escribe.
- Tiene una fecha fija configurada que se imprime en los APU (las ofertas de nov. 2026 salieron con "26-08-2025") [V].

**Propuesta económica que se presenta al MOP** [V, caso A-345]
- Cuatro documentos: carta oferta (plantilla MOP, monto en números y palabras, garantía en UF), formulario de presupuesto (plantilla Excel MOP con el itemizado oficial), documento de APU (uno por partida) y formulario E.2 de gastos generales y utilidades.
- GG y UT se aplican sobre el CD de cada partida, hoy 90% y 10% (configurables). El E.2 reparte el GG total en rubros mensuales por el plazo de la obra y debe cuadrar al peso con el GG de los APU. IVA 19% sobre el neto; la proforma va aparte y la fija el MOP.

Otros sistemas internos (ERP, gestión documental, correo, Drive o SharePoint): [P]. Es información crítica para diseñar agentes que trabajen con archivos locales.

---

## 8. MAPA DE PROCESOS CANDIDATOS A AUTOMATIZACIÓN [H]

Hipótesis ordenadas por ROI estimado y factibilidad con agentes de escritorio que trabajan sobre archivos locales. Todas requieren validación con Duffco antes de diseñar.

| # | Proceso | Por qué es buen candidato | Riesgo |
|---|---|---|---|
| 1 | Revisión de pólizas y garantías antes de entregarlas al MOP | Alto volumen documental, reglas explícitas, verificable, ya identificado por Duffco | Alto si el humano no revisa. Agente como pre-screener con semáforo y citas |
| 2 | Estudio de bases de licitación (extracción de requisitos, plazos, garantías, registro y categoría exigidos, criterios de evaluación) | Bases largas y heterogéneas; error costoso (oferta inadmisible) | Medio |
| 3 | Checklist de admisibilidad de ofertas (documentos, declaraciones juradas, Pacto de Integridad) | Reglas cambiantes por Ley 21.634 | Medio |
| 4 | Control de vencimientos de garantías y renovaciones (30 días antes) | Falta grave si falla; trabajo repetitivo | Bajo |
| 5 | Preparación de estados de pago y su respaldo documental | Ciclo mensual, mucha consolidación de datos | Medio |
| 6 | Redacción y revisión de comunicaciones al Inspector Fiscal y anotaciones en LOD | Frecuente, formato regulado | Medio |
| 7 | Gestión de liquidación y carpeta digital | Retenciones y garantías atrapadas cuestan caja | Medio |
| 8 | Mantención de flota (planificación, cotizaciones, facturas) | Proceso interno visible en avisos laborales | Bajo |
| 9 | Reportabilidad de prevención de riesgos | Exigencias de bases de prevención MOP | Bajo |

---

## 9. GLOSARIO

- **RCOP:** Reglamento para Contratos de Obras Públicas (D.S. MOP N° 75 de 2004).
- **DGOP:** Dirección General de Obras Públicas.
- **DOH:** Dirección de Obras Hidráulicas.
- **DCyF:** Dirección de Contabilidad y Finanzas del MOP.
- **IF / AIF:** Inspector Fiscal / Asesoría a la Inspección Fiscal.
- **LOD:** Libro de Obras Digital.
- **Bases (BAG, BAE, Anexo Complementario):** documentos que rigen cada licitación; prevalecen sobre reglas generales cuando el reglamento lo permite.
- **Boleta de garantía:** garantía bancaria. Alternativa a la póliza de seguro.
- **Póliza de garantía a primer requerimiento:** seguro de caución cobrable a solo requerimiento del beneficiario.
- **CMF:** Comisión para el Mercado Financiero (ex SVS). Mantiene el registro de textos de pólizas.
- **Valores proforma:** partidas incorporadas al contrato que no se exigen al contratista dentro del precio; no están afectas al límite de aumento del 30%, pero partidas nuevas de esta naturaleza requieren aprobación previa de la DGOP.
- **Obras Mayores / Obras Menores:** divisiones del Registro de Contratistas.
- **Camino básico:** solución vial de estándar intermedio para caminos de bajo tránsito, típicamente mediante contratos de conservación.
- **Conservación global mixta:** contrato de mantención de una red de caminos por varios años, que combina precios unitarios con niveles de servicio.
- **Liquidación:** cierre económico del contrato; determina cobro o devolución de garantías y retenciones.

---

## 10. HUECOS DE INFORMACIÓN (completar con Santi)

Prioridad alta:
- [ ] Organigrama de oficina central y nombres de las áreas que intervienen en garantías, licitaciones y estados de pago.
- [ ] Usuarios finales de cada agente (nombre, cargo, fluencia en IA, sistema operativo, plan Claude).
- [x] Plan Claude: Team; Fabiana con asiento Standard (decisión 2026-10-14). Pendiente: quién administra las cuentas y mínimo de asientos.
- [ ] Registros y categorías de Duffco en el Registro de Contratistas MOP.
- [ ] Cómo se revisan hoy las pólizas: quién, cuántas por mes, cuánto tarda cada una, errores típicos, qué documentos cruza.
- [ ] Aseguradoras y corredores con que trabaja Duffco. Corredora actual: Conosur [V]; aseguradoras: [P].
- [ ] Dónde viven los documentos (Drive, SharePoint, servidor local) y convención de nombres.

Prioridad media:
- [ ] Monto y estado de los contratos vigentes (en especial Cuesta Chaca Sur, Calama, San Pedro de Atacama).
- [ ] Consorcios en que participa Duffco.
- [ ] Software interno (ERP, control de flota). Presupuestos: CTBudget [V], ver 7.1.
- [ ] Contacto directo de Santi en el directorio y patrocinador interno del proyecto.

---

## 11. FUENTES

Empresa:
- Diario Oficial, constitución Duffco Ltda. (31-01-2020): https://dequienes.cl/diario-oficial/2020/01/31/duffco-ingenieria-y-construccion-limitada-1720406
- Diario Oficial, estatutos refundidos Duffco SpA (09-05-2025): https://dequienes.cl/diario-oficial/2025/05/09/duffco-ingenieria-y-construccion-spa-77119761-2-2643761
- Ficha empresa (dirección, tamaño, dotación): https://datalux.cl/empresa/77119761-2-duffco-ingenieria-y-construccion-spa/
- Giro SII: https://chilepymes.com/info/duffco-ingenieria-y-construccion-spa-6BF5CDBA53A23856
- Licitaciones adjudicadas: https://www.todolicitaciones.cl/proveedor/771197612/duffco-ingenieria-y-construccion-spa
- Contratos MOP iniciados marzo 2025: https://planeamiento.mop.gob.cl/uploads/sites/12/2025/04/Contratos-Iniciados-marzo-de-2025.pdf
- Aviso laboral flota: https://duoclaboral.cl/trabajar-en-duffco-ingenieria-y-construccion-spa/trabajos/planificador-de-mantenimiento-maquinaria/573580
- Perfil laboral: https://cl.computrabajo.com/empresas/acerca-de-duffco-AFA6398407F5EC2F
- Obras Río Salado Chañaral: https://www.infraestructurapublica.cl/ministra-de-obras-publicas-reabre-aerodromo-de-chanaral-e-inaugurara-obras-por-20-mil-millones-de-pesos-en-la-ciudad/
- Plan de licitaciones Vialidad 2025 (Cuesta Chaca Sur): https://www.mop.gob.cl/archivos/2025/03/5.-DIRECCION_VIALIDAD_plan_licitaciones_2025.pdf

Normativa y MOP:
- RCOP art. 96: https://iura.cl/dto-75-mop/96 (verificar en https://www.bcn.cl/leychile)
- Oficio DGOP N° 374 de 2026, Instructivo de instructivos: https://dgop.mop.gob.cl/uploads/sites/5/2026/07/OFICIO_374_27-04-2026_Instructivo-de-instructivos.pdf
- Manual de Contratos MOP: https://dgop.mop.gob.cl/areasdgop/ContratosConsultorias/Documents/MANUAL%20DE%20CONTRATOS.pdf
- Registro de Contratistas, Categorías y Especialidades: https://dgop.mop.gob.cl/uploads/sites/5/2024/08/Contratistas_Categorias_y_Especialidades.pdf
- Autoridades MOP 2026: https://www.infraestructurapublica.cl/expresidente-frei-visita-el-mop-para-compartir-con-sus-autoridades-su-vision-sobre-las-politicas-de-infraestructura-y-concesiones/
- Caso pólizas GAM: https://www.df.cl/mercados/seguros/ampliacion-del-gam-enfrenta-al-mop-con-aseguradora-de-credito-de-avla y https://www.jurischile.com/2021/02/se-acoge-recurso-de-proteccion-contra.html
- Conservación global Atacama 2026: https://www.infraestructurapublica.cl/mop-comenzo-licitacion-de-siete-contratos-clave-para-fortalecer-la-conectividad-en-atacama/

---

## 12. CHANGELOG

- v1.0 (2026-10-12): versión inicial construida por investigación pública. Pendiente validación de Santi en todas las filas [P] y [H].
- v1.1 (2026-10-14): personas de contacto (Fabiana, Catalina), Mercado Público como fuente principal y su API, plan Claude Team, corredora Conosur. Aprobado por Santi.
- v1.3 (2026-11-16, Zurgo): cargo de Fabiana Pañella (Gerente de Administración) y organización `duffco-spa`, desde la bienvenida de Santi; confirmados [V] por Santi en Sandia. Aprobado por Lucas.
- v1.4 (2026-11-18, Zurgo): Nicolás Paredes y Julio Dufflocq en personas de contacto; nueva sección 7.1 (CTBudget, formato `.CTBX`, estado de la biblioteca, documentos de la propuesta económica). Fuente: reportes de Santi del 16, 17 y 18-11 en Sandia. Aprobado por Lucas.
