s = input()
zero = s.replace('1', ' ').strip().split()
one = s.replace('0', ' ').strip().split()
print(len(zero) if len(zero) <= len(one) else len(one))