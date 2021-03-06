
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





"""Inicio de Registro Categorias de Unidades Administrativas"""


class uniadm_sudebi(models.Model):
     """Registra Categorias de Unidades Administrativas segun Sudebip"""
     _name = 'uniadm_sudebi'
     #_rec_name = 'uniadm_sudebi_codigo'
     _rec_name = 'uniadm_sudebi_nombre'
    
     uniadm_sudebi_codigo = fields.Char(string='Codigo de Categorias de Unidades Administrativas',size=3,required=True, help='Registra el Codigo de la Categoria de Oficina (SUDEBIP)')
     uniadm_sudebi_nombre = fields.Char(string='Nombre de Categorias de Unidades Administrativas',size=100,required=True, help='Registra el Nombre de la Categoria de Oficina (SUDEBIP)')
    
     _sql_constraints = [('uniadm_sudebi_codigo', 'unique(uniadm_sudebi_codigo)', 'El C??digo debe se ??nico!')]
     _sql_constraints = [('uniadm_sudebi_nombre', 'unique(uniadm_sudebi_nombre)', 'El Nombre debe se ??nico!')]



"""Fin de Registro Categorias de Unidades Administrativas"""


"""Inicio de Registro tipos de Lugares de Ubicacion"""

class tipos_lugares_ubicacion_sudebip(models.Model):
     """Registra los tipos de Lugares de Ubicacion"""
     _name = 'tipos_lugares_ubicacion_sudebip'
     #_rec_name = 'oficinas_codigo'
     _rec_name = 'nombre_lugar'
   
    
    
     codigo_lugar       = fields.Char(string='Codigo del Tipo o Lugar de Ubicaci??n',size=3,required=True, help='Registra el Codigo del Tipo o Lugar de Ubicaci??n')
     nombre_lugar       = fields.Char(string='Nombre del Tipo o Lugar de Ubicaci??n',size=100,required=True, help='Registra el Nombre del Tipo o Lugar de Ubicaci??n')
     

     #_sql_constraints = [('regiones_codigo ', 'unique(regiones_codigo)', 'El C??digo debe se ??nico!')] 
     _sql_constraints = [('nombre_lugar', 'unique(nombre_lugar)', 'El Nombre debe se ??nico!')] 


"""Fin de Registro tipos de Lugares de Ubicacion"""

"""Inicio de Registro Paises"""


class paises(models.Model):
     """Division Geopolitica"""
     _name = 'paises'
     #_rec_name = 'codigo'
     _rec_name = 'pais'

     codigo_pais = fields.Char(string='Codigo del Pa??s',size=3,required=True, help='Registra el C??digo de Identificaci??n Pa??s')
     pais = fields.Char(string='Pa??s',size=150,required=True, help='Registra el nombre del Pa??s')
     selepa = fields.Boolean (string='Seleccionado', help='Registra si el Pa??s aplica para el organismo')
    
     _sql_constraints = [('paises', 'unique(codigo_pais)', 'El C??digo debe se ??nico!')]


     _defaults={ 
        'selepa': True,
     }

"""Fin de Registro Paises"""

"""Inicio de Registro Estados"""

class mppp_reg_pro_estados(models.Model):
     """Registro de  Esstados del Pais"""
     _name = 'mppp_reg_pro_estados'
     #_rec_name = 'codigo'
     _rec_name = 'estado'

     codigo_estado = fields.Char(string='Codigo del Estado',size=2,required=True, help='Registra el C??digo de Identificaci??n del Estado del Pa??s')
     estado = fields.Char(string='Estado',size=30,required=True, help='Registra el nombre del estado')
     seledo = fields.Boolean (string='Seleccionado', help='Registra si el estado aplica para el organismo')
    
     _sql_constraints = [('mppp_reg_pro_estados', 'unique(codigo_estado)', 'El C??digo debe se ??nico!')]


     _defaults={ 
        'seledo': True,
     }

"""Fin de Registro Estados"""


"""Inicio de Registro Municipios"""

