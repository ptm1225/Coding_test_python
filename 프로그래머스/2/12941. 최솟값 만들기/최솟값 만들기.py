def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for a, b in zip(A, reversed(B)):
        answer += a * b
    return answer