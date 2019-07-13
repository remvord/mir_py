from datetime import date, time, datetime as dt

if __name__ == '__main__':
    print(dt.today())
    d = dt.today()
    print(f'Date-{d.day} month-{d.month} year-{d.year}')
    d1 = date.today()
    d2 = d1.replace(1999, 12, 10)
    print(d2.strftime('%Y/%m/%d'))
    d4 = date(1980, 5, 10)
    print(d4.strftime('%Y/%m/%d'))
    print(d2 - d4)
    print('-' * 10)
    d1 = date.today()
    d2 = d1.replace(d1.year, d1.month, d1.day+1)
    print(d2.strftime('%Y/%m/%d'))
    d = d2-d1
    print(d)
