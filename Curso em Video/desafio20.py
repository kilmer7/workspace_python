import random

al1 = str(input('Nome do primeiro aluno: '))
al2 = str(input('Nome do segundo aluno: '))
al3 = str(input('Nome do terceiro aluno: '))
al4 = str(input('Nome do quarto aluno: '))

lista = [al1, al2, al3, al4]
random.shuffle(lista)

print('A ordem de apresentação do trabalho será {}'.format(lista))
