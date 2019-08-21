import cx_Oracle

try:
    with cx_Oracle.Connection('u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        # print(conn)
        with conn.cursor() as cursor:
            # print(cursor)
            a = cursor.execute('select * from dept order by dname')
            c = a.description
            n = a.fetchall()
            print(n)
            for r in n:
                print(c[0][0], r[0],
                      c[1][0], r[1],
                      c[2][0], r[2])
                with conn.cursor() as cemps:
                    cemps.execute("""select * from emp 
                        where deptno = :deptno""",
                                  depnto=r[0])
                    emps = cemps.fetchall()
                    for r in emps:
                        print(r)

except Exception as e:
    print(e)
