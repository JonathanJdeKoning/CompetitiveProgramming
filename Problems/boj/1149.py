n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

def min_costs(n):
    if n==0: return houses[0]
    choices = min_costs(n-1)
    return [houses[n][0]+ min(choices[1], choices[2]),houses[n][1]+ min(choices[0], choices[2]), houses[n][2]+min(choices[0], choices[1])]
    
print(min(min_costs(n-1)))
