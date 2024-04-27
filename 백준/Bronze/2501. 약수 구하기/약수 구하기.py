n, k = map(int, input().split())
s = [i for i in range(1, n+1) if n % i == 0]
print(0 if len(s) < k else s[k-1])