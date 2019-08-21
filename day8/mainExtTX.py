import cx_Oracle

try:
    id = 7839
    sal = 5001
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as connUser, \
            cx_Oracle.Connection(
                'SCOTT', 'tiger', '172.30.2.133:1521/test.home.ru') as connScott:
        connUser.autocommit = 0
        connScott.autocommit = 0

        with connUser.cursor() as cursorUser, connScott.cursor() as cursorScott:
            try:
                cursorScott.execute(
                    'alter session set NLS_LANGUAGE=english')
                cursorScott.execute(
                    'alter session set NLS_TERRITORY=AMERICA')
                cursorUser.execute(
                    'update emp set sal=:sal where empno=:empno',
                    sal=sal, empno=id)
                cursorScott.execute('''insert into log_tab (text,sal)values
                                    (:text, :sal)
                                    ''',
                                    text=f'remvord Changed salary {sal} user {id}', sal=sal)
                connUser.commit()
                connScott.commit()

            except Exception as e:
                connUser.rollback()
                connScott.rollback()
                print(e)

except Exception as e:
    print(e)
