# cook your dish here
def solve():
    l, k = map(int, input().split())
    s = input()
    new = []
    ones = s.count("1")
    if k >= ones:
        k-= ones
        new = "0"*(l-ones)
        if len(new) == 0: return "0"
        return new[k:]
        
    for i in range(l):
        if s[i] == '1' and k > 0:
            s = s[:i] + '0' + s[i+1:]
            k -= 1
    return s
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
        
