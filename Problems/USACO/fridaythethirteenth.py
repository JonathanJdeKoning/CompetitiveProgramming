"""
ID: jj720461
LANG: PYTHON3
TASK: friday
"""
import sys
sys.stdin = open("friday.in", "r")
n = int(input())


ans = {6: 0,
       0: 0,
       1: 0,
       2: 0,
       3: 0,
       4: 0,
       5: 0}


def isLeapYear(year):
    return year%400==0 if year%100==0 else year%4==0

def daysInMonth(year, month):
    if month in {9, 4, 6, 11}: return 30
    if month != 2: return 31
    return 29 if isLeapYear(year) else 28

def nextDay(currDay, currDOW, currMonth, currYear):
    monthDays = daysInMonth(currYear, currMonth)
    
    if currDay != monthDays:
        currDay += 1
        currDOW = (currDOW+1)%7
    else:
        currDay = 1
        currDOW = (currDOW+1)%7
        currMonth = (currMonth+1)%12

        if currMonth == 1: currYear += 1

    return (currDay, currDOW, currMonth, currYear)


currDay = 1
currDOW = 1
currMonth = 1
currYear = 1900

while True:
    currDay, currDOW, currMonth, currYear = nextDay(currDay, currDOW, currMonth, currYear)
    if currMonth==0 and currDay==31 and currYear == 1900+n-1: break


    if currDay == 13:
        ans[currDOW] += 1

with open("friday.out", "w") as file:
    file.write(" ".join(list(map(str, ans.values())))+"\n")











