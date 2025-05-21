year =  0
while True:
    data = input()
    year += 1
    if data == "0": break
    n, order = data.split()
    n = int(n)
    words= []
    for _ in range(n):
        word = [order.index(x) for x in list(input())]
        words.append(word)
    words.sort()
    print(f"year {year}")
    for word in words:
        print("".join([order[c] for c in word]))