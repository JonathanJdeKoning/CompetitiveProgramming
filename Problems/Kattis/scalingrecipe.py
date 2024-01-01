ings, prodportions, needportions  = list(map(int, input().split()))

for i in range(ings):
    num = int(input())
    
    print(int((num/prodportions)*needportions))