class mppp_reg_pro_municipios(models.Model):
     """Registro de Municipios"""
     _name = 'mppp_reg_pro_municipios'
     #_rec_name = 'codigo'
     _rec_name = 'municipio'
     #_rec_name = 'estado_id'
    
    
     codigo_municipio  = fields.Char(string='Codigo del Municipio',size=10,required=True, help='Registra el C??digo de Identificaci??n del Municipio del Estado del Pa??s')
     municipio      = fields.Char(string='Municipio',size=30,required=True, help='Registra el nombre del Municipio')
     estado_id      = fields.Many2one('mppp_reg_pro_estados',string='Estado', help='Registra el Codigo de Vinculaci??n con el Estado al cual pertenece el Municipio')
     codigo_estado = fields.Char(string='Codigo del Estado',size=2,required=True, help='Registra el C??digo de Identificaci??n del Estado del Pa??s')
     codigo_sudebip_municipio = fields.Char(string='Codigo del Municipio por la SUDEBIP',size=10,required=True, help='Registra el C??digo de Identificaci??n del Municipio del Estado del Pa??s, Segun SUDEBIP')
     selemu    = fields.Boolean (string='Seleccionado', default ="True", help='Registra si el municipio aplica para el organismo')
     _sql_constraints = [('mppp_reg_pro_municipios', 'unique(estado_id,codigo_municipio)', 'El C??digo del Municipio debe se ??nico!')] 
     _sql_constraints = [('reg_pro_municipios_sudebip', 'unique(estado_id,codigo_municipio,codigo_sudebip)', 'El C??digo de SUDEBIP debe se ??nico!')] 
    
     _defaults = { 
        'selemu': True
     }
    

"""Fin de Registro Municipios"""

"""Inicio de Registro Parroquias"""


class mppp_reg_pro_parroquias(models.Model):
     """Registro de Parroquias"""
     _name = 'mppp_reg_pro_parroquias'
     #_rec_name = 'codigo'
     _rec_name = 'parroquia'
     #_rec_name = 'municipios_id'
    
     estado_id      = fields.Many2one('mppp_reg_pro_estados',string='Estado', help='Registra el Codigo de Vinculaci??n con el Estado al cual pertenece el Municipio')
     codigo_estado = fields.Char(string='Codigo del Estado',size=2,required=True, help='Registra el C??digo de Identificaci??n del Estado del Pa??s')
     municipios_id = fields.Many2one('mppp_reg_pro_municipios',string='Municipios', help='Registra el Codigo de Vinculaci??n con el Municipio al cual pertenece la Parroquia')
     codigo_municipio  = fields.Char(string='Codigo del Municipio',size=10,required=True, help='Registra el C??digo de Identificaci??n del Municipio del Estado del Pa??s')
     codigo_parroquia  = fields.Char(string='Codigo de la Parroquia',size=10,required=True, help='Registra el C??digo de Identificaci??n de la Parroquia del Municipio del Estado')
     parroquia     = fields.Char(string='Parroquia',size=30,required=True, help='Registra el nombre de la Parroquia')
     
     codigo_sudebip_parroquia = fields.Char(string='Codigo de la Parroquia por la SUDEBIP',size=10,required=True, help='Registra el Identificaci??n de la Parroquia del Municipio del Pa??s segun SUDEBIP')
     selepa        = fields.Boolean (string='Seleccionado', default ="True", help='Registra si la parroquia aplica para el organismo')
     _sql_constraints = [('mppp_reg_pro_parroquias', 'unique(municipios_id,codigo_parroquia)', 'El C??digo de la Parroquia debe se ??nico!')] 
     _sql_constraints = [('reg_pro_parroquias_sudebip', 'unique(municipios_id,codigo_parroquia,codigo_sudebip)', 'El C??digo de SUDEBIP debe se ??nico!')]       
    
     _defaults = { 
          'selepa': True
     }


"""Fin de Registro Parroquias"""

"""Inicio de Registro Ciudades"""

