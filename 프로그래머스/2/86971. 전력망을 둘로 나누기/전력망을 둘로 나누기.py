def find_set(x, node):
    if x == node[x]:
        return x
    return find_set(node[x], node)

def solution(n, wires):
    answer = float('inf')
    for i in range(n-1):
        node = list(range(n+1))
        for j in range(n-1):
            if i == j:
                continue
            u, v = wires[j]
            fu, fv = find_set(u, node), find_set(v, node)
            if fu == fv:
                continue
            
            if fu > fv:
                fu, fv = fv, fu
            for idx, v in enumerate(node):
                if v == fv:
                    node[idx] = fu
        node.pop(0)
        x = node.count(node[0])
        answer = min(answer, (abs(x - abs(n-x))))
    return answer