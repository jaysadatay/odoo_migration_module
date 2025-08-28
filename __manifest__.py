# -*- coding: utf-8 -*-
#################################################################################

#################################################################################
{
    'name': 'Migration from other odoo',
    "version": "14.0.0.0",
    "author": "MeLikeyMedia",
    "maintainer": "MeLikeyMedia",
    'depends': ['queue_job'],
    'external_dependencies': {'python': ['odoorpc']},
    'data': [
        #'data/migration.credentials.csv',
        #'data/migration.model.csv',
        #'data/migration.record.csv',
        'security/ir.model.access.csv',
        'views/migration_views.xml',
    ],
    "license": "AGPL-3",
}