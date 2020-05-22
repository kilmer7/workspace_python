import random

al1 = input('Escreva o nome do primeiro aluno: ')
al2 = input('Escreva o nome do segundo aluno: ')
al3 = input('Escreva o nome do terceiro aluno: ')
al4 = input('Escreva o nome do quarto aluno: ')

rand = random.choice([al1, al2, al3, al4])

print('O aluno escolhido foi o {}'.format(rand))
