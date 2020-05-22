import math

num = float(input('Qual o valor do cateto oposto: '))
num2 = float(input('Qual o valor do cateto Adjacente: '))

hipo = math.hypot(num, num2)

print('O comprimento da Hipotenusa é de {:2.f}'.format(hipo))

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))

'''