import psycopg2
from config import parameters

config = psycopg2.connect(**parameters)
current = config.cursor()

create_table = '''
    CREATE TABLE PhoneNumbers(
        name VARCHAR(255) ,
        number VARCHAR(255) UNIQUE
    );
'''

current.execute(create_table)
delete_row = '''
    DELETE FROM PhoneNumbers WHERE name = %s;
'''
current.execute(delete_row,('row',))
current.close()
config.commit()
config.close()