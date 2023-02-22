date_input = str(input('Введите месяц: '))
number_month = '1'
second_month_number = '2'
# Задаем текущий год
current_year1 = str(2023)
current_year2 = str(2023)


def get_month_number():
    date = date_input
    global number_month
    global second_month_number
    global  current_year2
    if date_input.lower() == 'январь':
        number_month = '01'
        second_month_number = '02'
    elif date.lower() == 'февраль':
        number_month = '02'
        second_month_number = '03'
    elif date.lower() == 'март':
        number_month = '03'
        second_month_number = '04'
    elif date.lower() == 'апрель':
        number_month = '04'
        second_month_number = '05'
    elif date.lower() == 'май':
        number_month = '05'
        second_month_number = '06'
    elif date.lower() == 'июнь':
        number_month = '06'
        second_month_number = '07'
    elif date.lower() == 'июль':
        number_month = '07'
        second_month_number = '08'
    elif date.lower() == 'август':
        number_month = '08'
        second_month_number = '09'
    elif date.lower() == 'сентябрь':
        number_month = '09'
        second_month_number = '10'
    elif date.lower() == 'октябрь':
        number_month = '10'
        second_month_number = '11'
    elif date.lower() == 'ноябрь':
        number_month = '11'
        second_month_number = '12'
    elif date.lower() == 'декабрь':
        number_month = '12'
        second_month_number = '01'
        current_year2 = int(current_year1) + 1
        current_year2 = str(current_year2)

    return number_month, second_month_number, current_year2


number_month_str, second_month_number_str, current_year2_str = get_month_number()
