from datetime import date

print('---------------------')
print('     BIRTHDAY APP    ')
print('---------------------')

birthday_date_input = input('When you were born? [YYYY.MM.DD]: ')
[year, month, day] = birthday_date_input.split('.')
today_date = date.today()
birthday_date = date.fromisoformat(
    str(today_date.year) + '-' + month + '-' + day
)
birthday_in = abs(birthday_date - today_date).days

print('It looks like you were born on ' + day + '.' + month + '.' + year)
print('Your birthday is in ' + str(birthday_in) + ' days.')
