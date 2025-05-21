for tc in range(int(input())):
    N = int(input())
    out = [N]
    out.extend(list(range(1, N)))
    print(" ".join(map(str, out )))
    