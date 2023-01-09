from os import getenv
from sys import argv
from datetime import date, timedelta, datetime

def get_week_number():
    week_number = date.today().isocalendar()[1]

    print(week_number)

def get_week():
    tody = date.today()
    start = tody - timedelta(days=tody.weekday())
    end = start + timedelta(days=6)

    print(f'{start} ~ {end}')

def get_work_day():
    tody = date.today()
    start = tody - timedelta(days=tody.weekday())
    end = start + timedelta(days=4)

    print(f'{start} ~ {end}')

def diff(*args):
    format = '%Y-%m-%d'

    date1 = datetime.strptime(getenv('ESPANSO_DATE1'), format)
    date2 = datetime.strptime(getenv('ESPANSO_DATE2'), format)

    delta = date1 - date2 if date1.timestamp() > date2.timestamp() else date2 - date1

    print(delta.days)


if __name__ == '__main__':
    globals()[argv[1]]()