class mppp_reg_pro_ciudad(models.Model):
     """Registro de Ciudadades"""
     _name = 'mppp_reg_pro_ciudad'
     #_rec_name = 'codigo'
     _rec_name = 'ciudad'
     #_rec_name = 'municipios_id'
    
     estado_id      = fields.Many2one('mppp_reg_pro_estados',string='Estado', help='Registra el Codigo de Vinculaci??n con el Estado al cual pertenece el Municipio')
     codigo_estado = fields.Char(string='Codigo del Estado',size=2,required=True, help='Registra el C??digo de Identificaci??n del Estado del Pa??s')
     codigo_municipio  = fields.Char(string='Codigo del Municipio',size=10,required=True, help='Registra el C??digo de Identificaci??n del Municipio del Estado del Pa??s')
     municipios_id = fields.Many2one('mppp_reg_pro_municipios',string='Municipios', help='Registra el Codigo de Vinculaci??n con el Municipio al cual pertenece la Ciudad')
     codigo_sudebip_ciudad = fields.Char(string='Codigo de la Ciudad por la SUDEBIP',size=10,required=True, help='Registra el Identificaci??n de la Ciudad del Municipio del Pa??s segun SUDEBIP')
     codigo_ciudad  = fields.Char(string='Codigo de la Ciudad',size=10,required=True, help='Registra el C??digo de Identificaci??n de la Ciudad del Municipio del Estado')
     ciudad        = fields.Char(string='Ciudad',size=30,required=True, help='Registra el nombre de la Ciudad')

     seleci        = fields.Boolean (string='Seleccionado', help='Registra si la ciduda aplica para el organismo')

     _sql_constraints = [('mppp_reg_pro_ciudad', 'unique(municipios_id,codigo_ciudad)', 'El C??digo de la Ciudad debe se ??nico!')] 
     _sql_constraints = [('reg_pro_ciudad_sudebip', 'unique(municipios_id,codigo_ciudad,codigo_sudebip)', 'El C??digo de SUDEBIP debe se ??nico!')]       
     
     _defaults = { 
        'seleci': True
     }


"""Fin de Registro de Ciudad"""


"""Inicio de Registro las Oficinas del Ministerio"""
class regiones(models.Model):
     """Registra las Regiones del Ministerio"""
     _name = 'regiones'
     #_rec_name = 'oficinas_codigo'
     _rec_name = 'regiones_nombre'
   
        
     regiones_codigo       = fields.Char(string='Codigo de la Regi??n',size=3,required=True, help='Registra el Codigo de la Regi??n')
     regiones_nombre       = fields.Char(string='Nombre de la Regi??n',size=100,required=True, help='Registra el Nombre de la Regi??n')
     #resp_uso_region_id   = fields.Many2one('personas',string= 'Responsable del Bien por la Region', domain="[('oficinas_id','=',id)]",size=3, help='Responsable de la Regi??n')    

     #_sql_constraints = [('regiones_codigo ', 'unique(regiones_codigo)', 'El C??digo debe se ??nico!')] 
     _sql_constraints = [('regiones_nombre', 'unique(regiones_nombre)', 'El Nombre debe se ??nico!')] 

"""Fin de Registro las Regiones del Ministerio"""


"""Inicio de Registro las Sedes del Ministerio"""

