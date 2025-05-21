N =int(input()) - 1
ans = 0
threes = N//3
fives = N//5
fifteens = N//15

ans    +=  5 * ( fives ** 2  +  fives ) // 2
ans   +=  3 * ( threes ** 2  +  threes ) // 2
ans -= 15 * ( fifteens ** 2  +  fifteens ) // 2
print(ans)
