
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]


def mwf(sentences):
    return max(map(len, [x.split() for x in sentences]))
print(mwf(sentences))
