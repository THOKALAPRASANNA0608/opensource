X, Y, Z = map(int, input().split())
total_minutes = 2* 24 * 60
required_minutes = X *Y
if required_minutes <= total_minutes:
    print("YES")
else:
    print("NO")
