from odoo import models, fields, api


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

    tests_expected = fields.Integer('Tests Expected Within 30 days',
                                    readonly=True,
                                    store=False,
                                    compute='_compute_tests_expected')

    @api.one
    def _compute_is_tester(self):
        self.is_tester = bool(self.env['test.test'].
                              search_count([('tester', '=', self.id)]))

    @api.one
    def _compute_tests_expected(self):
        query = '''
                  SELECT count(tts.id)
                  FROM test_test_session as tts
                    INNER JOIN test_test as tt
                      on tts.test = tt.id
                    INNER JOIN res_partner as rp
                      on tt.tester = rp.id
                  WHERE tt.tester = %s
                    AND tts.start_date < NOW() + INTERVAL %s
                    AND tts.end_date > NOW()
               '''
        self.env.cr.execute(query, [self.id, '1 month'])
        self.tests_expected = self.env.cr.fetchone()[0]
