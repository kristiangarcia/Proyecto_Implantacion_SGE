# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    """Herencia de res.partner para añadir campos específicos de NexusTech."""
    _inherit = 'res.partner'

    es_cliente_nexustech = fields.Boolean(string='¿Es Cliente NexusTech?', default=False)
    nivel_soporte = fields.Selection([
        ('basico', 'Básico'),
        ('estandar', 'Estándar'),
        ('premium', 'Premium'),
    ], string='Nivel de Soporte')
    proyecto_ids = fields.One2many('nexustech.proyecto', 'cliente_id', string='Proyectos Asociados')
