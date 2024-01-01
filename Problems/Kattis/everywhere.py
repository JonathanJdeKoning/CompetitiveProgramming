cases = int(input())
for case in range(cases):
    citylist = []
    
    cities = int(input())
    for city in range(cities):
        citylist.append(input())
    print(len(set(citylist)))