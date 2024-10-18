N =int(input())
mp = {1:1, 2:2, 3:3}
guess = {1:0, 2:0, 3:0}
for _ in range(N):
    A,B,G = list(map(int, input().split()))
    mp[A], mp[B] = mp[B], mp[A]

    guess[mp[G]] += 1

print(max(guess.values()))

