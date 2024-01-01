nums = list(range(100))
nums = [str(num) for num in nums]
ones = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
problems = ["11","12","13","14","15","16","17","18","19"]
probs = {
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen"}
tens = {
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety"
}


while True:
    try:
        new = []
        line = input().split()
        for idx, word in enumerate(line):
            if word not in nums:
                new.append(word)
            else:
                out = ""
                fin = False
                if word in problems:
                    out = probs[word]
                    fin = True
                if len(word) == 2 and not fin:
                    out += tens[word[0]]
                    if word[1] != "0":
                        out += "-"
                        out += ones[word[1]]
                else:
                    if not fin:
                        out += ones[word[0]]
                if idx == 0:
                    bomba = out
                    out = ""
                    out+= bomba[0].upper()
                    out += bomba[1:]
                new.append(out)
        print(" ".join(new))
    except EOFError:
        break
