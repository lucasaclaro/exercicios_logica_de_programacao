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


#Escreva um algorítimo para ler o número total de municípios, o número de votos branco, nulos e válidos.
#Calcule e escreva o percentual que cada representa em relação ao total de eleitores.

total = int(input('Digite o número total de eleitores do município: '))
brancos = int(input('Digite o número total de votos brancos: '))
nulos = int(input('Digite o número total de votos nulos: '))
validos = int(input('Digite o número total de votos válidos: '))

percentual_brancos = (100 * brancos) / total
percentual_nulos = (100 * nulos) / total
percentual_validos = (100 * validos) / total

print(f'''
    O percentual de votos foi de: \n 
    Brancos: {percentual_brancos:.2f}%,\n
    Nulos: {percentual_nulos:.2f}%,\n
    Válidos: {percentual_validos:.2f}%.
    ''')



#Escreva um algoritmo para ler o salário mensal atual de um funcionário e
#o percentual de reajuste. Calcular e escrever o valor do novo salário.

wage = float(input('Digite o salário atual: R$ '))
readjustment = int(input('Digite o percentual de reajuste do salário (em %): '))
new_wage = wage + (wage * readjustment / 100)

print(f'Com o reajuste de {readjustment}%, o salário passará de R$ {wage} para R$ {new_wage:.2f}.')
