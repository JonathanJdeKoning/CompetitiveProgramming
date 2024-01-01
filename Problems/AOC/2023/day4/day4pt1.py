sum = 0
with open("input.txt", "r") as file:
    for line in [x.strip() for x in file.readlines()]:
        data = line.replace(":", "|").split("|")
        winners = data[1].split()
        nums = data[2].split()
        
        goodie = 1
        for num in nums:
            if num in winners:
                print(f"{num} is a winner! points: {goodie}")
                goodie*=2
        sum += goodie//2
print(sum)
