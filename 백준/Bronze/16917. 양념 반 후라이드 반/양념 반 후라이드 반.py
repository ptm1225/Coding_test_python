import sys
input = sys.stdin.readline

A, B, C, X, Y = map(int, input().split())
if Y > X:
    X, Y = Y, X
    A, B = B, A

print(min(A*X + B*Y, A*(X-Y) + C*2*Y, C*2*X))