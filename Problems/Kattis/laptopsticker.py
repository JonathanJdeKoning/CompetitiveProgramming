wc, hc, ws, hs = list(map(int, input().split()))

print("1") if ws <= (wc-2) and hs <= (hc-2) else print("0")