nums = int(input())

base = int(input())

processed = [base]
while len(processed) <= nums-1:
    num = int(input())
    processed.append(num)
    if num%base == 0:
        print(num)
        base = int(input())
        processed.append(base)
