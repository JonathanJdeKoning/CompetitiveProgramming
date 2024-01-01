people, pieces = list(map(int, input().split()))

res = pieces - people

if res >= 0:
    if res == 1:
        print(f"Dr. Chaz will have {res} piece of chicken left over!")
    else:
        print(f"Dr. Chaz will have {res} pieces of chicken left over!")

else:
    if res == -1:
        print(f"Dr. Chaz needs {abs(res)} more piece of chicken!")
    else: 
        print(f"Dr. Chaz needs {abs(res)} more pieces of chicken!")
