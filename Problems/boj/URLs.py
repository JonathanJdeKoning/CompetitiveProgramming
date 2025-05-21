N = int(input())
for tc in range(N):
    print(f"URL #{tc+1}")
    data = input()
    proto, data = data.split("://")
    print(f"Protocol = {proto}")
    port = "<default>"
    if ":" in data:
        d = data.split(":")
        port = d[1][:d[1].index("/")]
        data = d[0] +d[1][d[1].index("/"):]
    if "/"

    print(data)
