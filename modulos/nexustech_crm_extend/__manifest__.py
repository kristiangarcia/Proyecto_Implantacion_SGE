# -*- coding: utf-8 -*-
{
    'name': 'NexusTech CRM Extensión',
    'version': '1.0',
    'summary': 'Extensión del módulo CRM para NexusTech Solutions S.L.',
    'description': """
        Módulo que extiende el modelo crm.lead (oportunidades) añadiendo
        un campo personalizado y nuevas vistas.
        Desarrollado como parte del Proyecto de Implantación - SGE 2º DAM.
    """,
    'author': 'Kristian Olav García Paulsen',
    'category': 'Ventas/CRM',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_vistas.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
