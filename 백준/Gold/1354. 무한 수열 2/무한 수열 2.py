def calculate_A(N, P, Q, X, Y, memo):
    # 이미 계산된 값이 있으면 바로 반환
    if N in memo:
        return memo[N]
    
    # N이 0 이하이면 1을 반환
    if N <= 0:
        return 1

    # A_n을 재귀적으로 계산
    A_n = calculate_A(N // P - X, P, Q, X, Y, memo) + calculate_A(N // Q - Y, P, Q, X, Y, memo)
    # 계산 결과를 메모리에 저장
    memo[N] = A_n
    return A_n

def main():
    # 입력 받기
    N, P, Q, X, Y = map(int, input().split())

    # 메모이제이션을 위한 딕셔너리
    memo = {}

    # A_N 계산
    result = calculate_A(N, P, Q, X, Y, memo)

    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()
