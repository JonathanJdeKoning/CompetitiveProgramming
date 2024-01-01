for _ in range(int(input())):
    day, month = input().split()
    day = int(day)
    if month == "Mar" and day >= 21:
        print("Aries")
    elif month == "Apr" and day <= 20:
        print("Aries")

    elif month == "Apr" and day >= 21:
        print("Taurus")
    elif month == "May" and day <= 20:
        print("Taurus")

    elif month == "May" and day >= 21:
        print("Gemini")
    elif month == "Jun" and day <= 21:
        print("Gemini")

    elif month == "Jun" and day >= 22:
        print("Cancer")
    elif month == "Jul" and day <= 22:
        print("Cancer")

    elif month == "Jul" and day >= 23:
        print("Leo")
    elif month == "Aug" and day <= 22:
        print("Leo")

    elif month == "Aug" and day >= 23:
        print("Virgo")
    elif month == "Sep" and day <= 21:
        print("Virgo")

    elif month == "Sep" and day >= 22:
        print("Libra")
    elif month == "Oct" and day <= 22:
        print("Libra")

    elif month == "Oct" and day >= 23:
        print("Scorpio")
    elif month == "Nov" and day <= 22:
        print("Scorpio")

    elif month == "Nov" and day >= 23:
        print("Sagittarius")
    elif month == "Dec" and day <= 21:
        print("Sagittarius")

    elif month == "Dec" and day >= 22:
        print("Capricorn")
    elif month == "Jan" and day <= 20:
        print("Capricorn")

    elif month == "Jan" and day >= 21:
        print("Aquarius")
    elif month == "Feb" and day <= 19:
        print("Aquarius")

    elif month == "Feb" and day >= 20:
        print("Pisces")
    elif month == "Mar" and day <= 20:
        print("Pisces")
