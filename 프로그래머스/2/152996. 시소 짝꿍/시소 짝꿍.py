from collections import Counter

def solution(weights):
    count = 0
    counter = Counter(weights)  # 각 무게의 개수를 세어둠
    distances = [2, 3, 4]  # 가능한 거리
    
    # 1. 같은 무게인 경우 같은 거리에 앉으면 균형
    for weight, freq in counter.items():
        if freq > 1:
            count += freq * (freq - 1) // 2  # 조합 개수 nC2
    
    # 2. 서로 다른 무게와 다른 거리에 앉아 균형을 이루는 경우
    for weight1 in counter:
        for weight2 in counter:
            if weight1 < weight2:  # 중복을 피하기 위해 weight1 < weight2로 조건 설정
                for d1 in distances:
                    for d2 in distances:
                        if weight1 * d1 == weight2 * d2:
                            count += counter[weight1] * counter[weight2]
    
    return count