class sedes(models.Model):
     """Registra las Sedes del Ministerio"""
     _name = 'sedes'
     #_rec_name = 'oficinas_codigo'
     _rec_name = 'sedes_nombre'
     # _rec_name = 'oficinas_padre_id'
     #_rec_name = 'uniadm_sudebi_codigo'
    
    
     sedes_codigo       = fields.Char(string='C??digo de la Sede',size=7,required=True, help='Registra el C??digo de la Sede')
     sedes_nombre       = fields.Char(string='Nombre de la Sede',size=100,required=True, help='Registra el Nombre de la Sede')     
     pais_id            = fields.Many2one('paises', string='Pa??s de Ubicaci??n de la Sede',size=3, required=True, domain= "[('selepa','=','TRUE')]",help='Regiones de Ubicaci??n de la Sede')    
     codigo_pais        = fields.Char(string='Codigo del Pa??s',size=3,required=True, help='Registra el C??digo de Identificaci??n Pa??s')
     tipo_localizacion  = fields.Selection([('N','Nacional'),('I','Internacional')], string='Tipo de Localizaci??n',size=2,required=True,help='Tipo de Localizaci??n de la Sede')
     lugar_id           = fields.Many2one('tipos_lugares_ubicacion_sudebip', string='Tipo o Lugar de Ubicaci??n',size=3, required=True,help='Tipo o Lugar de Ubicaci??n de la Sede seg??n SUDEBIP')    
     regiones_id        = fields.Many2one('regiones', string='Regiones de Ubicaci??n de la Sede',size=3, required=True,help='Regiones de Ubicaci??n de la Sede')    
     regiones_codigo    = fields.Char(string='Codigo de la Regi??n',size=3,required=True, help='Registra el Codigo de la Regi??n')
     estado_id          = fields.Many2one('mppp_reg_pro_estados','Entidad Federal',required=True,  domain="[('seledo','=','TRUE')]",help='Registra La Entidad Federal donde se Encuentra el Bien')
     codigo_estado      = fields.Char(string='Codigo del Estado',size=2,required=True, help='Registra el C??digo de Identificaci??n del Estado del Pa??s')
     municipios_id      = fields.Many2one('mppp_reg_pro_municipios','Municipio',required=True, domain="[('estado_id','=',estado_id)]", help='Registra el Municipio donde se la Sede')
     codigo_municipio   = fields.Char(string='Codigo del Municipio',size=10,required=True, help='Registra el C??digo de Identificaci??n del Municipio del Estado del Pa??s')
     parroquias_id      = fields.Many2one('mppp_reg_pro_parroquias','Parroquia',required=True,  domain="[('municipios_id','=', municipios_id)",help='Registra la Parroquia donde se Encuentra la Sede')
     codigo_parroquia   = fields.Char(string='Codigo de la Parroquia',size=10,required=True, help='Registra el C??digo de Identificaci??n de la Parroquia del Municipio del Estado')
     ciudad_id          = fields.Many2one('mppp_reg_pro_ciudad','Ciudad',required=True,  domain="[('municipios_id','=',municipios_id)]",help='Registra la Ciudad  donde se Encuentra la Sede')
     codigo_ciudad      = fields.Char(string='Codigo de la Ciudad',size=10,required=True, help='Registra el C??digo de Identificaci??n de la Ciudad del Municipio del Estado')
     urbanizacion  = fields.Char(string='Urbanizaci??n Calle o Avenida donde se localiza la sede del ??rgano o Ente',size=100,
                     required=True, help='Registra la  Urbanizaci??n donde se localiza la sede del ??rgano o Ente')
     calle         = fields.Char(string=' Calle o Avenida donde se localiza la sede del ??rgano o Ente',size=100,
                     required=True, help='Registra la  Calle o Avenida donde se localiza la sede del ??rgano o Ente')
     casa_edificio  = fields.Char(string=' Casa o Edificio donde se localiza la sede del ??rgano o Ente',size=100,
                     required=True, help='Registra la   Casa o Edificio donde se localiza la sede del ??rgano o Ente')
     piso_sede     = fields.Char(string=' Piso (si aplica) donde se localiza la sede del ??rgano o Ente',size=100,
                     help='Registra la  Calle o Avenida donde se localiza la sede del ??rgano o Ente')

     resp_uso_sede_id   = fields.Many2one('personas',string= 'Responsable del Bien por la Sede', domain="[('personas_sedes_id','=',id)]",size=3, help='Responsable de los  Bienes por la Sede')    

   #  resp_pat_id = fields.Many2one('personas', 'Responsable Patrimonial', size=3,domain="[('tipo_resp','=','D')]", help='Registra el Responsable Patrimonial de la Sede')

     _sql_constraints = [('sedes_codigo ', 'unique(sedes_codigo)', 'El C??digo debe se ??nico!')] 
     _sql_constraints = [('sedes_nombre', 'unique(sedes_nombre)', 'El Nombre debe se ??nico!')] 


     @api.onchange('pais_id')
     def onchange_pais(self):
        codigo= ''
        codigo = self.pais_id.codigo_pais
        self.codigo_pais =  codigo 


     @api.onchange('regiones_id')
     def onchange_region(self):
        codigo= ''
        codigo = self.regiones_id.regiones_codigo
        self.regiones_codigo =  codigo

     @api.onchange('estado_id')
     def onchange_estado(self):
        codigo= ''
        codigo = self.estado_id.codigo_estado
        self.codigo_estado =  codigo

     @api.onchange('municipios_id')
     def onchange_municipio(self):
        codigo= ''
        codigo = self.municipios_id.codigo_municipio
        self.codigo_municipio =  codigo

     @api.onchange('parroquias_id')
     def onchange_parroquia(self):
        codigo= ''
        codigo = self.parroquias_id.codigo_parroquia
        self.codigo_parroquia =  codigo

     @api.onchange('ciudad_id')
     def onchange_ciudad(self):
        codigo= ''
        codigo = self.ciudad_id.codigo_ciudad
        self.codigo_ciudad =  codigo



