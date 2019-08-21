import cx_Oracle

if __name__ == '__main__':
    with cx_Oracle.Connection('u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        with conn.cursor() as cursor:
            ctable = 'dept'

            try:
                n = cursor.var(cx_Oracle.NUMBER)
                cdata = cursor.var(cx_Oracle.CURSOR)
                cursor.callfunc("pack1.info", n,
                                (ctable, cdata))
                # cursor.execute(
                #     'alter session set NLS_LANGUAGE=english')
                # cursor.execute(
                #     'alter session set NLS_TERRITORY=AMERICA')

                print(n.getvalue())
                print(cdata.getvalue())

            except Exception as e:
                print(f'Error --{e}')
