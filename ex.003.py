#Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias.
#e escreva a idade dessa pessoa expressa em dias (considerar o mês com 30 dias).

from datetime import datetime

date = datetime.now()
current_year = date.year
current_month = date.month
current_day = date.day



date_of_birth = input('Digite a sua de nascimento (utilize o formato xx/xx/xxxx): ')
print(date_of_birth)
days = int(date_of_birth[0:2])
months = int(date_of_birth[3:5])
years = int(date_of_birth[6:])

years_lived = current_year - years
month_lived = current_month - months
days_lived = current_day - days

if current_month < months:
    years_lived = years_lived - 1
elif current_month == months:
    if current_day < days:
        days_lived = current_day - days

print(years_lived)
print(month_lived)
print(days_lived)



days_of_live = (years * 360) + (months * 30) + days
print(f'Você viveu até o momento {days_of_live} dias.')