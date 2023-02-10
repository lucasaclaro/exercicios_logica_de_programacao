#Escreva um algoritmo para ler o salário mensal atual de um funcionário e
#o percentual de reajuste. Calcular e escrever o valor do novo salário.

wage = float(input('Digite o salário atual: R$ '))
readjustment = int(input('Digite o percentual de reajuste do salário (em %): '))
new_wage = wage + (wage * readjustment / 100)

print(f'Com o reajuste de {readjustment}%, o salário passará de R$ {wage} para R$ {new_wage:.2f}.')
