import cx_Oracle

try:
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        cur = conn.cursor()

        try:
            cur.execute('alter session set NLS_LANGUAGE=english')
            cur.execute('alter session set NLS_TERRITORY=AMERICA')
            cur.execute("create table b as select * from base")
            print(cur.rowcount)
            print("Table created")
        except cx_Oracle.DatabaseError as e:
            print(f'{type(e)} - {e}')
            cur.execute("truncate table b")
            print(cur.rowcount)
        cur.execute("insert into b (select * from base where nomer like '3%')")
        cur.execute("update b set famil = 'qqqq'")
        print(cur.rowcount)
        conn.commit()

except Exception as e:
    print(e)

