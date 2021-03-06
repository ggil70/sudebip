
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
# from osv import fields,osv --- <8.0.X
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date, datetime,timedelta
from odoo import api
from time import time
formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging
#Definimos la Variable Global
codigo_ad = ''
_logger = logging.getLogger(__name__)



########### Clasificacin de lo Bienes (SUDEBIP)###############################
class catalogo_sudebi(models.Model):
    """Registra la Clasificacion de Bienes (SUDEBIP)"""
    _name = 'catalogo_sudebi'
    #_rec_name = 'catalogo_sudebi_codigo'
    _rec_name = 'catalogo_sudebi_nombre'
    catalogo_sudebi_codigo   = fields.Char(string='Codigo de la Categoria',size=10,required=True, help='Codigo de la Categoria General de la (SUDEBIP)')
    catalogo_sudebi_nombre   = fields.Char(string='Nombre de la Categoria',size=100,required=True, help='Nombre de la Categoria General de la (SUDEBIP)')
   
    _sql_constraints = [('catalogo_sudebi_codigo', 'unique(catalogo_sudebi_codigo)', 'El C??digo debe se ??nico!')]
    _sql_constraints = [('catalogo_sudebi_nombre', 'unique(catalogo_sudebi_nombre  )', 'El Nombre debe se ??nico!')]


class catalogo_sudebi_sub(models.Model):
     """Registra la Sub-Clasificacion de Bienes (SUDEBIP)"""
     _name = 'catalogo_sudebi_sub'
     #_rec_name = 'catalogo_sudebi_sub_codigo'
     _rec_name = 'catalogo_sudebi_sub_nombre'
     #_rec_name = 'catalogo_sudebi_id'
    
     catalogo_sudebi_sub_codigo  = fields.Char(string='Codigo de la SubCategoria',size=10,required=True, help='Codigo de la Categoria Sub-General de la (SUDEBIP)')
     catalogo_sudebi_sub_nombre  = fields.Char(string='Nombre de la SubCategoria',size=100,required=True, help='Nombre de la Categoria Sub-General de la (SUDEBIP)')
     catalogo_sudebi_id          = fields.Many2one('catalogo_sudebi',string='Categoria General', help='Registra el C??digo de vinculacion con la Categoria General ')
     catalogo_sudebi_codigo      = fields.Char(string='Codigo de la Categoria',size=10,required=True, help='Codigo de la Categoria General de la (SUDEBIP)')


     @api.onchange('catalogo_sudebi_id')
     def onchange_catalogo(self):
        codigo= ''
        codigo = self.catalogo_sudebi_id.catalogo_sudebi_codigo
        self.catalogo_sudebi_codigo =  codigo





     _sql_constraints = [('catalogo_sudebi_sub_codigo', 'unique(catalogo_sudebi_sub_codigo)', 'El C??digo debe se ??nico!')]
     _sql_constraints = [('catalogo_sudebi_sub_nombre','unique(catalogo_sudebi_sub_nombre)', 'El Nombre debe se ??nico!')]



class catalogo_sudebi_esp(models.Model):
     """Registra la Especifico de Bienes (SUDEBIP)"""
     _name = 'catalogo_sudebi_esp'
     #_rec_name = 'catalogo_sudebi_esp_codigo'
     _rec_name = 'catalogo_sudebi_esp_nombre'
     #_rec_name = 'catalogo_sudebi_sub_id'
   
     catalogo_sudebi_esp_codigo   = fields.Char(string='Codigo de la Categoria Espec??fica',size=10,required=True, help='Codigo de la Categoria Especifica de la (SUDEBIP)')
     catalogo_sudebi_esp_nombre   = fields.Char(string='Nombre de la Categoria Espec??fica',size=100,required=True, help='Nombre de la Categoria  Especifica de la (SUDEBIP)')
     catalogo_sudebi_sub_id       = fields.Many2one('catalogo_sudebi_sub',string='Sub-Categoria ', help='Registra el C??digo de vinculacion con la Categoria Sub-General ')
     catalogo_sudebi_sub_codigo  = fields.Char(string='Codigo de la Sub-Categoria',size=10,required=True, help='Codigo de la Categoria Sub-General de la (SUDEBIP)')
     catalogo_sudebi_id          = fields.Many2one('catalogo_sudebi',string='Categoria General', help='Registra el C??digo de vinculacion con la Categoria General ')
     catalogo_sudebi_codigo      = fields.Char(string='Codigo de la Categoria',size=10,required=True, help='Codigo de la Categoria General de la (SUDEBIP)')


     @api.onchange('catalogo_sudebi_sub_id')
     def onchange_catalogo_sub(self):
        codigosu= ''
        codigosu = self.catalogo_sudebi_sub_id.catalogo_sudebi_sub_codigo
        self.catalogo_sudebi_sub_codigo =  codigosu




     @api.onchange('catalogo_sudebi_id')
     def onchange_catalogo(self):
        codigo= ''
        codigo = self.catalogo_sudebi_id.catalogo_sudebi_codigo
        self.catalogo_sudebi_codigo =  codigo


     _sql_constraints = [('catalogo_sudebi_esp_codigo', 'unique(catalogo_sudebi_esp_codigo)', 'El C??digo debe se ??nico!')]

     _sql_constraints = [('catalogo_sudebi_esp_nombre','unique( catalogo_sudebi_sub_id,catalogo_sudebi_esp_nombre)', 'El Nombre debe se ??nico!')]
 


class color_sudebi(models.Model):
    """Registra el Color de los Bienes segun SUDEBIP"""
    _name = 'color_sudebi'
    #_rec_name = 'color_sudebi_codigo'
    _rec_name = 'color_sudebi_nombre'
   
    color_sudebi_codigo = fields.Char(string='Codigo del Color segun Sudebip',size=3, help='Registra el Codigo de Color segun (SUDEBIP)')
    color_sudebi_nombre = fields.Char(string='Nombre del Color segun Sudebip',size=100,required=True, help='Registra el Nombre del Color')
   
    _sql_constraints = [('color_sudebi_codigo', 'unique(color_sudebi_codigo)', 'El C??digo debe se ??nico!')]    
    _sql_constraints = [('color_sudebi_nombre', 'unique(color_sudebi_nombre)', 'El Color debe se ??nico!')]     




class clase_sudebi(models.Model):
     """Registra las Clases de Vehiculos"""
     _name = 'clase_sudebi'
     # _rec_name = 'clase_sudebi_codigo'
     _rec_name = 'clase_sudebi_nombre'
                
    
     clase_sudebi_codigo   = fields.Char(string='Codigo de Clase de Veh??culos',size=3,required=True, help='Registra el Codigo de Clase de Veh??culos (SUDEBIP)')
     clase_sudebi_nombre   = fields.Char(string='Nombre de Clase de Veh??culos',size=100,required=True, help='Registra el Nombre de la Clase de Veh??culos(SUDEBIP)')
    


     @api.onchange('clase_sudebi_nombre')
     def onchange_nombre(self):
        self.clase_sudebi_nombre = self.clase_sudebi_nombre.upper()
  
     _sql_constraints = [('clase_sudebi_codigo', 'unique(clase_sudebi_codigo)', 'El C??digo debe se ??nico!')]
     _sql_constraints = [('clase_sudebi_nombre', 'unique(clase_sudebi_nombre)', 'El Nombre debe se ??nico!')]     





