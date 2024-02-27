w, h, x, y, p = map(int, input().split())
r = h / 2
count = 0
for _ in range(p):
    px, py = map(int, input().split())
    if (x <= px <= x + w and y <= py <= y + h) or (
        (x - px)**2 + (y + r - py)**2 <= r**2) or ((x + w - px)**2 +
                                                   (y + r - py)**2 <= r**2):
        count += 1
print(count)