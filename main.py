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


def take_wage(wage=31482):  # изменить оклад при необходимости

    wage_one_day = wage / take_busy_days()
    wage_one_hour = round(wage_one_day / 8)
    wage_evening = wage_one_hour * 5
    wage_holiday = wage_one_hour * 16
    print(f'Плата за вечеровку равна: {wage_evening}руб.')
    print(f'Плата за выходной равна: {wage_holiday}руб.')


take_wage()
