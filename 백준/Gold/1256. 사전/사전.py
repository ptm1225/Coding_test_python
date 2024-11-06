from math import comb
N, M, K = map(int, input().split())

def find_kth_string(N, M, K):
    if K > comb(N + M, N):
        return -1
    
    result = ""
    while N > 0 and M > 0:
        count_a_first = comb(N + M - 1, N - 1)
        
        if K <= count_a_first:
            result += 'a'
            N -= 1
        else:
            result += 'z'
            M -= 1
            K -= count_a_first
    
    result += 'a' * N
    result += 'z' * M
    
    return result

print(find_kth_string(N, M, K))