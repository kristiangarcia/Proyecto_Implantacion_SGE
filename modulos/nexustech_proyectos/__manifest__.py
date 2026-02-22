# -*- coding: utf-8 -*-
{
    'name': 'NexusTech Proyectos',
    'version': '1.0',
    'summary': 'Gestión de proyectos IT para NexusTech Solutions S.L.',
    'description': """
        Módulo personalizado para la gestión de proyectos tecnológicos.
        Incluye gestión de proyectos, tareas y registro de horas.
        Desarrollado como parte del Proyecto de Implantación - SGE 2º DAM.
    """,
    'author': 'Kristian Olav García Paulsen',
    'category': 'Servicios/Proyectos',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/proyecto_vistas.xml',
        'views/tarea_vistas.xml',
        'views/registro_horas_vistas.xml',
        'views/partner_vistas.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
