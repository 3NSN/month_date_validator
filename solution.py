month_name = str(input('Enter month name: '))
month_date = int(input('Enter month date: '))#

months31 = ['Janury', 'March', 'May', 'Jule', 'August', 'October', 'December']
months30 = ['June', 'September', 'November', 'April']
months29 = ['February']

beginning_of_month = 1

if month_name in months31:
    end_of_month = 31
elif month_name in months30:
    end_of_month = 30
elif month_name in months29:
    end_of_month = 29

if month_date < 0 or month_date > 31 or month_name not in (months31 + months30 + months29):
    print("Таких месяцев или дат не существует")
    exit(0)

if beginning_of_month <= month_date <= end_of_month:
    print("Да, " + month_name + " содержит число " + str(month_date))
else:
    print("Нет, " + month_name + " содержит только числа с " + str(beginning_of_month) + " по " + str(end_of_month))