N = int(input())
channels = [input() for _ in range(N)]

one = channels.index("KBS1")

commands = [1]*one
commands.extend([4]*one)

curr = one
for i in range(one):
    channels[curr-1], channels[curr] = channels[curr], channels[curr-1]
    curr -= 1
two = channels.index("KBS2")
commands.extend([1]*(two))
commands.extend([4]*(two-1))

print("".join(map(str, commands)))
