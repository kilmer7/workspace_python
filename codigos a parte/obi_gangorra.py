p1,c1,p2,c2 = input()

p1 = int(p1)
c1 = int(c1)
p2 = int(p2)
c2 = int(c2)

right = p1*c1
left = p2*c2

if (right == left):
    print(0)
elif (right < left):
    print(-1)
else:
    print(1)
