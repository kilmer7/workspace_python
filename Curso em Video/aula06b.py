cond = True;
while cond == True:
    n1 = int(input('Digite algo: '))
    if n1 < 10 and n1 > 0:
        print('Esse número é possível de acordo com o problema.')
        break;
    else:
        print('Errado, coloque uma entrada válida.')