"""Fin de Registro las Sedes del Ministerio"""


"""Inicio de Registro Oficinas"""


class oficinas(models.Model):
     """Registra las Oficinas del Ministerio"""
     _name = 'oficinas'
     #_rec_name = 'oficinas_codigo'
     _rec_name = 'oficinas_nombre'
     _order = 'orden desc'
     # _rec_name = 'oficinas_padre_id'
     #_rec_name = 'uniadm_sudebi_codigo'
    
    
     oficinas_codigo       = fields.Char(string='Nomenclatura de la Oficina',size=20,required=True, help='Registra la Nomenclatura de la Oficina')
     oficinas_nombre       = fields.Char(string='Nombre de la Oficina',size=200,required=True, help='Registra el Nombre de la Oficina')
     uniadm_sudebi_codigo  = fields.Many2one('uniadm_sudebi',string='Categorias Administrativas (SUDEBIP)', required=True, help='Registra el Codigo de Vinculacion con las Categorias de Unidades Administrativas segun Sudebi ')
     oficinas_padre_id     = fields.Many2one('oficinas',string='Unidad de Adscripci??n')
     regiones_id           = fields.Many2one('regiones',string= 'Regiones de Ubicaci??n de la Sede',size=3, required=True,help='Regiones de Ubicaci??n de la Sede')    
     regiones_codigo    = fields.Char(string='Codigo de la Regi??n',size=3,required=True, help='Registra el Codigo de la Regi??n')
     sedes_id              = fields.Many2one('sedes',string='Sedes' , required=True, domain="[('regiones_id','=',regiones_id)]")
     sedes_codigo       = fields.Char(string='C??digo de la Sede',size=7,required=True, help='Registra el C??digo de la Sede')

     resp_uso_uni_id       = fields.Many2one('personas',string= 'Responsable del Bien por la Unidad', domain="[('personas_oficinas_id','=',id)]",size=3,help='Responsable de los  Bienes por la Unidad')    
     
     orden = fields.Integer(string='Orden de Jerarquias de las Oficinas')
   

     _sql_constraints = [('oficinas_codigo', 'unique(oficinas_codigo)', 'El C??digo debe se ??nico!')] 
     _sql_constraints = [('oficinas_nombre', 'unique(oficinas_nombre)', 'El Nombre debe se ??nico!')] 

     @api.onchange('regiones_id')
     def onchange_region(self):
        codigo= ''
        codigo = self.regiones_id.regiones_codigo
        self.regiones_codigo =  codigo

     @api.onchange('sedes_id')
     def onchange_sedes(self):
        codigo= ''
        codigo = self.sedes_id.sedes_codigo
        self.sedes_codigo =  codigo


"""Finde Registro Oficinas"""





