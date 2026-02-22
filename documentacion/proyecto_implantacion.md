---
stylesheet:
  - https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap
body_class: pdf-document
css: |-
  body {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
  }
  .portada {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    page-break-after: always;
  }
  .portada h1 {
    font-size: 32pt;
    font-weight: 700;
    color: #1a365d;
    margin-bottom: 10px;
    border: none;
  }
  .portada h2 {
    font-size: 16pt;
    font-weight: 400;
    color: #4a5568;
    margin-bottom: 40px;
    border: none;
  }
  .portada .datos {
    font-size: 12pt;
    color: #2d3748;
    line-height: 2;
  }
  .portada .linea {
    width: 200px;
    height: 3px;
    background: #2b6cb0;
    margin: 30px auto;
  }
  h1 {
    font-size: 20pt;
    color: #1a365d;
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 6px;
    margin-top: 30px;
    page-break-before: always;
  }
  h1:first-of-type {
    page-break-before: avoid;
  }
  h2 {
    font-size: 14pt;
    color: #2c5282;
    border-bottom: 1px solid #bee3f8;
    padding-bottom: 4px;
    margin-top: 20px;
  }
  h3 {
    font-size: 12pt;
    color: #2d3748;
    margin-top: 15px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
  }
  th {
    background-color: #2b6cb0;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
  }
  td {
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
  }
  tr:nth-child(even) {
    background-color: #f7fafc;
  }
  code {
    background-color: #edf2f7;
    padding: 2px 5px;
    border-radius: 3px;
    font-size: 10pt;
  }
  pre {
    background-color: #1a202c;
    color: #e2e8f0;
    padding: 14px;
    border-radius: 6px;
    font-size: 9pt;
    overflow-x: auto;
  }
  pre code {
    background: none;
    padding: 0;
    color: #e2e8f0;
  }
  blockquote {
    border-left: 4px solid #2b6cb0;
    padding-left: 12px;
    color: #4a5568;
    margin: 10px 0;
  }
  strong {
    color: #1a202c;
  }
  a {
    color: #2b6cb0;
  }
  ul, ol {
    margin: 6px 0;
  }
  @page {
    margin: 2cm 2.5cm;
    size: A4;
  }
  @page:first {
    margin: 0;
  }
---

<div class="portada">

# PROYECTO DE IMPLANTACION

## Sistemas de Gestion Empresarial - 2 DAM

<div class="linea"></div>

<div class="datos">

**Alumno:** Kristian Olav Garcia Paulsen

**ERP utilizado:** Odoo 19.0

**Empresa ficticia:** NexusTech Solutions S.L.

**Repositorio:** https://github.com/kristiangarcia/Proyecto_Implantacion_SGE

**Curso:** 2024 - 2025

</div>

</div>

# INDICE

