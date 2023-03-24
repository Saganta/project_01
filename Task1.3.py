
month_number = 104

months = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}
mess = 'Такого месяца нет!'
if(not(month_number > 12 or month_number < 1)):
    mess = months[str(month_number)]
    
print(mess)