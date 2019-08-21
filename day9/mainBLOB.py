import cx_Oracle

with cx_Oracle.Connection(
        'u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
    with conn.cursor() as cursor:
        try:
            n = cursor.var(cx_Oracle.NUMBER)
            with open(r'/home/remvord/1.png', 'rb') as f:
                cursor.execute('''
                insert into pic (data)
                values
                (:data) return id into :n
                ''', data=f.read(), n=n)
                conn.commit()
                cursor.execute('select data from pic where id=:id',
                               id=n.getvalue()[0])
                r = cursor.fetchone()
                with open(r'/home/remvord/11.png', 'wb') as f:
                    f.write(r[0].read())

        except Exception as e:
            print(f'Ошибка ----{e}')