#Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias.
#e escreva a idade dessa pessoa expressa em dias (considerar o mês com 30 dias).

from datetime import datetime

date = datetime.now()
current_year = date.year
current_month = date.month
current_day = date.day



date_of_birth = input('Digite a sua de nascimento (utilize o formato xx/xx/xxxx): ')
days = int(date_of_birth[0:2])
months = int(date_of_birth[3:5])
years = int(date_of_birth[6:])

if current_month < months:
    total_years = (current_year - years - 1) * 360
    total_months = current_month * 30
    total_days = current_day
    total = total_days + total_months + total_years
elif current_month > months:
    total_years = (current_year - years) * 360
    total_months = (current_month - months) * 30
    total_days = current_day - days
    total = total_days + total_months + total_years
elif current_month == months:
    if current_day > days:
        total_years = (current_year - years - 1) * 360
        total_months = (current_month - 1) * 30
        total_days = days
        total = total_days + total_months + total_years
    elif current_day < days:
        total_years = (current_year - years) * 360
        total_months = (current_month - months) * 30
        total_days = days - current_day

        total = total_days + total_months + total_years
    elif current_day == days:
        total = (current_year - years) * 360


print(f'Você viveu até hoje {total} dias.')
