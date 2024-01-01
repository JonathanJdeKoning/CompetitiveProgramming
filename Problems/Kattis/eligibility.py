tests = int(input())

for i in range(tests):
    string = input().split()
    name = string[0]

    beganpost = int(string[1].split("/")[0])

    dob = int(string[2].split("/")[0])
    courses = string[3]

    result = ""

    if beganpost >= 2010 or dob >= 1991:
        result = "eligible"
    else:
        if int(courses) >= 41:
            result = "ineligible"
        else:
            result = "coach petitions"
    print(f"{name} {result}")
