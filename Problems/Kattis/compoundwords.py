import itertools
words = []

while True:
    try:
        line = input().split()
        for word in line:
            words.append(word)
        
        
    except EOFError:
        output = []
        combs = list(itertools.combinations(words, 2))
        for comb in combs:
            output.append(comb[0] + comb[1])
            output.append(comb[1] + comb[0])
        output = sorted(set(output))
        print("\n".join(output))
        break

