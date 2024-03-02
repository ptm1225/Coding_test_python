n = int(input())

a = '1'

for i in range(2, n+1):
    a = str(int(a)*i).rstrip('0')[-15:]

print(a[-5:])