import psycopg2 as psg


try:
    # /var/lib/pgsql/data/pg_hba.conf --> (peer -> md5)
    conn = psg.connect(database="delivery_base", user='postgres', password='1234')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    print(cursor.fetchone())
except Exception as e:
    print(e)