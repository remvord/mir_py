import cx_Oracle
from day9.myclasses import Person
import pickle

if __name__ == '__main__':
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        with conn.cursor() as cursor:
            cursor.execute('''select ename, job, sal, hiredate from emp''')
            curPersons = cursor.fetchall()
            persons = []
            for r in curPersons:
                persons.append(Person(ename=r[0], job=r[1], sal=r[2], bd=r[3]))
                print(persons)
                with open(r'/home/remvord/person', 'wb') as f:
                    pickle.dump(persons, f)

                del persons
                with open(r'/home/remvord/person', 'rb') as f:
                    pass
                print(persons)
