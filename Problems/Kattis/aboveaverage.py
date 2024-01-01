cases = int(input())

for case in range(cases):
    data = list(map(int, input().split()))
    students = data[0]
    data = data[1:]
    
    avg = sum(data) / students
    
    numabove = len([x for x in data if x > avg])
    output = 100*(numabove/students)
    print(f"{output:.3f}%")