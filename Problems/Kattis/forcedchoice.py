cards, secret, steps = list(map(int, input().split()))

for step in range(steps):
    choices = list(map(int, input().split()))[1:]
    
    if secret in choices:
        print("KEEP")
    else:
        print("REMOVE")
        