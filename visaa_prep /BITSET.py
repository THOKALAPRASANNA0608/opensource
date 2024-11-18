import sys

def check_bit_set(N, k):
    k -= 1
    mask = 1 << k

    if N & mask:
        return "true"
    else:
        return"false"
    
if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    
    if not input_data:
        print("false")
    else:
        
        N, k = map(int, input_data.split())
        print(check_bit_set(N, k))
