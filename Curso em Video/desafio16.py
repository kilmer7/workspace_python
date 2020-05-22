import math
num = float(input('Digite um número real: '))

num = math.trunc(num)

print('O número inteiro do algarismo que você escreveu é {}'.format(num))

'''
Outra forma de resolver sem adicionar bibliotecas.

num = float(input('Digite um valor'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

'''