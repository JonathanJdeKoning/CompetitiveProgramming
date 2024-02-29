num2word = {}
word2num = {}

while True:
    try:
        sent = input().split()
        if sent[0] == "def":
            sent[2] = int(sent[2])
            if sent[1] in word2num:
                del num2word[word2num[sent[1]]]
            num2word[sent[2]] = sent[1]
            word2num[sent[1]] = sent[2]
        elif sent[0] == "calc":
            total = 0
            mult = 1
            for rest in sent[1:]:
                if rest == "+":
                    mult = 1
                elif rest == "-":
                    mult = -1
                elif rest == "=":
                    pass
                else:
                    if rest not in word2num:
                        total += -99999999999999
                    else:
                        total += mult*word2num[rest]
            print(" ".join(sent[1:]), end="")
            if total in num2word:
                print(f" {num2word[total]}")
            else:
                print(" unknown")
        elif sent[0] == "clear":
            num2word = {}
            word2num = {}

            
    except EOFError:
        break
