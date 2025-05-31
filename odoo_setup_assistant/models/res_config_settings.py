# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    setup_assist_base_git_dir = fields.Char(
        string="Base Git Cloning Directory",
        config_parameter='setup.assist.base_git_dir',
        help="Absolute path where GitHub repositories will be cloned/pulled. Used by Odoo Setup Assistant."
    ) 