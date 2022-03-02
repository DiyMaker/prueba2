# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas2(models.Model):
    _name = 'lista_tareas2.lista_tareas2'
    _description = 'lista_tareas2.lista_tareas2'

    avatar = fields.Image('Imagen tarea', max_width=50,max_heigth=50)
    fecha = fields.Date()
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    descripcion = fields.Text()

    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>6:
                record.urgente = True
            else:
                record.urgente = False
