import cx_Oracle
# from myclasses import Person
# import pickle

if __name__ == '__main__':
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        with conn.cursor() as cursor:
            cursor.execute('''select ename, job, sal, hiredate from emp''')
            curPersons = cursor.fetchall()
            persons = []
            for r in curPersons:
                persons.append(Person(ename=r[0], job=r[1], sal=r[2], bd=r[3]))
            persons.sort()
            obj = pickle.dumps(persons)

            print(obj)
            try:
                cursor.execute('''insert into persons_obj
                                (data)values(:data)
                                ''',
                               data=obj)
                conn.commit()

            except Exception as e:
                print(e)
