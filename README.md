# Proyecto de Implantacion SGE - Odoo

Proyecto de implantacion de un ERP (Odoo 19.0) para la empresa ficticia **NexusTech Solutions S.L.**, una empresa de soluciones tecnologicas (software, hardware y servicios IT).

Asignatura: Sistemas de Gestion Empresarial - 2 DAM

Alumno: Kristian Olav Garcia Paulsen

## Estructura del repositorio

```
├── modulos/
│   ├── nexustech_proyectos/      # Modulo custom: Gestion de proyectos IT
│   └── nexustech_crm_extend/     # Extension del modulo CRM
├── datos/
│   └── importar_datos.py         # Script de importacion via XML-RPC
├── documentacion/
│   ├── proyecto_implantacion.md  # Documentacion completa (fuente)
│   └── proyecto_implantacion.pdf # Documentacion en PDF
```

## Modulos desarrollados

### nexustech_proyectos

Modulo personalizado para la gestion de proyectos IT. Incluye:

- 3 modelos: Proyecto, Tarea y Registro de Horas
- Relaciones Many2one entre modelos
- Campos calculados (coste total a partir de horas registradas)
- Campo de imagen en todos los modelos
- Herencia de `res.partner` con campos adicionales
- Vistas: formulario, lista y kanban
- Menus y permisos de acceso

### nexustech_crm_extend

Extension del modulo CRM que añade al modelo `crm.lead`:

- Campos: tipo de servicio, presupuesto estimado, urgencia, notas tecnicas
- Campo calculado: rentabilidad
- Vistas modificadas: formulario (nueva pestana), lista (columnas extra), busqueda (filtros y agrupacion)

## Modulos de Odoo instalados

| Modulo | Nombre tecnico |
|--------|---------------|
| Punto de Venta | `point_of_sale` |
| Ventas | `sale_management` |
| Compras | `purchase` |
| Contactos | `contacts` |
| Recursos Humanos | `hr` |
| Contabilidad | `account` |
| Inventario | `stock` |
| CRM | `crm` |

## Carga de datos

El script `datos/importar_datos.py` importa automaticamente via XML-RPC:

- 14 clientes
- 9 productos de software
- 39 productos de hardware
- 8 servicios
- 15 empleados con departamentos

## Requisitos

- Docker y Docker Compose
- Python 3 con `openpyxl`
- Odoo 19.0 con PostgreSQL
