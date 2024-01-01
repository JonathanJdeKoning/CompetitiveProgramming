vardict = {}

while True:
    data = input()
    if data == "0": break
    if "=" in data:
        data = data.split(" = ")
        vardict[data[0]] = data[1]
    else:
        data = data.split(" + ")
        for i, thing in enumerate(data):
            if thing in vardict:
                data[i] = vardict[thing]
        total = 0
        for item in data:
            try:
                item = int(item)
                total += item

            except:
                continue
        data = [x for x in data if not x.isdigit()]
        if total != 0:
            data = [total] + data
        print(" + ".join([str(x) for x in data]))
