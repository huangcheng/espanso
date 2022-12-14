from sys import argv
from datetime import date, timedelta

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

if __name__ == '__main__':
    globals()[argv[1]]()