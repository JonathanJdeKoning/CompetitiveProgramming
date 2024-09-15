l,r = input().split("|")
l = list(l)
r = list(r)

w = list(input())

if (len(l)+len(r) + len(w))%2 == 1:
    exit(print("Impossible"))
else:
    need = (len(l)+len(w)+len(r))//2
    if len(l)>need or len(r)>need: exit(print("Impossible"))

    for c in w:
        if len(l) != need:
            l.append(c)
        else:
            r.append(c)


print(f'{"".join(l)}|{"".join(r)}')

    
