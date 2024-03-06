arr = input().split()
if arr == [str(i) for i in range(1,9)]:
    print("ascending")
elif arr == [str(i) for i in range(8,0,-1)]:
    print("descending")
else:
    print("mixed")