P,R = input()

P=int(P)
R=int(R)

if P == 0 and R == 0:
    print ("C")
elif P == 0 and R == 1:
    print ("C")
elif P == 1 and R == 0:
    print ("B")
else:
    print ("A")