1. [Analisis de la Empresa](#1-analisis-de-la-empresa)
2. [Eleccion del Responsable](#2-eleccion-del-responsable)
3. [Deteccion de Necesidades y Evaluacion del ERP](#3-deteccion-de-necesidades-eleccion-y-evaluacion-del-erp)
4. [Instalacion del ERP y Seleccion de Modulos](#4-instalacion-del-erp-y-seleccion-de-modulos)
5. [Planificacion de la Migracion](#5-planificacion-de-la-migracion)
6. [Plan de Formacion](#6-plan-de-formacion)
7. [Migracion y Carga de Datos](#7-migracion-de-los-procesos-de-negocio-y-carga-de-datos)
8. [Pruebas y Resolucion de Problemas](#8-pruebas-y-resolucion-de-problemas)
9. [Documentacion del Proceso](#9-documentacion-del-proceso)

---

# 1. ANALISIS DE LA EMPRESA

## 1.a. Plan de negocio

**NexusTech Solutions S.L.** es una empresa de soluciones tecnologicas ubicada en Madrid (Calle Tecnologia, 42 - 28001). Se dedica a la venta de productos de software, hardware y servicios de consultoria IT a otras empresas (modelo B2B).

**Datos fiscales:**
- CIF: ESB12345678
- Telefono: +34 912 345 678
- Email: info@nexustech.es
- Web: https://www.nexustech.es

**Situacion actual:**
La empresa lleva funcionando 5 años y hasta ahora ha gestionado toda su operativa con hojas de calculo (Excel), facturacion manual en Word, y correo electronico para comunicarse con clientes y proveedores. Los empleados guardan los datos de clientes en archivos Excel individuales, las facturas se crean manualmente copiando plantillas de Word, y el inventario de productos se lleva en una hoja de calculo compartida que frecuentemente tiene datos desactualizados.

## 1.b. Trabajadores y cargos

| Nombre | Cargo | Departamento |
|--------|-------|-------------|
| Kristian Garcia | Director General / Administrador ERP | Direccion |
| Ana Lopez | Directora Comercial | Ventas |
| Carlos Ruiz | Tecnico de Soporte | Soporte Tecnico |
| Laura Martinez | Responsable de Compras | Compras |
| Pedro Sanchez | Contable | Contabilidad |
| Sofia Navarro | Responsable RRHH | Recursos Humanos |
| Miguel Torres | Comercial | Ventas |
| Elena Diaz | Tecnica de Sistemas | Soporte Tecnico |
| David Moreno | Almacenero | Almacen |
| Raquel Fernandez | Administrativa | Administracion |

## 1.c. Areas funcionales

Las areas funcionales de la empresa son:

- **Direccion:** Gestion general, toma de decisiones estrategicas, supervision de todas las areas.
- **Ventas:** Gestion de oportunidades comerciales, presupuestos, pedidos de venta, relacion con clientes.
- **Compras:** Gestion de proveedores, pedidos de compra, negociacion de precios.
- **Almacen:** Control de stock, entradas y salidas de material, inventarios.
- **Contabilidad:** Facturacion, cobros, pagos, contabilidad general.
- **Recursos Humanos:** Gestion de empleados, contratos, nominas, ausencias.
- **Soporte Tecnico:** Atencion a clientes, resolucion de incidencias, instalacion de productos.

## 1.d. Procesos de negocio

Los principales procesos de negocio de NexusTech son:

1. **Proceso de venta:**
   - Un cliente contacta con la empresa (telefono, email, web).
   - El comercial crea un presupuesto con los productos/servicios solicitados.
   - Si el cliente acepta, se convierte en pedido de venta.
   - Se genera la factura y se envia al cliente.
   - Se registra el cobro cuando el cliente paga.

2. **Proceso de compra:**
   - El responsable de compras detecta necesidad de stock o un pedido de cliente requiere material.
   - Se solicita presupuesto a uno o varios proveedores.
   - Se elige el proveedor y se confirma el pedido de compra.
   - Se recibe el material en almacen y se verifica.
   - Se registra la factura del proveedor y se realiza el pago.

3. **Proceso de soporte tecnico:**
   - El cliente reporta una incidencia o solicita un servicio.
   - Se registra el ticket en el sistema.
   - Un tecnico se asigna y resuelve la incidencia.
   - Se cierra el ticket y se factura si corresponde.

4. **Proceso de gestion de proyectos IT:**
   - Se acuerda un proyecto con el cliente (desarrollo, consultoria, etc.).
   - Se planifican las tareas y se asignan a los tecnicos.
   - Los tecnicos registran las horas trabajadas.
   - Al finalizar, se factura segun las horas y el presupuesto acordado.

**Actualmente** todos estos procesos se hacen de forma manual: los presupuestos son documentos de Word, la facturacion es manual, el seguimiento de clientes se lleva en Excel, y la comunicacion entre departamentos es por email. No hay trazabilidad real de los procesos ni datos centralizados.

## 1.e. Diagrama de areas funcionales y procesos de negocio

```
                    ┌──────────────────────┐
                    │     DIRECCION         │
                    │  (Supervision general)│
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
    ┌─────▼─────┐      ┌──────▼──────┐     ┌──────▼──────┐
    │  VENTAS   │      │  COMPRAS    │     │    RRHH     │
    │           │      │             │     │             │
    │ Presupues.│      │ Pedidos     │     │ Empleados   │
    │ Pedidos   │      │ Proveedores │     │ Contratos   │
    │ Facturas  │      │ Recepciones │     │ Nominas     │
    └─────┬─────┘      └──────┬──────┘     └─────────────┘
          │                   │
          │            ┌──────▼──────┐
          │            │  ALMACEN    │
          │            │             │
          │            │ Stock       │
          │            │ Inventarios │
          │            │ Entradas    │
          │            │ Salidas     │
          │            └─────────────┘
          │
    ┌─────▼──────────┐     ┌─────────────────┐
    │ CONTABILIDAD   │     │ SOPORTE TECNICO │
    │                │     │                 │
    │ Facturas       │     │ Tickets         │
    │ Cobros/Pagos   │     │ Incidencias     │
    │ Impuestos      │     │ Proyectos IT    │
    └────────────────┘     └─────────────────┘
```

## 1.g. Tipos de S.I. y procesos de negocio

| Area funcional | Sistema actual | Proceso de negocio | Como se gestionan los datos |
|---|---|---|---|
| Ventas | Excel + Word | Presupuestos, pedidos, facturas | Hojas de calculo individuales por comercial, facturas en Word |
| Compras | Excel | Pedidos a proveedores | Hoja de calculo compartida |
| Almacen | Excel | Control de stock | Hoja de calculo (frecuentemente desactualizada) |
| Contabilidad | Contaplus (externo) | Facturacion y contabilidad | Software externo de contabilidad, datos duplicados |
| RRHH | Excel | Nominas, contratos | Archivos Excel en carpeta compartida |
| Soporte | Email | Tickets de soporte | Correos electronicos, sin seguimiento organizado |

## 1.h. Mapa conceptual del proceso de negocio de la empresa

```
     ┌──────── CLIENTE ────────┐
     │                         │
     ▼                         ▼
  Solicita              Reporta
  Producto/             Incidencia
  Servicio
     │                         │
     ▼                         ▼
  ┌──────────┐          ┌──────────┐
  │PRESUPUES.│          │ TICKET   │
  │  (Word)  │          │ (Email)  │
  └────┬─────┘          └────┬─────┘
       │ Acepta               │ Asignar
       ▼                      ▼
  ┌──────────┐          ┌──────────┐
  │ PEDIDO   │          │ TECNICO  │
  │ (Excel)  │          │ Resuelve │
  └────┬─────┘          └────┬─────┘
       │                     │
       ├──── Compra? ────┐   │
       │                 ▼   │
       │           ┌──────┐  │
       │           │PROVEED│  │
       │           │OReso  │  │
       │           └───┬──┘  │
       │               │     │
       ▼               ▼     ▼
  ┌──────────┐   ┌──────┐
  │ FACTURA  │   │ALMACEN│
  │  (Word)  │   │(Excel)│
  └────┬─────┘   └──────┘
       │
       ▼
  ┌──────────┐
  │  COBRO   │
  │(Contaplus│
  └──────────┘
```

Los procesos se representan con **cajas** (son las actividades) y las **flechas** indican el flujo. Las herramientas entre parentesis son las que se usan actualmente. Como se puede ver, los datos estan repartidos entre multiples herramientas sin integracion entre ellas.

---

# 2. ELECCION DEL RESPONSABLE

El responsable del proyecto de implantacion sera **Kristian Olav Garcia Paulsen**, que actuara como administrador del sistema ERP.

Se ha creado un usuario administrador en Odoo con los siguientes datos:
- **Usuario:** admin
- **Rol:** Administrador (acceso completo a todos los modulos)
- **Base de datos:** nexustech

Este usuario tendra permisos completos sobre todos los modulos instalados y sera el encargado de la configuracion inicial, la carga de datos y la formacion de los demas usuarios.

---

# 3. DETECCION DE NECESIDADES, ELECCION Y EVALUACION DEL ERP

## 3.a. Necesidades de la empresa

Tras analizar la situacion actual de NexusTech, se detectan las siguientes necesidades:

1. **Centralizacion de datos:** Actualmente cada departamento tiene sus propios archivos Excel. Se necesita que todos los datos esten en un unico sistema accesible por todos.

2. **Automatizacion de facturacion:** Las facturas se crean manualmente en Word, lo que provoca errores y duplicidades. Se necesita un sistema que genere facturas automaticamente a partir de pedidos.

3. **Control de stock real:** La hoja de calculo de almacen se desactualiza constantemente. Se necesita un sistema que actualice el stock automaticamente con cada entrada/salida.

4. **Seguimiento comercial:** No hay forma de hacer seguimiento de las oportunidades de venta. Los comerciales pierden clientes potenciales por falta de organizacion.

5. **Gestion de RRHH:** Los datos de empleados y contratos estan en Excel sin control. Se necesita un modulo que centralice la gestion de personal.

6. **Punto de venta:** Para la venta directa de productos hardware se necesita un TPV funcional.

7. **CRM:** Gestion de oportunidades de venta y relacion con clientes.

## 3.b. Evaluacion del ERP: Odoo

Se ha elegido **Odoo** como ERP por las siguientes razones:

| Criterio | Odoo | Alternativa (SAP Business One) |
|---|---|---|
| Coste de licencia | Gratuito (Community) | De pago (miles de euros/año) |
| Modularidad | Muy modular, instalar solo lo necesario | Paquete completo, menos flexible |
| Facilidad de uso | Interfaz web intuitiva | Interfaz mas compleja |
| Personalizacion | Altamente personalizable con modulos propios | Personalizacion limitada y cara |
| Comunidad | Gran comunidad y documentacion | Comunidad mas reducida |
| Requisitos tecnicos | Bajo (servidor web + PostgreSQL) | Alto (servidor dedicado) |
| Adaptacion a PYME | Excelente | Orientado a empresas grandes |

**Conclusion:** Odoo es la opcion mas adecuada para NexusTech por su coste, flexibilidad y facilidad de personalizacion.

## 3.c. Usuarios, roles y areas funcionales

| Usuario | Rol | Modulos con acceso |
|---|---|---|
| Kristian Garcia (admin) | Administrador | Todos |
| Ana Lopez | Responsable de Ventas | Ventas, CRM, Facturacion, Contactos |
| Carlos Ruiz | Tecnico | Soporte, Proyectos NexusTech |
| Laura Martinez | Responsable de Compras | Compras, Almacen, Contactos |
| Pedro Sanchez | Contable | Contabilidad, Facturacion |
| Sofia Navarro | Responsable RRHH | RRHH, Contactos |

---

# 4. INSTALACION DEL ERP Y SELECCION DE MODULOS

## 4.a. Instalacion de Odoo y creacion de usuarios

Odoo 19.0 se ha instalado mediante Docker en WSL (Windows Subsystem for Linux), con PostgreSQL como base de datos.

Se ha creado una nueva base de datos llamada **nexustech** especificamente para este proyecto, separada de cualquier otra base de datos existente.

El usuario administrador se ha creado automaticamente al crear la base de datos. Los demas usuarios se crearan segun la tabla del punto 3.c, cada uno con acceso unicamente a las areas funcionales que le corresponden.

## 4.b. Modulos instalados

Los siguientes modulos se han instalado en Odoo para cubrir las necesidades detectadas:

| Modulo | Nombre tecnico | Uso |
|---|---|---|
| Punto de Venta | point_of_sale | Venta directa de productos hardware |
| Ventas | sale_management | Gestion de presupuestos y pedidos de venta |
| Compras | purchase | Gestion de pedidos de compra a proveedores |
| Contactos | contacts | Gestion centralizada de clientes y proveedores |
| Recursos Humanos | hr | Gestion de empleados, departamentos y cargos |
| Contabilidad | account | Facturacion, contabilidad y pagos |
| Inventario | stock | Control de stock y almacen |
| CRM | crm | Gestion de oportunidades comerciales |

### Productos en el TPV

Se han importado un minimo de 5 productos para el modulo de Punto de Venta, organizados en varias categorias. Los productos incluyen precio de coste y precio de venta.

### Productos en Compras/Ventas

Se han importado productos tanto de software como de hardware. Los productos de software se han configurado como tipo "Servicio" (no requieren stock fisico) y los de hardware como tipo "Consumible" con stock en almacen.

**Productos distintos para TPV y Compras/Ventas:** Los productos se distinguen segun su categoria y tipo. Los productos hardware se venden tanto por TPV como por pedido de venta, mientras que los servicios de software se gestionan unicamente por pedidos de venta.

### Clientes

Se han importado 14 clientes desde el archivo `1-1-b-ListadoClientes.xlsx`, todos como empresas con sus datos fiscales, direccion y datos de contacto.

### Proveedores

Los proveedores se han asociado a los productos correspondientes. Se han dado de alta al menos 2 proveedores con sus datos completos.

### Recursos Humanos

Se han importado 15 empleados desde el archivo `Lista_empleados_usuario.xlsx`, con sus departamentos y cargos correspondientes. Los departamentos se han creado automaticamente durante la importacion.

## 4.c. Modulo nuevo: NexusTech Proyectos (`nexustech_proyectos`)

Se ha desarrollado un modulo personalizado para la gestion de proyectos IT de la empresa. Este modulo incluye:

### Modelos (3 modelos + herencia)

1. **nexustech.proyecto** - Modelo principal del proyecto
   - `nombre` (Char): Nombre del proyecto
   - `cliente_id` (Many2one -> res.partner): Cliente del proyecto
   - `fecha_inicio` (Date): Fecha de inicio
   - `fecha_fin` (Date): Fecha de fin
   - `presupuesto` (Float): Presupuesto en euros
   - `estado` (Selection): Borrador / En Progreso / Finalizado / Cancelado
   - `imagen` (Image): Imagen del proyecto
   - `horas_estimadas` (Float): Horas estimadas
   - `descripcion` (Text): Descripcion del proyecto
   - `coste_total` (Float, **calculado**): Se calcula automaticamente sumando las horas de todos los registros de las tareas del proyecto y multiplicando por 50 euros/hora
   - `total_horas` (Float, **calculado**): Total de horas registradas en todas las tareas
   - `tarea_ids` (One2many): Relacion con las tareas del proyecto

2. **nexustech.tarea** - Tareas dentro de un proyecto
   - `nombre` (Char): Nombre de la tarea
   - `proyecto_id` (Many2one -> nexustech.proyecto): Proyecto al que pertenece
   - `responsable_id` (Many2one -> res.partner): Responsable de la tarea
   - `prioridad` (Selection): Baja / Media / Alta / Urgente
   - `estado` (Selection): Pendiente / En Progreso / Completada
   - `descripcion` (Text): Descripcion
   - `imagen` (Image): Imagen adjunta
   - `fecha_limite` (Date): Fecha limite
   - `registro_ids` (One2many): Registros de horas

3. **nexustech.registro.horas** - Registro de horas trabajadas
   - `tarea_id` (Many2one -> nexustech.tarea): Tarea
   - `empleado_id` (Many2one -> res.partner): Empleado
   - `fecha` (Date): Fecha
   - `horas` (Float): Horas trabajadas
   - `descripcion` (Text): Descripcion del trabajo

4. **Herencia de res.partner** - Se añaden campos al modelo de contactos
   - `es_cliente_nexustech` (Boolean): Indica si es cliente de NexusTech
   - `nivel_soporte` (Selection): Basico / Estandar / Premium
   - `proyecto_ids` (One2many): Proyectos asociados al contacto

### Vistas

- **Formulario de Proyecto:** Vista completa con imagen, datos generales, datos economicos, pestañas de descripcion y tareas, y chatter para seguimiento.
- **Lista de Proyectos:** Columnas con nombre, cliente, fechas, presupuesto, estado y coste total.
- **Kanban de Proyectos:** Tarjetas agrupadas por estado con imagen, nombre, cliente y presupuesto.
- **Formulario de Tarea:** Imagen, datos de la tarea, y lista editable de registros de horas.
- **Lista de Tareas:** Columnas con nombre, proyecto, responsable, prioridad, estado y fecha limite.
- **Formulario de Registro de Horas:** Datos del registro.
- **Lista de Registros de Horas:** Lista editable inline.
- **Vista heredada de res.partner:** Nueva pestana "NexusTech" en el formulario de contacto con los campos añadidos y la lista de proyectos asociados.

### Menus

- Menu principal: "NexusTech Proyectos"
  - Submenu "Gestion":
    - Proyectos
    - Tareas
    - Registro de Horas

### Permisos

Se han configurado permisos de lectura, escritura, creacion y eliminacion para todos los usuarios en los 3 modelos.

## 4.d. Modificacion de modulo existente: NexusTech CRM Extension (`nexustech_crm_extend`)

Se ha creado un modulo que extiende el modulo CRM (modelo `crm.lead`) añadiendo los siguientes campos:

- `tipo_servicio` (Selection): Consultoria IT / Desarrollo de Software / Soporte Tecnico / Infraestructura / Formacion
- `presupuesto_estimado` (Float): Presupuesto estimado para la oportunidad
- `es_urgente` (Boolean): Indica si la oportunidad es urgente
- `notas_tecnicas` (Text): Notas tecnicas relevantes
- `rentabilidad` (Float, **calculado**): Calcula el porcentaje de rentabilidad comparando el ingreso esperado con el presupuesto estimado

### Vistas modificadas (3 tipos)

1. **Vista FORMULARIO (Form):** Se añade una nueva pestana "NexusTech" al formulario de oportunidades con los campos de tipo de servicio, urgencia, presupuesto estimado, rentabilidad y notas tecnicas.

2. **Vista LISTA (Tree):** Se añaden columnas de tipo de servicio y urgencia a la lista de oportunidades.

3. **Vista BUSQUEDA (Search):** Se añaden filtros para filtrar por urgentes, por tipo de servicio (consultoria, desarrollo), y agrupacion por tipo de servicio.

## 4.e. Plan de copias de seguridad

Se establece el siguiente plan de copias de seguridad:

| Frecuencia | Tipo | Metodo | Retencion |
|---|---|---|---|
| Diaria (lunes a viernes) | Base de datos completa | `pg_dump` automatizado via cron | 7 dias |
| Semanal (domingos) | Base de datos + filestore | Backup completo desde interfaz de Odoo | 4 semanas |
| Mensual | Base de datos + filestore + modulos custom | Backup completo + copia de `/mnt/extra-addons` | 3 meses |

**Procedimiento de restauracion:**
1. Acceder al gestor de bases de datos de Odoo (`/web/database/manager`).
2. Seleccionar "Restaurar base de datos".
3. Subir el archivo de backup y asignarle un nombre.
4. Verificar que la restauracion es correcta accediendo a la base de datos restaurada.

**Comprobacion:** Se recomienda hacer una restauracion de prueba mensualmente para verificar que los backups se restauran correctamente.

---

# 5. PLANIFICACION DE LA MIGRACION

## 5.a. Planificacion detallada

La implantacion se planifica en las siguientes fases, utilizando dias laborables:

| Tarea | Duracion | Inicio | Fin |
|---|---|---|---|
| Instalacion de Odoo y modulos | 1 dia | Dia 1 | Dia 1 |
| Configuracion de modulos | 2 dias | Dia 2 | Dia 3 |
| Formacion de usuarios | 3 dias | Dia 4 | Dia 6 |
| Carga de datos | 2 dias | Dia 7 | Dia 8 |
| Periodo de pruebas | 3 dias | Dia 9 | Dia 11 |
| Migracion definitiva | 1 dia | Dia 12 | Dia 12 |

## 5.b. Diagrama de Gantt

```
DIAGRAMA DE GANTT - PROYECTO DE IMPLANTACION NEXUSTECH

Tarea                          | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |D10 |D11 |D12 |
-------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
Instalacion Odoo y modulos     | ## |    |    |    |    |    |    |    |    |    |    |    |
Configuracion de modulos       |    | ## | ## |    |    |    |    |    |    |    |    |    |
Formacion de usuarios          |    |    |    | ## | ## | ## |    |    |    |    |    |    |
Carga de datos                 |    |    |    |    |    |    | ## | ## |    |    |    |    |
Periodo de pruebas             |    |    |    |    |    |    |    |    | ## | ## | ## |    |
Migracion definitiva           |    |    |    |    |    |    |    |    |    |    |    | ## |
```

**Respuestas a las preguntas de planificacion:**

- **Cuando se hara la instalacion del ERP y modulos?** Dia 1 (primer dia laborable).
- **Cuando se hara la configuracion?** Dias 2-3, justo despues de la instalacion.
- **Cuando se hara la formacion?** Dias 4-6, una vez el sistema este configurado.
- **Cuando se hara la carga de datos?** Dias 7-8, con los usuarios ya formados para que puedan validar.
- **Cuando se hara la migracion definitiva?** Dia 12, tras las pruebas.
- **Cuando se haran las pruebas?** Dias 9-11, justo antes de la migracion.

**Estrategia de migracion:** Se ha optado por una migracion progresiva (no de golpe). Durante el periodo de pruebas (dias 9-11), ambos sistemas (el antiguo con Excel y el nuevo con Odoo) funcionaran en paralelo. Esto permite detectar errores sin afectar al negocio. Una vez validado todo, se hace la migracion definitiva el dia 12 y se deja de usar el sistema antiguo.

---

# 6. PLAN DE FORMACION

## 6.a. Plan de formacion detallado

| Tipo de trabajador | Contenido de la formacion | Duracion | Dia |
|---|---|---|---|
| Administrador (Kristian) | Configuracion completa del sistema, gestion de usuarios, backups, instalacion de modulos | 4h | Dia 4 |
| Comerciales (Ana, Miguel) | Modulo de Ventas, CRM, creacion de presupuestos y pedidos, Punto de Venta | 4h | Dia 4 |
| Responsable de Compras (Laura) | Modulo de Compras, gestion de proveedores, pedidos de compra, recepciones | 3h | Dia 5 |
| Contable (Pedro) | Modulo de Contabilidad, facturacion, cobros y pagos | 3h | Dia 5 |
| Responsable RRHH (Sofia) | Modulo de RRHH, gestion de empleados, departamentos | 2h | Dia 5 |
| Tecnicos (Carlos, Elena) | Modulo NexusTech Proyectos, gestion de tareas y registro de horas | 3h | Dia 6 |
| Almacenero (David) | Modulo de Inventario, entradas, salidas, ajustes de stock | 2h | Dia 6 |
| Todos | Uso basico de Odoo: navegacion, busquedas, filtros, comunicacion interna | 1h | Dia 4 |

**Materiales de formacion:** Se proporcionara un manual de usuario basico (incluido en el apartado 9) y sesiones practicas con el propio sistema. Los cursos del Tema 3 en Moodle tambien sirven como recurso de formacion.

---

# 7. MIGRACION DE LOS PROCESOS DE NEGOCIO Y CARGA DE DATOS

## 7.a. Estrategia de carga de datos

La carga de datos se ha realizado de forma **automatizada** mediante un script de Python que utiliza la API XML-RPC de Odoo. Este metodo es mas fiable que la carga manual ya que:
- Evita errores humanos de entrada de datos.
- Es reproducible (se puede ejecutar multiples veces).
- Permite gestionar duplicados automaticamente.

Los archivos de datos utilizados provienen de la carpeta "Datos para importar-PROYECTO" proporcionada con la tarea.

## 7.b. Archivos importados

| Archivo | Datos que contiene | Registros importados |
|---|---|---|
| `1-1-b-ListadoClientes.xlsx` | Clientes con nombre, contacto, CIF, email, direccion | 14 clientes |
| `4-3-d-ProductosSoftware.xlsx` | Productos de software con nombre, descripcion, precio | 9 productos |
| `ProducHard.xlsx` | Productos de hardware con nombre, precio, categoria | 39 productos |
| `4-3-d-Servicios.xlsx` | Servicios con nombre, descripcion, precio | 8 servicios |
| `Lista_empleados_usuario.xlsx` | Empleados con nombre, departamento, cargo | 15 empleados |

## 7.c. Proceso de importacion (tecnico)

El script `datos/importar_datos.py` realiza los siguientes pasos:

1. **Conexion:** Se conecta a Odoo mediante XML-RPC (protocolo estandar de Odoo para comunicacion externa).
2. **Configuracion de la empresa:** Actualiza los datos de la empresa principal con la informacion de NexusTech Solutions S.L.
3. **Importacion de clientes:** Lee el archivo Excel, extrae los datos de cada fila y crea un registro `res.partner` en Odoo por cada cliente. Antes de crear, comprueba que no exista ya un cliente con el mismo nombre para evitar duplicados.
4. **Importacion de productos:** Lee los archivos de software, hardware y servicios, y crea registros `product.template` con el tipo correspondiente (servicio o consumible).
5. **Importacion de empleados:** Lee el archivo de empleados, crea los departamentos si no existen, y crea registros `hr.employee`.

```python
# Ejemplo de como se importa un cliente
valores = {
    'name': 'UNIPAPER ANDORRA',
    'ref': 'M90125',
    'vat': 'ESA12345678',
    'email': 'info@unipaper.es',
    'city': 'Andorra',
    'customer_rank': 1,
    'is_company': True,
}
modelos.execute_kw(BD, uid, CLAVE, 'res.partner', 'create', [valores])
```

## 7.d. Migracion de procesos

La migracion de cada proceso de negocio al ERP se corresponde con los modulos instalados:

| Proceso antiguo | Herramienta antigua | Modulo Odoo | Estado |
|---|---|---|---|
| Presupuestos y pedidos | Word + Excel | Ventas (sale_management) | Migrado |
| Compras a proveedores | Excel | Compras (purchase) | Migrado |
| Control de stock | Excel compartida | Inventario (stock) | Migrado |
| Facturacion | Word manual | Contabilidad (account) | Migrado |
| Datos de clientes | Excel individuales | Contactos (contacts) + CRM (crm) | Migrado |
| Datos de empleados | Excel | RRHH (hr) | Migrado |
| Soporte tecnico | Email | CRM (crm) | Migrado |
| Proyectos IT | No existia | NexusTech Proyectos (custom) | Nuevo |
| Venta directa | No existia | Punto de Venta (point_of_sale) | Nuevo |

---

# 8. PRUEBAS Y RESOLUCION DE PROBLEMAS

## 8.a. Pruebas a realizar

| Prueba | Descripcion | Resultado esperado |
|---|---|---|
| Verificar clientes | Comprobar que los 14 clientes importados aparecen en Contactos | 14 registros con datos correctos |
| Verificar productos | Comprobar que existen productos de software, hardware y servicios | Minimo 56 productos en total |
| Verificar empleados | Comprobar que los 15 empleados aparecen en RRHH | 15 empleados con departamentos |
| Crear presupuesto | Crear un presupuesto de venta con productos y enviarlo al cliente | Presupuesto generado correctamente |
| Confirmar pedido | Confirmar el presupuesto anterior como pedido de venta | Pedido confirmado, albaran generado |
| Generar factura | Generar factura desde el pedido confirmado | Factura creada con importes correctos |
| Crear pedido de compra | Crear un pedido de compra a un proveedor | Pedido creado, recepcion pendiente |
| Modulo NexusTech | Crear un proyecto, añadir tareas, registrar horas | Coste total calculado correctamente |
| Extension CRM | Crear una oportunidad con tipo de servicio y presupuesto | Campos visibles, rentabilidad calculada |

## 8.b. Errores previstos y soluciones

| Error previsto | Causa posible | Solucion |
|---|---|---|
| Datos duplicados al importar | Ejecutar el script dos veces | El script comprueba duplicados por nombre antes de crear |
| Productos sin precio | Campos vacios en el Excel original | Se asigna precio 0 por defecto, revisar manualmente |
| CIF invalido | Formato incorrecto en el archivo de clientes | Corregir manualmente en Odoo o en el archivo original |
| Modulo custom no aparece | Odoo no encuentra la carpeta de modulos | Configurar `addons_path` en Odoo para incluir la ruta de modulos custom |
| Error al instalar modulo | Dependencias no satisfechas | Verificar que los modulos base estan instalados antes |
| Perdida de datos durante migracion | Fallo del servidor durante la carga | Restaurar backup y repetir la carga |

## 8.c. Errores NO previstos

En caso de encontrar un error no previsto, el procedimiento seria:

1. Anotar el error: que se estaba haciendo, que mensaje aparece, que datos se estaban introduciendo.
2. Comprobar los logs de Odoo (accesibles desde el terminal de Docker o el archivo de log).
3. Buscar el error en la documentacion oficial de Odoo o en foros de la comunidad.
4. Si el error afecta a datos, restaurar el ultimo backup y repetir la operacion con precaucion.
5. Documentar la solucion encontrada para futuras referencias.

---

# 9. DOCUMENTACION DEL PROCESO

Este documento constituye la documentacion completa del proceso de implantacion. A continuacion se incluyen los manuales requeridos.

## 9.a. Documentacion general del proceso

Todo el proceso de implantacion ha quedado documentado en los apartados 1 a 8 de este documento. El proceso ha consistido en:

1. Analizar la empresa ficticia NexusTech Solutions S.L. y detectar sus necesidades.
2. Elegir Odoo como ERP por su coste, flexibilidad y adecuacion a PYMEs.
3. Instalar Odoo 19.0 con Docker y crear la base de datos `nexustech`.
4. Instalar los modulos necesarios: TPV, Ventas, Compras, Contactos, RRHH, Contabilidad, Inventario, CRM.
5. Desarrollar un modulo custom (`nexustech_proyectos`) con 3 modelos y herencia.
6. Extender el modulo CRM con campos y vistas personalizadas.
7. Importar datos reales desde archivos Excel/CSV mediante script automatizado.
8. Planificar pruebas y documentar posibles errores.

## 9.b. Manual de instalacion y configuracion de Odoo

### Requisitos previos
- Docker y Docker Compose instalados (en Linux o WSL).
- Minimo 2 GB de RAM disponible.
- Conexion a internet para descargar imagenes de Docker.

### Instalacion con Docker

1. Crear un archivo `docker-compose.yml` con los servicios de Odoo y PostgreSQL:

```yaml
version: '3'
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - pgdata:/var/lib/postgresql/data

  odoo:
    image: odoo:19.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-data:/var/lib/odoo
      - ./modulos:/mnt/extra-addons
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo

volumes:
  pgdata:
  odoo-data:
```

2. Ejecutar `docker-compose up -d` para levantar los servicios.
3. Acceder a `http://localhost:8069` en el navegador.
4. Crear una nueva base de datos con el boton "Create Database".

### Configuracion de la empresa

1. Ir a Ajustes > Compañias > Mi compañia.
2. Rellenar los datos de NexusTech Solutions S.L. (nombre, direccion, CIF, telefono, email, web).

### Instalacion de modulos

1. Ir a Aplicaciones.
2. Buscar cada modulo por nombre (Punto de Venta, Ventas, Compras, etc.).
3. Hacer clic en "Instalar" para cada uno.

### Instalacion de modulos custom

1. Copiar las carpetas de los modulos custom (`nexustech_proyectos` y `nexustech_crm_extend`) a la carpeta `/mnt/extra-addons` del contenedor de Odoo (o al volumen configurado).
2. Ir a Ajustes > Activar modo desarrollador.
3. Ir a Aplicaciones > Actualizar lista de aplicaciones.
4. Buscar "NexusTech" y hacer clic en "Instalar" para ambos modulos.

## 9.c. Manual de usuario

### Acceso al sistema
1. Abrir el navegador y acceder a `http://localhost:8069`.
2. Seleccionar la base de datos `nexustech`.
3. Introducir el usuario y contraseña proporcionados.

### Navegacion general
- El menu principal se encuentra en la barra superior.
- Cada modulo tiene su propio icono y nombre.
- Dentro de cada modulo, el menu lateral permite acceder a las diferentes funciones.
- Se pueden usar los filtros y la barra de busqueda para encontrar registros rapido.

### Modulo de Ventas: crear un presupuesto
1. Ir a Ventas > Presupuestos > Nuevo.
2. Seleccionar el cliente.
3. Añadir los productos en las lineas del pedido.
4. Guardar y enviar al cliente por email o confirmar directamente.
5. Una vez confirmado, se convierte en pedido de venta.

### Modulo de Compras: crear un pedido
1. Ir a Compras > Pedidos de compra > Nuevo.
2. Seleccionar el proveedor.
3. Añadir los productos a comprar.
4. Confirmar el pedido.
5. Una vez recibida la mercancia, validar la recepcion en Almacen.

### Modulo NexusTech Proyectos
1. Ir a NexusTech Proyectos > Gestion > Proyectos.
2. Crear un nuevo proyecto asignando cliente, fechas y presupuesto.
3. Añadir tareas al proyecto desde la pestana "Tareas".
4. Registrar horas en cada tarea desde la pestana "Registro de Horas" de la tarea.
5. El coste total del proyecto se calcula automaticamente.

### Modulo CRM
1. Ir a CRM > Mi pipeline.
2. Crear una nueva oportunidad.
3. En la pestana "NexusTech" se pueden rellenar el tipo de servicio, presupuesto estimado y notas tecnicas.
4. Los filtros permiten buscar por urgentes o por tipo de servicio.

## 9.d. Manual de administrador

### Gestion de usuarios
1. Ir a Ajustes > Usuarios y compañias > Usuarios.
2. Crear un nuevo usuario con nombre y email.
3. Asignar los permisos correspondientes marcando las casillas de acceso a cada modulo.

### Copias de seguridad
1. Acceder a `/web/database/manager`.
2. Seleccionar "Backup" junto a la base de datos.
3. Elegir formato (zip recomendado) y descargar.
4. Guardar el backup en una ubicacion segura.

### Restaurar backup
1. Acceder a `/web/database/manager`.
2. Seleccionar "Restore Database".
3. Subir el archivo de backup y asignarle un nombre de base de datos.
4. Verificar el contenido de la base de datos restaurada.

### Actualizar modulos custom
1. Si se modifica el codigo de un modulo, reiniciar el servicio de Odoo.
2. Ir a Aplicaciones > buscar el modulo > hacer clic en los tres puntos > "Actualizar".
3. Verificar que los cambios se aplican correctamente.

---

**Enlace al repositorio con los modulos desarrollados:** [https://github.com/kristiangarcia/Proyecto_Implantacion_SGE](https://github.com/kristiangarcia/Proyecto_Implantacion_SGE)
