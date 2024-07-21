import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
a = X if X > Y else Y
b = Y if X > Y else X
result = 0

if S < W:
    result = S * (b + ((a-b)//2)*2) + W * ((a-b)%2)
elif S < W*2:
    result = S * b + W * (a-b)
else:
    result = W * (a + b)

print(result)