n,p = int(input());

m = 0;
for rep in range(n):
    x,y = int(input());
    z = x + y;
    if z >= p:
        m += 1;
print(m);
