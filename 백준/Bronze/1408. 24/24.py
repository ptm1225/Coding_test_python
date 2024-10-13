def time_to_seconds(t):
    h, m, s = map(int, t.strip().split(':'))
    return h * 3600 + m * 60 + s


def seconds_to_time(s):
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return f"{h:02d}:{m:02d}:{s:02d}"


current_time = input()
start_time = input()

current_seconds = time_to_seconds(current_time)
start_seconds = time_to_seconds(start_time)

if current_seconds < start_seconds:
    remaining_seconds = start_seconds - current_seconds
else:
    remaining_seconds = 86400 - (current_seconds - start_seconds)

print(seconds_to_time(remaining_seconds))
