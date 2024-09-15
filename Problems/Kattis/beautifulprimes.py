D=input
for F in range(int(D())):
	A=int(D());B,C=11**A,0
	while len(str(B))!=A:B=B//11*7;C+=1
	E=['11']*(A-C)+['7']*C;print(' '.join(E))
