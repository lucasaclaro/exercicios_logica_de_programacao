#Escreva um algoritmo para ler o salário mensal atual de um funcionário e
#o percentual de reajuste. Calcular e escrever o valor do novo salário.

wage = float(input('Digite o salário atual: R$ '))
readjustment = int(input('Digite o percentual de reajuste do salário (em %): '))
new_wage = wage + (wage * readjustment / 100)

print(f'Com o reajuste de {readjustment}%, o salário passará de R$ {wage} para R$ {new_wage:.2f}.')


#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês mais uma comissão fixa por carro vendido de
#5% sobre o total de vendas efetuadas. Escreva um algoritmo que leia o número de carros vendidos, o valor total das vendas, o valor que ele recebe
#por cada carro e o salário fixo  e calcule o salário dele.


name = input('Nome do funcionário: ')
wage = float(input(f'Digite o salário do/da {name}: R$ '))
cars_sold = int(input(f'Quantidade de veículos vendida por {name}: '))
cars_value = float(input(f'Valor total dos carros vendidos por {name}: '))
commission = (cars_value * 5 / 100) 
wage_commission = wage + (commission * cars_sold)

print(f'Neste mês, {name} vendeu {cars_sold} veículos, totalizando um valor de R$ {cars_value:.2f}. Ele(a) recebeu R$ {commission:.2f} por veículo vendido.\n'
      f'Seu salário final, contando com as comissões foi de R$ {wage_commission:.2f}.')


