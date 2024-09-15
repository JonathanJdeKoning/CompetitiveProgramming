base = {"1":"one", "2":"two","3": "three",  "4":"four", "5": "five", "6": "six","7":"seven","8":"eight","9":"nine"}
ten = {"2":"twenty","3": "thirty",  "4":"forty", "5": "fifty", "6": "sixty","7":"seventy","8":"eighty","9":"ninety"}
teen = {"10": "ten", "11":"eleven","12": "twelve",  "13":"thirteen", "14": "fourteen", "15": "fifteen","16":"sixteen","17":"seventeen","18":"eighteen", "19": "nineteen"}
n = input()
if n == "0":
    exit(print("zero"))
if n in base:
    exit(print(base[n]))
    
if n in teen:
    exit(print(teen[n]))
if n[1] == "0":
    exit(print(ten[n[0]]))

print(f"{ten[n[0]]}-{base[n[1]]}")


