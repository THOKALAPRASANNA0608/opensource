
import math

X,N=map(int,input().split())
current_capacity=X*100
if current_capacity>=N:
    print(0)

else:
    remaining_passengers=N-current_capacity
    new_planes=(remaining_passengers+99)//100
    print(new_planes
