import sys
input = sys.stdin.readline

N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
for i in range(N):
    for i_2 in range(i, N):
        for j in range(N):
            for j_2 in range(j, N):
                minx=min(min(tree[i][0], tree[i_2][0]), min(tree[j][0], tree[j_2][0]))
                maxx=max(max(tree[i][0], tree[i_2][0]), max(tree[j][0], tree[j_2][0]))
                miny=min(min(tree[i][1], tree[i_2][1]), min(tree[j][1], tree[j_2][1]))
                maxy=max(max(tree[i][1], tree[i_2][1]), max(tree[j][1], tree[j_2][1]))
                
                d = 2*(maxx - minx + maxy - miny)
                cnt = 0
                
                ins = []
                out = 0
                for t in tree:
                    if minx <= t[0] <= maxx and miny <= t[1] <= maxy:
                        ins.append(t[2])
                    else:
                        out += t[2]
                        cnt += 1
                ins.sort()

                while ins and out < d:
                    out += ins.pop()
                    cnt += 1
                result = min(result, cnt)
print(result)