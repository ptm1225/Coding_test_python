N = int(input())
arr = list(map(int, input().split()))
result = [0] * 2000001

for x in arr:
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            result[x//i] += 1
            result[i] += 1
    if x**0.5 == int(x**0.5):
        result[int(x**0.5)] -= 1
    
print(max(i*v for i, v in enumerate(result) if v > 1))