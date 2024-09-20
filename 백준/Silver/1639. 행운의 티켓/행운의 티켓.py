def find_lucky_ticket(s):
    n = len(s)
    max_length = 0

    for length in range(2, n+1, 2):
        for i in range(n - length + 1):
            mid = i + length // 2
            left_sum = sum(map(int, s[i:mid]))
            right_sum = sum(map(int, s[mid:i+length]))
            if left_sum == right_sum:
                max_length = max(max_length, length)
    
    return max_length

s = input()

print(find_lucky_ticket(s))
