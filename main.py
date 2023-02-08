from numpy import busday_count
import month_number

month = month_number.number_month_str
second_month_number = month_number.second_month_number_str

holiday = int(input('Введите количество праздничных дней: '))

first_date = f'{month_number.current_year1}-{month}'
second_date = f'{month_number.current_year2_str}-{second_month_number}'
buday = first_date
endbuday = second_date
print(buday, endbuday)


def take_busy_days():
    busy_days = busday_count(buday, endbuday)
    busy_days_without_holiday = int(busy_days) - holiday
    print(f'Количество рабочих дней: {busy_days_without_holiday}')
    return busy_days_without_holiday


def take_wage(salary=31482):  # изменить оклад при необходимости

    salary_one_day = salary / take_busy_days()
    salary_one_hour = round(salary_one_day / 8)
    salary_evening = salary_one_hour * 5
    salary_holiday = salary_one_hour * 16
    print(f'Плата за одну смену равна: {int(salary_one_day)}руб.')
    print(f'Плата за вечеровку равна: {salary_evening}руб.')
    print(f'Плата за выходной равна: {salary_holiday}руб.')


take_wage()
