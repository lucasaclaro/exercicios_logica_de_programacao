#Faça um algoritmo que leia 3 notas e calcule a média. A média é poderada e o peso das notas é 2, 3, 5.
#n1 * 2 + n2 * 3 + n3 * 5 / 10

name = input('Digite o nome do aluno: ')
note1 = float(input('Nota 1: '))
note2 = float(input('Nota 2: '))
note3 = float(input('Nota 3: '))
media = ((note1 * 2) + (note2 * 3) + (note3 * 5)) / 10
print(f'A nota final do(a) aluno(a) {name}, que tirou as notas {note1:.1f}, {note2:.1f} e {note3:.1f} é de {media:.1f}.')