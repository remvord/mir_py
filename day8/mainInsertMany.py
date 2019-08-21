import cx_Oracle

insertSQL = '''insert into USER_PROFILES
("USER_ID",
"PROFILE_NO",
"DATE_INSERT")
values(
:USER_ID,
:PROFILE_NO,
:DATE_INSERT)'''

try:
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as connUser, \
            cx_Oracle.Connection('rwc', 'rwc', 'localhost:15210/OSB') as connParus:
        # получили 2 соединения
        print(connUser)
        print(connParus)

        # создали 2-а крусора - из одного чиатем в другой пишем
        with connParus.cursor() as cursorParus, connUser.cursor() as cursorUser:
            cursorParus.execute(
                'alter session set optimizer_mode=all_rows')
            cursorUser.execute(
                'alter session set optimizer_mode=first_rows')
            cursorUser.execute(
                'alter session set NLS_LANGUAGE=english')
            cursorUser.execute(
                'alter session set NLS_TERRITORY=AMERICA')
            cursorParus.arraysize = 5
            source = cursorParus.execute("select * from USER_PROFILES")

            while (True):
                src = source.fetchmany()
                if src == []:
                    break
                print(src)
                print('-'*len(src))
                cursorUser.prepare(insertSQL)
                cursorUser.executemany(insertSQL, src)
                connUser.commit()

except Exception as e:
    print(e)
