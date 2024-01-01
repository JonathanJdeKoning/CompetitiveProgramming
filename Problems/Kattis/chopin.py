notedict = {
    "A": "UNIQUE",
    "A#": "Bb",
    "Bb": "A#",
    "B": "UNIQUE",
    "C": "UNIQUE",
    "C#": "Db",
    "Db": "C#",
    "D": "UNIQUE",
    "D#": "Eb",
    "Eb": "D#",
    "E": "UNIQUE",
    "F": "UNIQUE",
    "F#": "Gb",
    "Gb": "F#",
    "G": "UNIQUE",
    "G#": "Ab",
    "Ab" : "G#"
}
count = 1
while True:
    try:
        
        text = input().split()
        
        newtext = f"Case {count}: "
        newtext += notedict[text[0]]
        if notedict[text[0]] != "UNIQUE":
            newtext += " "
            newtext += text[1]
        
        print(newtext)
        count += 1
        
         
    except EOFError:
        break