cartas = input().split(" ")

cartas[0] = int(cartas[0])
cartas[1] = int(cartas[1])
cartas[2] = int(cartas[2])
cartas[3] = int(cartas[3])
cartas[4] = int(cartas[4])

if min(cartas) >= 1 and max(cartas) <= 13:
  if cartas[0] < cartas[1] < cartas[2] < cartas[3] < cartas[4]:
     print('C')
  elif cartas[0] > cartas[1] > cartas[2] > cartas[3] > cartas[4]:
     print('D')
  else:
     print('N')