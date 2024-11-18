N = int(input())
s = input()
t = input()

def is_isomorphic(s, t):
    map_s_to_t = {}
    map_t_to_s = {}
    
    for c1, c2 in zip(s, t):
        if c1 in map_s_to_t:
            if map_s_to_t[c1] != c2:
                return "false"
        else:
            map_s_to_t[c1] = c2
            
        if c2 in map_t_to_s:
            if map_t_to_s[c2] != c1:
                return "false"
            
        else:
            map_t_to_s[c2] = c1
    return "true"

print(is_isomorphic(s, t))
