from odoo import models, fields, api, tools

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_book = fields.Boolean(string="Is Book", default=False)
    writer_name = fields.Many2one('res.writer', string="Writer's Name")
    writer_lastname = fields.Char( string="Writer's Lastname", related="writer_name.lastname")
    release_date = fields.Date(string="Release Date")
    copyright_ = fields.Html(string="Copyright")

    @api.onchange('writer_name')
    def _onchange_writer_name(self):
        for writer in self.writer_name:
            if self not in writer.books:
                writer.books |= self