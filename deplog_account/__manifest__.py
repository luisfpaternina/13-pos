{
    'name': 'deplog account',

    'version': '13.0.0.0',

    'author': "Deplog",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.deplog.com/es/",

    'category': 'Accounting',

    'depends': [

        'account_accountant',
        'account',
        'base',

    ],

    'data': [
       
        'views/account_move.xml',
                   
    ],
    'installable': True
}
