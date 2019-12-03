Year = 0

Year = int(input("Enter a year to check if it leaps >>>"))

if (Year % 4) == 0:
    if (Year % 100) == 0:
        if(Year % 400) == 0:
            print(Year, "is a leap year")
        else:
            print(Year, "is not a leap year")
    else:
        print(Year, "is a leap year")
else:
    print(Year, "is not a leap year")
