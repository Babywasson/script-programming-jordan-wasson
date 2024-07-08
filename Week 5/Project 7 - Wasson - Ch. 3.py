salary = float(input("Please input the starting Salary: "))
yearlyRaise = float(input("Please input the percentage raise in decimal format (ex. if the raise = 5%, input .05): "))
conversionRate = float(1 + yearlyRaise)
yearsofService = int(input("Please input the amount of years worked: "))

print("%-17s%6s" %("Years of Service", "Salary"))
for year in range(2, yearsofService+1):
    salary = salary * conversionRate
    print("%-17d$ %6.2f" % (year, salary))
print("This chart will show your raises for the next ", yearsofService, " years.")
