import math

ang = float(input('Informe o angulo: '))

ang2 = math.radians(ang)
seno = math.sin(ang2)
coseno = math.cos(ang2)
tangente = math.tan(ang2)

print('O seno é {:.2f}, o coseno é {:.2f}, e a tangente é {:.2f} do angulo {:.0f}'.format(seno,coseno,tangente,ang))
