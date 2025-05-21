
def num(start, end):
    

def direc(start, end):
    if start == end: return "A"
    if start == "<":
        if end == "v":return ">A"
        elif end == ">":return ">>A"
        elif end == "^":return ">^A"
        elif end == "A":return ">>^A"
    elif start == "v":
        if end != "A":return end + "A"
        else:return ">^A"
    elif start == "^":
        if end == "<":return "v<A"
        elif end == "v":return "vA"
        elif end == ">":return "v>A"
        elif end == "A":return ">A"
    elif start == ">":
        if end == "<":return "<<A"
        elif end == "v":return "<A"
        elif end == "^":return "<^A"
        elif end == "A": return "^A"
    elif start == "A":
        if end == "<": return "v<<A"
        elif end == ">": return "vA"
        elif end == "v":return "v<A"
        elif end == "^": return "<A" 
    