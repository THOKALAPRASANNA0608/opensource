A, B, C, x = map(int, input().split())

if A + B >= x or A + C >= x or B + C >= x:
    print("YES")
else:
    print("NO")
