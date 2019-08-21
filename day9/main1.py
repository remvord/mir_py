import cx_Oracle
import xmlformatter

sql = '''
select xmlelement("enterprise",
 (select xmlagg(
     xmlelement("departments",
     xmlattributes(deptno as "id"),
    xmlelement("dname",dname),
    xmlelement("emps",(select xmlagg(xmlelement("person",
                            xmlattributes(empno as "id"),
                            xmlforest(ename as "ename"),
                            xmlforest(job as "job"),
                            xmlforest(sal as "sal"))) from emp 
                          where emp.deptno=dept.deptno)
    ))) from dept)) as x from dual'''

if __name__ == '__main__':
    with cx_Oracle.Connection('u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        try:
            conn.execute('alter session set NLS_LANGUAGE=english')
            conn.execute('alter session set NLS_TERRITORY=AMERICA')
            with open(r'/home/remvord/king_corp.xml', 'r') as f:
                cdata = f.read()
                # print(cdata)
            with conn.cursor() as cursor:
                cursor.execute("""insert into x (data)values(:xdata)""",
                               xdata=cdata)
            conn.commit()
        except Exception as e:
            print(e)
