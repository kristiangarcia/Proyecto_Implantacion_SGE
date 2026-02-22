# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Proyecto(models.Model):
    """Modelo para gestionar proyectos IT de NexusTech."""
    _name = 'nexustech.proyecto'
    _description = 'Proyecto IT'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    nombre = fields.Char(string='Nombre del Proyecto', required=True, tracking=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True, tracking=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    fecha_fin = fields.Date(string='Fecha de Fin')
    presupuesto = fields.Float(string='Presupuesto (€)', digits=(10, 2))
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado', default='borrador', tracking=True)
    imagen = fields.Image(string='Imagen del Proyecto', max_width=256, max_height=256)
    horas_estimadas = fields.Float(string='Horas Estimadas')
    descripcion = fields.Text(string='Descripción')
    tarea_ids = fields.One2many('nexustech.tarea', 'proyecto_id', string='Tareas')

    # Campo calculado: coste total basado en horas registradas
    coste_total = fields.Float(
        string='Coste Total (€)',
        compute='_calcular_coste_total',
        store=True,
        digits=(10, 2),
    )
    total_horas = fields.Float(
        string='Total Horas Registradas',
        compute='_calcular_coste_total',
        store=True,
    )

    @api.depends('tarea_ids.registro_ids.horas')
    def _calcular_coste_total(self):
        """Calcula el coste total sumando las horas de todos los registros
        de las tareas del proyecto, multiplicado por 50€/hora."""
        for proyecto in self:
            total = 0.0
            for tarea in proyecto.tarea_ids:
                for registro in tarea.registro_ids:
                    total += registro.horas
            proyecto.total_horas = total
            proyecto.coste_total = total * 50.0  # 50€ por hora
