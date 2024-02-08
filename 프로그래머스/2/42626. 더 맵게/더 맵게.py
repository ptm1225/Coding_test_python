import heapq

def solution(scoville, K):
    count = 0
    scoville.sort()
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            break
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        
        count += 1
    
    if scoville[-1] < K:
        count = -1
    
    return count