print("This program is used to predict the growth of organisms.")
organismNumber = int(input("Input the initial number of organisms: "))
rateofGrowth = int(input("Input the rate at which the organisms grow: "))
grTimeline = int(input("Input the time it will take to acheive the rate of growth: "))
growthTimeFrame = int(input("Input the amount of hours the population is allowed to grow: "))
rogRatio = rateofGrowth * (growthTimeFrame / grTimeline)
newPopulation = organismNumber * rogRatio
print("The new population is ", newPopulation, "organisms.")
