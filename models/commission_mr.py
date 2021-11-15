# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MedicalRepresentiveExtension(models.Model):
    _inherit = 'medical.representative'
    _description = 'acs_hms_mr_commission_extension'


    commission_role_id = fields.Many2one('acs_hms.commission.role', string='Role')
    # commission_ids = fields.One2many('acs.hms.commission', 'partner_id', 'Business Commission')
    provide_commission = fields.Boolean('Give Commission')
    commission_percentage = fields.Float('Commission Percentage')
    # commission_rule_ids = fields.One2many("acs.commission.rule", "partner_id", string="Commission Rules")



# class AcsCommissionRole(models.Model):
#     _name = 'acs_hms.commission.role'
#     _description = 'Commission Role'
#
#     name = fields.Char(string='Name', required=True)
#     description = fields.Text("Description")
    # commission_rule_ids = fields.One2many("acs.commission.rule", "role_id", string="Commission Rules")
