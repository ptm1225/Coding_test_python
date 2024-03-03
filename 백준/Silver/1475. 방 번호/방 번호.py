from math import ceil
d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in input():
    d[i] += 1
a = ceil((d['6'] + d['9']) / 2)
d['6'], d['9'] = a, a
print(max(d.values()))