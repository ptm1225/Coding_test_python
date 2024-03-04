n = int(input())
f = int(input())
a = n//100*100
for i in range(a, a+100):
    if i%f == 0:
        print(str(i)[-2:])
        break