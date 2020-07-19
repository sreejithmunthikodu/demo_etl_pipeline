import os

DB_DETAILS = {
    'dev': {
        'mysql': {
            'username': 'my_admin',
            'password': 'mypassword',
            'host': '3.96.15.164',
            'port': 3306,
            'database': 'covid_db_mysql'
        },
        'psql': {
            'username': 'my_admin',
            'password': 'mypassword',
            'host': '3.96.15.164',
            'port': 5432,
            'database': 'covid_db_psql'
        }
    }
}

POPULATION_TABLE = 'world_population'
COVID_TABLE = 'covid_data'