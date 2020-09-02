#Date_of_birth 

day = input("Day\n")
month = input("Month\n")
year = input("Year\n")
print("{}/{}/{}".format(day,month,year))

Date_of_birth = input("Date of Birth format DDMMYYYY:")
Day = Date_of_birth[:2]
Month = Date_of_birth[2:4]
Year = Date_of_birth[4:]
print(Day+"/"+Month+"/"+Year)

