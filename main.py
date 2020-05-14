import datetime
from application import salary as s
from application.db.people import get_employees

def main():
    print(datetime.datetime.now())
    s.calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()