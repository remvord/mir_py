import cx_Oracle

conn = None
# получаем доступ к базе данных
try:
    conn = cx_Oracle.Connection('u0', 'u0', '172.30.2.133:1521/test.home.ru')

    try:
        cursor = conn.cursor()

    except Exception e:
        raise e
    finally:
        cursor.close()

except Exception as e:
    print(e)
finally:
    if conn is not None:
        
        conn.close()
