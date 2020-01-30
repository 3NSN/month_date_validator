month_name = str(input('Enter month name: '))
month_date = int(input('Enter month date: '))
months31 = ['Janury', 'March', 'May', 'Jule', 'August', 'October', 'December']
months30 = ['June', 'September', 'November', 'April']
months29 = ['February']

correction = 1

if month_date < 0 or month_date > 31:
    print ("Таких месяцев или дат не существует")
    exit(0)

if month_name in months31:
    date_range = range(1, 31 + correction)
elif month_name in months30:
    date_range = range(1, 30 + correction)
elif month_name in months29:
    date_range = range(1, 29 + correction)
else:
    print("Таких месяцев или дат не существует")
    exit(0)

if month_date in date_range:
    print("Да, " + month_name + " содержит число " + str(month_date))
else:
    print("Нет, " + month_name + " содержит только числа с " + str(date_range.start) + " по " + str(date_range.stop - correction))