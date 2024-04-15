C=input
def A():
 F,G=map(int,C().split());A=['?']*F
 for J in range(G):
  H,I=C().split();B=int(H)-2
  for D in I:
   B+=1;E=A[B]
   if E=='?'or E==D:A[B]=D
   else:return'Villa'
 return''.join(A)
print(A())
