from odoo import models, fields, api
from datetime import datetime

class Tests(models.Model):
    _name = 'test.test'
    _description = 'Test'

    name = fields.Char('Test Name', index=True, required=True)
    purpose = fields.Text('Test Purpose')
    tester = fields.Many2one('res.partner', 'Test',
                             required=True, ondelete='cascade')


class TestSession(models.Model):
    _name = 'test.test_session'
    _description = 'Test Session'
    _rec_name = 'test'

    test = fields.Many2one('test.test', 'Test', requiered=True,
                           ondelete='cascade')
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    duration = fields.Integer(readonly=True, store=False,
                              compute='_compute_duration',
                              help='Duration in seconds')

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            start = fields.Datetime.from_string(r.start_date)
            end = fields.Datetime.from_string(r.end_date)
            r.duration = (end - start).days + 1


class TestResPartner(models.Model):
    _inherit = 'res.partner'

    is_tester = fields.Boolean('Is Tester', readonly=True,
                               store=False, compute='_compute_is_tester',)
    tests_expected = fields.One2many('test.test_session', 'test')

    @api.one
    def _compute_is_tester(self):
        self.is_tester = bool(self.env['test.test'].
                              search_count([('tester', '=', self.id)]))
