curr = 10
ans = 0
while True:
    if curr == sum([int(x)**5 for x in str(curr)]):
        print(f"Found {curr}")
        ans += curr
    
    print(f"{ans=}")
    curr += 1

