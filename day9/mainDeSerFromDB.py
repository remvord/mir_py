import cx_Oracle
# from myclasses import Person
import pickle

if __name__ == '__main__':
    with cx_Oracle.Connection(
            'u0', 'u0', '172.30.2.133:1521/test.home.ru') as conn:
        with conn.cursor() as cursor:
            cursor.execute('''select data 
                            from persons_obj where id=1
                            ''')
            r = cursor.fetchone()
            # print(r[0].read())
            persons = pickle.loads(r[0].read())
            print(persons)
            for r in persons:
                print(r.info())
