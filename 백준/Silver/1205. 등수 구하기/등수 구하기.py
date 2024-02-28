n, new_score, p = map(int, input().split())
answer = 0
if n == 0:
    answer = 1
else:
    scores = list(map(int, input().split()))
    if n == p and scores[-1] >= new_score:
        answer = -1
    else:
        answer = n+1
        for i in range(n):
            if scores[i] <= new_score:
                answer = i+1
                break

print(answer)