# -*- coding: utf-8 -*-
from odoo import models, fields


class RegistroHoras(models.Model):
    """Modelo para registrar horas trabajadas en cada tarea."""
    _name = 'nexustech.registro.horas'
    _description = 'Registro de Horas'

    tarea_id = fields.Many2one('nexustech.tarea', string='Tarea', required=True, ondelete='cascade')
    empleado_id = fields.Many2one('res.partner', string='Empleado', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    horas = fields.Float(string='Horas Trabajadas', required=True)
    descripcion = fields.Text(string='Descripción del Trabajo')