class personas(models.Model):
     """Registra las Personas que trabajan en el Ente"""
     _name = 'personas'
     #_rec_name = 'personas_cedula'
     _rec_name = 'combination'

     #_rec_name = 'personas_snombre'
     #_rec_name = 'personas_papellido'    
     #     #_rec_name = 'personas_sapellido'

     personas_cedula      = fields.Integer(string='Cedula',size=10,required=True, help='Registra la Cedula de la persona')
     personas_pnombre     = fields.Char(string='Primer Nombre',size=40,required=True, help='Registra el Primer Nombre de la Persona')
     personas_snombre     = fields.Char(string='Segundo Nombre',size=40, help='Registra el Segundo Nombre de la Persona')
     personas_papellido   = fields.Char(string='Primer Apellido',size=40,required=True, help='Registra el Primer Apellido de la Persona')
     personas_sapellido   = fields.Char(string='Segundo Apellido',size=40, help='Registra el Segundo Apellido de la Persona')
     personas_cargo       = fields.Char(string='Cargo',size=100, required=True,help='Registra el Cargo de la Persona')
     personas_regiones_id = fields.Many2one('regiones',string= 'Regiones de Ubicaci??n de la Sede',size=3, required=True,help='Regiones de Ubicaci??n de la Sede')    
     personas_regiones_codigo    = fields.Char(string='Codigo de la Regi??n',size=3,required=True, help='Registra el Codigo de la Regi??n')
     personas_sedes_id    = fields.Many2one('sedes',string='Sedes del Ministerio', required=True, domain="[('regiones_id','=',personas_regiones_id)]",help='Registra el Codigo de Vinculacion con las Sedes del Ministerio')
     personas_sedes_codigo       = fields.Char(string='C??digo de la Sede',size=7,required=True, help='Registra el C??digo de la Sede')
     personas_oficinas_id          = fields.Many2one('oficinas', 'Oficina', size=3, required=True, domain="[('sedes_id','=',personas_sedes_id)]",help='Registra el Codigo de Vinculacion con las Oficinas del Ministerio')
     personas_oficinas_codigo       = fields.Char(string='Nomenclatura de la Oficina',size=20,required=True, help='Registra la Nomenclatura de la Oficina')

     tipo_resp            = fields.Selection([('D','Administrativo'),('U','Uso Directo'),('C','Cuido Directo')],string='Tipo de Responsable',size=2,required=True,help='Tipo de Responsable')
     correo_e             = fields.Char(string='Correo Electronico',size=200, required=True, help='Registra el Correo Electr??nico de la Persona')
     #status             = fields.Selection([('A','Activo'),('I','Inactivo')],string='Estatus del Personal',size=2,required=True,help='Estatus del Personal')
     active               = fields.Boolean('Estatus del Personal (Activo s/n)', default = True, size=2, help='Indica sei el personal esta activo en la instituci??n ')
        


     combination = fields.Char(string='Combination', compute='_compute_fields_combination')

     @api.depends('personas_pnombre', 'personas_papellido')
     def _compute_fields_combination(self):
        for test in self:
            test.combination = test.personas_pnombre + ' ' + test.personas_papellido

     @api.onchange('personas_regiones_id')
     def onchange_region(self):
        codigo= ''
        codigo = self.personas_regiones_id.regiones_codigo
        self.personas_regiones_codigo =  codigo
     
     @api.onchange('personas_sedes_id')
     def onchange_sedes(self):
        codigo= ''
        codigo = self.personas_sedes_id.sedes_codigo
        self.personas_sedes_codigo =  codigo
    
     @api.onchange('personas_oficinas_id')
     def onchange_oficinas(self):
        codigo= ''
        codigo = self.personas_oficinas_id.oficinas_codigo
        self.personas_oficinas_codigo =  codigo
    

    
     _sql_constraints = [('personas_cedula', 'unique(personas_cedula)', 'La Cedula debe se ??nica!')]  
    
  



class bienes_ministerio(models.Model):
     """datos ministero"""
     _name = 'bienes_ministerio'
     #_rec_name = 'rif'
     _rec_name = 'nsudebip'
     #_rec_name = 'fecha_remision'
    
     rif              = fields.Char(string='Rif del Ministerio',size=10,required=True, help='Registra el Rif del Ministerio')
     nsudebip         = fields.Char(string='Numero del Ministerio en la Sudebip',size=18,required=True, help='Registra el Numero Asignado al Ministerio por la Sudebip')
     bienes_ministerio_codigo       = fields.Char(string='C??digo de la Informacion del Ministerio en la Sudebip',size=18,
                        required=True, default='New',
                         help='Registra el codigo de la informaci??n del  Ministerio por la Sudebip')

     resp_patrimonial = fields.Many2one('personas','Responsable Patrimonial del Ministerio')
    # fecha_remision   = fields.Date(string='Fecha de Remision del Inventario', help='Registra la Fecha de Remision del Inventario a la Sudebip')
     telefono         = fields.Char(string='Numero Telefonico de la Unidad de Bienes',size=18,required=True, help='Registra el Numero telefono de la Unidad de Bienes')
     seleinv          = fields.Boolean (string='Vigencia', help='Registra si la informacion es la vigente para remitir el inventario')
    

     @api.model  
     def create(self,vals):
       if vals.get('bienes_ministerio_codigo',  'New') == 'New' or '':
          vals['bienes_ministerio_codigo'] = self.env['ir.sequence'].next_by_code(
           'self.bienes_ministerio_codigo')  or 'New'
          
       result = super(bienes_ministerio, self).create(vals)
       return result 

    
