import sys
life = 0
while(life < 100):
    life = int(input())
    sys.stdout.flush()
    print(life)
    if life == 42:
        break