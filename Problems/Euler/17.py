digs = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
tens = {
    "10": "ten",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
}
teens = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
ans = 0
test = [4, 17, 30, 45, 500, 814, 540, 508, 666, 1000]


def numLetters(s):
    if s in digs:
        return len(digs[s])
    if s in tens:
        return len(tens[s])
    if s in teens:
        return len(teens[s])

    if len(s) == 2:
        return len(tens[s[0] + "0"]) + len(digs[s[-1]])

    if len(s) == 3:
        ans = 0
        ans += len(digs[s[0]])
        ans += len("hundred")
        if s[1:] == "00":
            return ans

        ans += len("and")

        if s[1:] in teens:
            ans += len(teens[s[1:]])
            return ans

        if s[1] != "0":
            ans += len(tens[s[1] + "0"])
        if s[-1] != "0":
            ans += len(digs[s[-1]])
        return ans
    return 11


out = 0
for i in range(1, 1001):
    out += numLetters(str(i))

print(out)
