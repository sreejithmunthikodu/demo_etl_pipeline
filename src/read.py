import config
from sqlalchemy import create_engine
import pandas as pd
# import pymysql


# Connect MYSQL database
def connect_to_source_db(DB_DETAILS, source):
    # Get the connection details from config file
    if source == 'mysql':
        dev = DB_DETAILS['dev']['mysql']
        connection_uri = f'mysql+pymysql://{dev["username"]}:{dev["password"]}@{dev["host"]}:{dev["port"]}/{dev["database"]}'
    elif source == 'psql':
        dev = DB_DETAILS['dev']['psql']
        connection_uri = f'postgresql://{dev["username"]}:{dev["password"]}@{dev["host"]}:{dev["port"]}/{dev["database"]}'

    db_engine = create_engine(connection_uri)

    return db_engine


# Read from source databases
def extract_table_to_pandas(tablename, db_engine):
    query = f'SELECT * FROM {tablename}'
    df = pd.read_sql(query, db_engine)

    return df


if __name__ == "__main__":
    print('Reading from PSQL...')
    db_engine_psql = connect_to_source_db(config.DB_DETAILS, source='psql')
    df_pop = extract_table_to_pandas(config.POPULATION_TABLE, db_engine_psql)
    print(df_pop)

    print('\nReading from MYSQL...')
    db_engine_mysql = connect_to_source_db(config.DB_DETAILS, source='mysql')
    df_covid = extract_table_to_pandas(config.COVID_TABLE, db_engine_mysql)
    print(df_covid)
    

