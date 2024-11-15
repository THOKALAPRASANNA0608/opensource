X, Y, Z = map(int, input().split())
max_weight = Z - Y
if max_weight <= 0:
    print(0)
else:
    max_mangoes = max_weight // X
    print(max_mangoes)
