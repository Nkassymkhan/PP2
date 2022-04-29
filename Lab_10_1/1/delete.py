import psycopg2
from config import parameters
config = psycopg2.connect(**parameters)
current = config.cursor()
name = input("name")
delete_raw = '''
    DELETE FROM PhoneNumbers WHERE name = %s;
'''
current.execute(delete_raw,(name,))
current.close()
config.commit()
config.close()