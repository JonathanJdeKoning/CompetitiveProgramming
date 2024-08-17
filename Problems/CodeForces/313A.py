n = input()
if int(n) >0 :print(n)

else:
    print(max(int(n[:-1]),  int(n[:-2]+n[-1]) ))
