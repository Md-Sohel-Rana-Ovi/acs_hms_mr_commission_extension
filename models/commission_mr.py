# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RespartnerExtension(models.Model):
    _inherit = "res.partner"
    _description = 'acs_hms_mr_commission_extension'


    commission_role_id = fields.Many2one('commission.role', string='Role')
    commission_ids = fields.One2many('acs.commission', 'partner_id', 'Business Commission')
    provide_commission = fields.Boolean('Give Commission')
    commission_percentage = fields.Float('Commission Percentage')
    commission_rule_ids = fields.One2many("commission.rule", "partner_id", string="Commission Rules")

    def commission_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id("acs_hms_commission.acs_hms_commission_action")
        action['domain'] = [('partner_id', '=', self.id)]
        action['context'] = {'default_partner_id': self.id, 'search_default_not_invoiced': 1}
        return action

class MedicalRepresentativeExtension(models.Model):
    _inherit = "medical.representative"

    def commission_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id("acs_hms_commission.acs_hms_commission_action")
        action['domain'] = [('partner_id','=',self.partner_id.id)]
        action['context'] = {'default_partner_id': self.partner_id.id, 'search_default_not_invoiced': 1}
        return action


class AcsCommissionRole(models.Model):
    _name = 'commission.role'
    _description = 'Commission Role'
    # _order = "sequence"

    name = fields.Char(string='Name', required=True)
    description = fields.Text("Description")
    commission_rule_ids = fields.One2many("commission.rule", "role_id", string="Commission Rules")


class AcsCommissionRoleExtension(models.Model):
    _name = 'commission.rule'
    _description = 'Commission Rule'
    _order = "sequence"

    sequence = fields.Integer(string='Sequence', default=50)
    rule_type = fields.Selection([
        ('role', 'Role'),
        ('user', 'User'),
    ], string='Rule Type', copy=False, default='role', required=True)
    role_id = fields.Many2one('commission.role', string='Role')
    user_id = fields.Many2one('res.users', string='User')
    partner_id = fields.Many2one('res.partner', string='Partner')
    physician_id = fields.Many2one('res.partner', string='Physician')
    rule_on = fields.Selection([
        ('product_category', 'Product Category'),
        ('product', 'Product'),
    ], string='Rule On', copy=False, default='product_category', required=True)
    product_category_id = fields.Many2one('product.category', string='Product Category')
    product_id = fields.Many2one('product.template', string='Product')
    percentage = fields.Float('Commission Percentage')
    description = fields.Text("Description")

class HMSCommissionExtension(models.Model):
    _name = 'acs.commission'
    _description = 'HMS Commission'

    partner_id = fields.Many2one('res.partner', 'Partner', required=True, tracking=True)





