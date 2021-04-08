{
    'name': 'material',
    'summary': """""",
    'version': '1.0',
    'description': """register the materials to be sold""",
    'depends': ['base'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/material_registration.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}