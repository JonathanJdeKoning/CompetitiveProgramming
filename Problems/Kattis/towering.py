data = list(map(int, input().split()))

h1 = data[-2]
h2 = data[-1]

boxes = data[:-2]
mn = min(boxes)
boxes.remove(mn)

find = h1-mn
find2 = h2-mn
one = []

for box in boxes:
    if (find-box) in boxes:
        one = sorted([mn, box, find-box], reverse=True)
        boxes.remove(box)
        boxes.remove(find-box)

    elif (find2-box) in boxes:
        one = sorted([mn, box, find2-box], reverse=True)
        boxes.remove(box)
        boxes.remove(find2-box)


if sum(one) == h1:
    print(" ".join([str(x) for x in one]), end =" ")
    print(" ".join([str(x) for x in sorted(boxes, reverse=True)]), end =" ")
else:
    print(" ".join([str(x) for x in sorted(boxes,reverse=True)]), end =" ")
    print(" ".join([str(x) for x in one]), end =" ")

    
        
