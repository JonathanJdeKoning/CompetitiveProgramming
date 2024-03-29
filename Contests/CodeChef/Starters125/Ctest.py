# cook your dish here
def solve():
    l, k = map(int, input().split())
    s = input()
    new = []
    ones = s.count("1")
    if k >= ones:
        return "0"*(l-k)
        
    for c in s:
        if c == "1" and k > 0:
            new.append("0")
            k-=1
        else:
            new.append(c)

    return "".join(new)
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
        
