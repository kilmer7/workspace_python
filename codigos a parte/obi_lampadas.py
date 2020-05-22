n = int(input())

lampA = False
lampB = False

for m in range(n):
    l = int(input())
    if l == 1:
        lampA = True
        lampB = False
    else:
        lampA = True
        lampB = True
        
    lampA = lampA
    lampB = lampB

if lampA == True and lampB == True:
    print('1')
    print('1')
elif lampA == False and lampB == True:
    print('0')
    print('1')
elif lampA == True and lampB == False:
    print('1')
    print('0')
else:
    print('0')
    print('0')
