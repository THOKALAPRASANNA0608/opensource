
def will_reach_on_time(X):

    if X >= 30:

        return "YES"

    else:

        return "NO"

def main():

    T = int(input().strip())

    for _ in range(T):
        X = int(input().strip())
        print(will_reach_on_time(X))

if __name__ == "__main__":  
    main()
