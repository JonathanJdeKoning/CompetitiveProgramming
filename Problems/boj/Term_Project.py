ans = 0
for _ in range(int(input())):
    N = int(input())
    pick =list(map(lambda x: int(x)-1, input().split()))
    done = [0]*N
    ans = 0
    for i in range(N):
        if done[i]: continue
        path = [i]
        seen = set([i])
        curr = i

        while True:
            new = pick[curr]
            if done[new]:
                for left in path:
                    done[left] = 1
                    ans += 1
                break

            if new in seen:
                while True:
                    p = path.pop()
                    done[p] = 1
                    if p == new:
                        for left in path:
                            done[left] = 1
                            ans += 1
                        break
                break
            else:
                path.append(new)
                seen.add(new)
                curr = new

    print(ans)
