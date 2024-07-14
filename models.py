# -*- coding: utf-8 -*-
import base64

from odoo import models, fields, api, tools


@api.model
def _lang_get(self):
    return self.env['res.lang'].get_installed()


class ResWriter(models.Model):

    _name = 'res.writer'
    _inherit = ['format.address.mixin', 'avatar.mixin']
    _description = 'Writer Management'

    name = fields.Char(index=True, default_export_compatible=True)
    lastname = fields.Char(index=True, default_export_compatible=True)
    phone = fields.Char(unaccent=False)
    mobile = fields.Char(unaccent=False)
    institution = fields.Many2one("institution.w",string="Institution")
    speciality = fields.Many2many("speciality.w",string="Speciality")
    copyright_ = fields.Text(string="Copyright")
    is_writer = fields.Boolean(string="Is Writer", default=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code = fields.Char(related='country_id.code', string="Country Code")
    email = fields.Char()
    email_formatted = fields.Char(
            'Formatted Email', compute='_compute_email_formatted',
            help='Format email address "Name <email@domain>"')
    bank_account = fields.Char('Bank Account')

    title = fields.Many2one('res.partner.title')
    lang = fields.Selection(_lang_get, string='Language',
                            help="All the emails and documents sent to this contact will be translated in this language.")
    active_lang_count = fields.Integer(compute='_compute_active_lang_count')
    books = fields.Many2many('product.template', string="Books Written")



    company_id = fields.Many2one('res.company', 'Company', index=True)

    @api.depends('lang')
    def _compute_active_lang_count(self):
        lang_count = len(self.env['res.lang'].get_installed())
        for partner in self:
            partner.active_lang_count = lang_count

    def _default_category(self):
        return self.env['res.partner.category'].browse(self._context.get('category_id'))

    category_id = fields.Many2many('res.partner.category', column1='writer_id',
                                    column2='category_id', string='Tags', default=_default_category)


    @api.depends('name', 'image_1920')
    def _compute_avatar_1920(self):
        super()._compute_avatar_1920()

    @api.depends('name', 'image_1024')
    def _compute_avatar_1024(self):
        super()._compute_avatar_1024()

    @api.depends('name', 'image_512')
    def _compute_avatar_512(self):
        super()._compute_avatar_512()

    @api.depends('name','image_256')
    def _compute_avatar_256(self):
        super()._compute_avatar_256()

    @api.depends('name', 'image_128')
    def _compute_avatar_128(self):
        super()._compute_avatar_128()



    def _avatar_get_placeholder_path(self):

        return super()._avatar_get_placeholder_path()

    def _get_report_base_filename(self):
        self.ensure_one()
        return "The Writer - %s" % self.name

    def _get_list_base_filename(self):
        self.ensure_one()
        return "Writers - %s" % self.name

    @api.onchange('books')
    def _onchange_books(self):
        for book in self.books:
            if (self not in book.writer_name) and book.is_book:
                book.writer_name |= self

    def action_books_written(self):
        return {
            "type" : "ir.actions.act_window",
            "name" : f"{self.name} - Books",
            "domain" : [("writer_name", "=", self.id)],
            "view_mode" : "tree",
            "res_model" : "product.template",
        }





class Institution(models.Model):
    _name = "institution.w"
    _description = "Institution"

    ref = fields.Char(string="Reference")
    name = fields.Char(string="Name", required=True )


class Speciality(models.Model):
    _name = "speciality.w"
    _description = "Speciality"

    ref = fields.Char(string="Reference")
    name = fields.Char(string="Name", required=True )



