def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        words.insert(0, begin)
        ans = words.index(target)
        n = len(words)
        arr = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and sum([x!=y for x, y in zip(words[i], words[j])]) == 1:
                    arr[i].append(j)
        visited = [False] * n
        queue = [0]
        count = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.pop(0)
                if i == ans:
                    return count
                v = words[i]
                if not visited[i]:
                    visited[i] = True
                    for x in arr[i]:
                        if not visited[x]:
                            queue.append(x)
            count += 1