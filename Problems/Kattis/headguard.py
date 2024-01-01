from itertools import groupby

while True:
    try:
        string = input()
        myarr = ["".join(group) for ele, group in groupby(string)]

        output = ""

        for animal in myarr:
            output += str(len(animal))
            output += animal[0]
        print(output)
         
    except EOFError:
        break
