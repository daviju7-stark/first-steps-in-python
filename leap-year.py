#leap-year/año bisiesto
year= int(input("Year: "))
if year%4!=0:
    print("It's not a leap year")
else:
    if year%100!=0 or year%400==0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
