
import math
2
X,N=map(int,input().split())
3
current_capacity=X*100
4
if current_capacity>=N:
5
    print(0)
6
else:
7
    remaining_passengers=N-current_capacity
8
    new_planes=(remaining_passengers+99)//100
9
    print(new_planes
