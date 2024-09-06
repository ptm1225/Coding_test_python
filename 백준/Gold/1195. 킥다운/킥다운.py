def can_fit(A, B, shift):
    for i in range(len(B)):
        if 0 <= i + shift < len(A):
            if A[i + shift] == '2' and B[i] == '2':
                return False
    return True

def min_width(A, B):
    min_len = len(A) + len(B)  # 초기값은 두 문자열의 길이 합
    
    # A를 B의 왼쪽으로부터 이동시키면서 검사
    for shift in range(-len(B) + 1, len(A)):
        if can_fit(A, B, shift):
            min_len = min(min_len, max(len(A), shift + len(B)) - min(0, shift))
    
    return min_len

# 입력 받기
A = input().strip()
B = input().strip()

# 최소 가로 너비 계산 및 출력
result = min_width(A, B)
print(result)
