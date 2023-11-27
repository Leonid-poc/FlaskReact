import psycopg2 as psg

try:
    psg.connect(database="delivery_base", user='postgres', password='1234')
    print('Connected!')
except Exception as e:
    print(e)