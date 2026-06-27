day, month, year = input("What's your date of birth (Day/month/year): ").split("/")
Day, Month, Year = input("What's the date today (Day/month/year): ").split("/")

Day = int(Day)
Month = int(Month)
Year = int(Year)

day = int(day)
month = int(month)
year = int(year)

age_years = Year - year
age_month = Month - month
age_days = Day - day

if age_month < 0:
    age_years = age_years - 1
    age_month = 12 + age_month
    
if age_days < 0:
    age_month = age_month - 1
    if Month -1 in [1, 3, 5, 7, 8, 10, 0] :
        age_days = 31 +  age_days

    if Month -1 in [4, 6, 9, 11]:
        age_days = 30 + age_days

    if Month -1 == 2:
        if Year%4 == 0:
            age_days = 29 + age_days
        else:
            age_days = 28 + age_days

if age_years < 0:
    print("Do you think I am stupid, you are not born yet")
    
print("Congratulations!! you lived: " + str(age_years) + " years, " + str(age_month) + " months, " + str(age_days) + " days")
