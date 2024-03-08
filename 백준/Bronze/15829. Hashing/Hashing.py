L = int(input())
arr = list(map(ord, input()))
arr = [(v-96) * (31**i) for i, v in enumerate(arr)]
print(sum(arr)%1234567891)