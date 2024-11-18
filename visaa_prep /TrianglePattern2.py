def print_triangle(N):
    for i in range(1, N + 1):
        print(" ".join([str(i)] * i))
        
if __name__ == '__main__':
    N = int(input())
    print_triangle(N)
