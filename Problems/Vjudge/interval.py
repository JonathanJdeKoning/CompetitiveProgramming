n = float(input())
if n<0 or n>100:
    print("Out of Intervals")
elif 0<=n<=25:
    print("Interval [0,25]")
elif n <= 50:
    print("Interval (25,50]")
elif n <=75:
    print("Interval (50,75]")
elif n <= 100:
    print("Interval (75,100]")
