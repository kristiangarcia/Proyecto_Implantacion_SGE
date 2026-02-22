# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    """Extensión del modelo crm.lead para añadir campos de NexusTech."""
    _inherit = 'crm.lead'

    tipo_servicio = fields.Selection([
        ('consultoria', 'Consultoría IT'),
        ('desarrollo', 'Desarrollo de Software'),
        ('soporte', 'Soporte Técnico'),
        ('infraestructura', 'Infraestructura'),
        ('formacion', 'Formación'),
    ], string='Tipo de Servicio', help='Tipo de servicio que solicita el cliente')

    presupuesto_estimado = fields.Float(
        string='Presupuesto Estimado (€)',
        digits=(10, 2),
        help='Presupuesto estimado para esta oportunidad',
    )

    es_urgente = fields.Boolean(
        string='¿Es Urgente?',
        default=False,
        help='Marcar si la oportunidad requiere atención urgente',
    )

    notas_tecnicas = fields.Text(
        string='Notas Técnicas',
        help='Notas técnicas relevantes para esta oportunidad',
    )

    rentabilidad = fields.Float(
        string='Rentabilidad (%)',
        compute='_calcular_rentabilidad',
        store=True,
        digits=(5, 2),
    )

    @api.depends('expected_revenue', 'presupuesto_estimado')
    def _calcular_rentabilidad(self):
        """Calcula la rentabilidad como porcentaje de ingreso esperado vs presupuesto."""
        for registro in self:
            if registro.presupuesto_estimado > 0:
                registro.rentabilidad = (
                    (registro.expected_revenue - registro.presupuesto_estimado)
                    / registro.presupuesto_estimado * 100
                )
            else:
                registro.rentabilidad = 0.0
