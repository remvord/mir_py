import cx_Oracle

try:
    # Соединились с базой данных
    with cx_Oracle.Connection('u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        # print(conn)
        # Открываем курсор и подготавливаем для него работу - 1.2.3. фазы выполения
        # этот курсор соержит отделы как только он закроется все ленивые курсоры тоже будут закрыты
        with conn.cursor() as cursor:
            # print(cursor)
            cursor.execute("alter session set NLS_LANGUAGE=russian")
            a = cursor.execute("""select 
                                d.dname, 
                                 CURSOR(
                                 select ename, job, sal 
                                 from emp
                                 where emp.deptno=d.deptno
                                 ) as emps
                                 from 
                                dept d order by d.dname""")
            # из курсора а фетчим все данные
            # это ленивый курсор - после выполнения закроется
            depts = a.fetchall()
            for r in depts:
                print(r[0])
                aemps = r[1]
                emps = aemps.fetchall()
                # print(emps)
                for r in emps:
                    print(f'   {r[0]}', r[1], r[2])

except Exception as e:
    print(e)
