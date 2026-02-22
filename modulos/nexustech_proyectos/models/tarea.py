# -*- coding: utf-8 -*-
from odoo import models, fields


class Tarea(models.Model):
    """Modelo para gestionar tareas dentro de un proyecto."""
    _name = 'nexustech.tarea'
    _description = 'Tarea de Proyecto'

    nombre = fields.Char(string='Nombre de la Tarea', required=True)
    proyecto_id = fields.Many2one('nexustech.proyecto', string='Proyecto', required=True, ondelete='cascade')
    responsable_id = fields.Many2one('res.partner', string='Responsable')
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ], string='Prioridad', default='media')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ], string='Estado', default='pendiente')
    descripcion = fields.Text(string='Descripción')
    imagen = fields.Image(string='Imagen Adjunta', max_width=256, max_height=256)
    fecha_limite = fields.Date(string='Fecha Límite')
    registro_ids = fields.One2many('nexustech.registro.horas', 'tarea_id', string='Registros de Horas')
