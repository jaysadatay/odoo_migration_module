# -*- coding: utf-8 -*-
#################################################################################
# Author      : MeLikeyMedia
# License     : AGPL-3
#
#################################################################################
{
    'name': 'Migration from other odoo',
    "version": "17.0.0.0",
    "author": "MeLikeyMedia",
    "maintainer": "MeLikeyMedia",
    'depends': ['account'],
    'external_dependencies': {'python': ['odoorpc']},
    'data': [
        #'data/migration.credentials.csv',
        # 'data/migration.model.csv',
        # 'data/migration.record.csv',
        'security/ir.model.access.csv',
        'views/migration_views.xml',
    ],
    "license": "AGPL-3",
}