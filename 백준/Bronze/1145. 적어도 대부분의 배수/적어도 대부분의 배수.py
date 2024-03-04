arr = list(map(int, input().split()))
number = min(arr)
while True:
    if sum([number%i==0 for i in arr]) >= 3:
        break
    number += 1
print(number)