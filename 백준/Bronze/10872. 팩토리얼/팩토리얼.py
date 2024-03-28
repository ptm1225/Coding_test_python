n=int(input())
if n==0:
    print(1)
else:
    print(eval('*'.join([str(i) for i in range(1, n+1)])))