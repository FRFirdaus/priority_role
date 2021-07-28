from odoo import api, fields, models

class Karyawan(models.Model):
    _name = 'karyawan.pns'
    _inherit = ['mail.thread']
    # _order = 'pendidikan, join_date ASC'

    image = fields.Binary()
    name = fields.Char(required=True, track_visibility='onchange')
    nik = fields.Char(required=True, track_visibility='onchange')
    active = fields.Boolean(default=True)
    
    pendidikan = fields.Selection(
        [('S3', 'S3'),
        ('S2', 'S2'),
        ('S1', 'S1'),
        ('D4', 'D4'),
        ('D3', 'D3'),
        ('D2', 'D2'),
        ('D1', 'D1'),
        ('SMA', 'SMA'),
        ('SMK', 'SMK'),
        ('SMp', 'SMP'),
        ('SD', 'SD')], 
        required=True,
        track_visibility='onchange'
    )

    join_date = fields.Date(track_visibility='onchange')
    is_hakim = fields.Boolean(track_visibility='onchange')

    role_id = fields.Many2one('karyawan.role')

    @api.constrains('nik')
    def get_join_date_from_nik(self):
        for rec in self:
            nik = rec.nik
            clean_nik = nik.replace(" ", "")
            if len(clean_nik) < 18:
                raise ValidationError(_("Jumlah karakter pada NIK tidak boleh kurang dari 18 karakter, jumlah karakter pada NIK: %s" % (len(clean_nik))))
            
            date = "%s-%s-01" % (clean_nik[8:12], clean_nik[12:14])
            rec.join_date = date

class KaryawanRole(models.Model):
    _name = 'karyawan.role'

    name = fields.Char()
    description = fields.Text()