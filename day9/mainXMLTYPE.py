import cx_Oracle
import xmlformatter

if __name__ == '__main__':
    with cx_Oracle.Connection(
            'u0', 'u0',
            '172.30.2.133:1521/test.home.ru') as conn:
        try:

            # conn.execute('alter session set NLS_LANGUAGE=american')
            # conn.execute('alter session set NLS_TERRITORY=AMERICA')

            with open(r'/home/remvord/king_corp.xml', 'r') as f:
                cdata = f.read()
            with conn.cursor() as cursor:
                cursor.execute("""insert into x (data)values(:xdata)""",
                               xdata=cdata)
            conn.commit()
        except Exception as e:
            print(e)
