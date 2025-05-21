while True:
    try:
        ay, ax, by, bx, _, _, cy, cx = map(float, input().split())
    except EOFError: break
    aydiff, axdiff = by-ay,bx-ax
    cydiff, cxdiff = by-cy, bx-cx

    print(f"{by-aydiff-cydiff:.3f} {bx-axdiff-cxdiff:.3f}")