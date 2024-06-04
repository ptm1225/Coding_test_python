def max_lit_rows(N, M, table, K):
    from collections import defaultdict

    row_count = defaultdict(int)
    for row in table:
        row_str = ''.join(map(str, row))
        row_count[row_str] += 1

    max_lit = 0

    for row_str, count in row_count.items():
        zero_count = row_str.count('0')

        if zero_count <= K and (K - zero_count) % 2 == 0:
            max_lit = max(max_lit, count)

    return max_lit

N, M = map(int, input().split())
table = [list(map(int, input().strip())) for _ in range(N)]
K = int(input().strip())

print(max_lit_rows(N, M, table, K))