n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
result = [i*j for i, j in zip(a, b)]
print(sum(result))